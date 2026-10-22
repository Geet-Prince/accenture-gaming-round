/**
 * Firebase Auth & Cloud Firestore Synchronization Manager
 * Accenture Gamified Assessment Simulator
 *
 * SDK: Firebase v10 Compat (loaded via CDN, global `firebase` object)
 * Document ID strategy: ALWAYS user.uid — guarantees security rule ownership check passes.
 */

class FirebaseSyncManager {
    constructor() {
        this.app          = null;
        this.auth         = null;
        this.db           = null;
        this.currentUser  = null;
        this.lastSyncError = null;
        this.isSyncing    = false;
        this.lastSyncTime = null;
        this.debounceTimeout = null;

        this.init();
    }

    /* -------------------------------------------------------------------------
       INITIALIZATION
       ------------------------------------------------------------------------- */
    init() {
        if (typeof firebase === 'undefined') {
            console.error('[Firebase] ❌ SDK scripts not loaded. Check your <script> tags.');
            return false;
        }

        try {
            // Initialise the Firebase app (only once)
            if (!firebase.apps.length) {
                this.app = firebase.initializeApp(window.FIREBASE_CONFIG);
            } else {
                this.app = firebase.app();
            }

            this.auth = firebase.auth();
            this.db   = firebase.firestore();

            console.log('[Firebase] ✅ App, Auth, Firestore initialised. Project:', window.FIREBASE_CONFIG?.projectId);

            // Analytics — optional, ignore failures
            if (window.FIREBASE_CONFIG?.measurementId && typeof firebase.analytics === 'function') {
                try { this.analytics = firebase.analytics(); } catch (_) {}
            }

            // ---------------------------------------------------------------
            // Auth state listener
            // Fires immediately on page load (persisted session) AND after
            // every sign-in / sign-out.
            // ---------------------------------------------------------------
            this.auth.onAuthStateChanged(user => {
                console.log('[Firebase] onAuthStateChanged fired. User:', user ? user.uid : 'null');
                this.currentUser = user;
                this.updateUI();

                if (user) {
                    // If signInWithGoogle() already called _doSync() for THIS session,
                    // isSyncing will be true — skip to avoid double write.
                    // On a FRESH PAGE LOAD with a persisted session, isSyncing is false,
                    // so this path handles the "returning user" case.
                    if (!this.isSyncing) {
                        this._doSync(user).catch(err => {
                            console.warn('[Firebase] onAuthStateChanged sync failed:', err?.code || err?.message);
                        });
                    }
                }
            });

            return true;
        } catch (err) {
            console.error('[Firebase] ❌ Init error:', err);
            return false;
        }
    }

    /* -------------------------------------------------------------------------
       AUTH — GOOGLE SIGN-IN (only sign-in method enabled)
       ------------------------------------------------------------------------- */
    async signInWithGoogle() {
        if (!this.auth) {
            throw new Error('Firebase Auth is not initialised. Check your config.');
        }

        console.log('[Firebase] Starting Google Sign-In popup…');

        const provider = new firebase.auth.GoogleAuthProvider();
        provider.setCustomParameters({ prompt: 'select_account' });

        // signInWithPopup resolves AFTER the popup closes and Firebase confirms auth.
        let cred;
        try {
            cred = await this.auth.signInWithPopup(provider);
        } catch (authErr) {
            console.error('[Firebase] ❌ Google Auth error:', authErr.code, authErr.message);
            throw authErr; // rethrow so handleGoogleSignIn() can show UI error
        }

        console.log('[Firebase] ✅ Google Auth success. UID:', cred.user.uid);

        // Update local state immediately so the UI responds before Firestore finishes
        this.currentUser = cred.user;
        this.updateUI();

        // Write to Firestore — await so the caller can catch Firestore errors separately
        await this._doSync(cred.user);

        return cred;
    }

    async signOut() {
        if (!this.auth) return;
        await this.auth.signOut();
        this.currentUser   = null;
        this.lastSyncError = null;
        this.isSyncing     = false;
        if (this.debounceTimeout) {
            clearTimeout(this.debounceTimeout);
            this.debounceTimeout = null;
        }
        this.updateUI();
        console.log('[Firebase] User signed out.');
    }

    /* -------------------------------------------------------------------------
       FIRESTORE SYNC — _doSync(user)
       Always writes to users/{user.uid}.
       ------------------------------------------------------------------------- */
    async _doSync(user) {
        if (!this.db || !user) {
            console.warn('[Firebase Sync] _doSync called but db or user is missing.');
            return;
        }
        if (this.isSyncing) {
            console.debug('[Firebase Sync] Already syncing — skipping duplicate call for uid:', user.uid);
            return;
        }

        this.isSyncing = true;
        this.setSyncStatus('SYNCING');
        console.log('[Firebase Sync] Starting sync for uid:', user.uid);

        try {
            const docId   = user.uid;   // ← ALWAYS uid. Document ID == request.auth.uid → rules pass.
            const userRef = this.db.collection('users').doc(docId);

            // ------------------------------------------------------------------
            // Step 1: Read existing document
            // ------------------------------------------------------------------
            let cloudData = null;
            try {
                console.log('[Firebase Sync] Reading users/' + docId + '…');
                const snap = await userRef.get();
                if (snap.exists) {
                    cloudData = snap.data();
                    console.log('[Firebase Sync] Existing document found:', Object.keys(cloudData));
                } else {
                    console.log('[Firebase Sync] No existing document — this is a new user.');
                }
            } catch (readErr) {
                // permission-denied on read is NOT fatal for a new user —
                // the create rule may still allow the write.
                console.warn('[Firebase Sync] Read failed (' + (readErr.code || readErr.message) + '). Proceeding to write.');
            }

            // ------------------------------------------------------------------
            // Step 2: Merge progress (local wins for anything cloud doesn't have)
            // ------------------------------------------------------------------
            const localProgress  = this._loadLocalProgress();
            const cloudProgress  = cloudData?.progress || null;
            const mergedProgress = this._mergeProgress(localProgress, cloudProgress);

            // Persist merged progress back to localStorage + the live app instance
            const appInstance = window.app || (typeof app !== 'undefined' ? app : null);
            const storageKey  = appInstance?.storageKey ?? 'accenture_exam_sim_v3';
            if (appInstance) appInstance.progress = mergedProgress;
            try { localStorage.setItem(storageKey, JSON.stringify(mergedProgress)); } catch (_) {}

            // ------------------------------------------------------------------
            // Step 3: Build Firestore payload
            // ------------------------------------------------------------------
            const username = user.email
                ? user.email.split('@')[0]
                : (user.displayName || 'Candidate');
            const nowIso   = new Date().toISOString();

            const payload = {
                uid:          user.uid,
                username:     username,
                email:        user.email        || '',
                displayName:  user.displayName  || username,
                photoURL:     user.photoURL     || '',
                createdAt:    cloudData?.createdAt  ?? nowIso,
                lastLoginAt:  nowIso,
                lastSyncedAt: nowIso,
                progress:     mergedProgress
            };

            // ------------------------------------------------------------------
            // Step 4: Write to Firestore
            // set(..., { merge: true }) → creates doc if new, merges if existing
            // ------------------------------------------------------------------
            console.log('[Firebase Sync] Writing users/' + docId + ' with fields:', Object.keys(payload));
            await userRef.set(payload, { merge: true });
            console.log('[Firebase Sync] ✅ Firestore write SUCCESS for users/' + docId);

            this.lastSyncTime  = new Date();
            this.lastSyncError = null;
            this.setSyncStatus('SYNCED');

            // Refresh dashboard so cloud-merged scores appear immediately
            if (appInstance && typeof appInstance.renderDashboard === 'function') {
                appInstance.renderDashboard();
            }

        } catch (err) {
            // Log the full error so it appears in the browser console
            console.error(
                '[Firebase Sync] ❌ WRITE FAILED',
                '\n  Code   :', err.code    || 'N/A',
                '\n  Message:', err.message || 'N/A',
                '\n  Likely causes:',
                '\n    • Firestore Security Rules not yet published → go to',
                '\n      https://console.firebase.google.com/project/' + (window.FIREBASE_CONFIG?.projectId || 'YOUR_PROJECT') + '/firestore/rules',
                '\n      and click Publish.',
                '\n    • Firestore database not created yet → go to',
                '\n      https://console.firebase.google.com/project/' + (window.FIREBASE_CONFIG?.projectId || 'YOUR_PROJECT') + '/firestore',
                '\n      and click Create Database.',
                '\n  Full error object:', err
            );
            this.lastSyncError = err;
            this.setSyncStatus('ERROR', err);
            throw err; // rethrow so callers can handle UI feedback
        } finally {
            this.isSyncing = false;
        }
    }

    /** Public alias — keeps backward compatibility with any existing callers. */
    async syncCloudAndLocal(user) {
        return this._doSync(user || this.currentUser);
    }

    /* -------------------------------------------------------------------------
       DEBOUNCED CLOUD SAVE — called by saveProgress() after each level finish
       ------------------------------------------------------------------------- */
    queueCloudSave(progress) {
        if (!this.currentUser || !this.db) {
            console.debug('[Firebase Sync] queueCloudSave skipped — not signed in or db missing.');
            return;
        }

        this.setSyncStatus('SYNCING');
        if (this.debounceTimeout) clearTimeout(this.debounceTimeout);

        this.debounceTimeout = setTimeout(async () => {
            const docId   = this.currentUser.uid;   // Always uid
            const userRef = this.db.collection('users').doc(docId);
            const username = this.currentUser.email
                ? this.currentUser.email.split('@')[0]
                : (this.currentUser.displayName || 'Candidate');

            const updatePayload = {
                uid:          this.currentUser.uid,
                username:     username,
                email:        this.currentUser.email       || '',
                displayName:  this.currentUser.displayName || username,
                photoURL:     this.currentUser.photoURL    || '',
                lastSyncedAt: new Date().toISOString(),
                progress:     progress
            };

            try {
                console.log('[Firebase Sync] queueCloudSave writing users/' + docId + '…');
                await userRef.set(updatePayload, { merge: true });
                this.lastSyncTime  = new Date();
                this.lastSyncError = null;
                this.setSyncStatus('SYNCED');
                console.log('[Firebase Sync] ✅ queueCloudSave write SUCCESS');
            } catch (e) {
                console.error('[Firebase Sync] ❌ queueCloudSave FAILED:', e.code || e.message, e);
                this.lastSyncError = e;
                this.setSyncStatus('ERROR', e);
            }
        }, 1200);  // 1.2 s debounce to batch rapid level completions
    }

    /* -------------------------------------------------------------------------
       PROGRESS HELPERS
       ------------------------------------------------------------------------- */
    _createInitialProgress() {
        const gameIds = ['pathfinder', 'bubblemath', 'memorymaze', 'keydoor', 'memoryrecall'];
        const initial = { totalAttempts: 0, games: {}, gameAttempts: {} };
        gameIds.forEach(gid => {
            initial.games[gid] = {};
            initial.gameAttempts[gid] = 0;
            for (let r = 1; r <= 15; r++) {
                initial.games[gid][r] = {
                    completed: false,
                    bestTime:  null,
                    highScore: 0,
                    accuracy:  null,
                    attempts:  0
                };
            }
        });
        return initial;
    }

    _loadLocalProgress() {
        const appInstance = window.app || (typeof app !== 'undefined' ? app : null);
        if (appInstance?.progress?.games && Object.keys(appInstance.progress.games).length > 0) {
            return appInstance.progress;
        }
        const storageKey = appInstance?.storageKey ?? 'accenture_exam_sim_v3';
        try {
            const raw = localStorage.getItem(storageKey);
            if (raw) {
                const parsed = JSON.parse(raw);
                if (parsed?.games && Object.keys(parsed.games).length > 0) return parsed;
            }
        } catch (_) {}
        if (appInstance && typeof appInstance.loadProgress === 'function') {
            return appInstance.loadProgress();
        }
        return this._createInitialProgress();
    }

    _mergeProgress(local, remote) {
        const base      = this._createInitialProgress();
        const srcLocal  = local?.games  ? local  : base;
        const srcRemote = remote?.games ? remote : null;

        const merged = {
            totalAttempts: Math.max(srcLocal.totalAttempts || 0, srcRemote?.totalAttempts || 0),
            games:         {},
            gameAttempts:  {}
        };

        ['pathfinder', 'bubblemath', 'memorymaze', 'keydoor', 'memoryrecall'].forEach(gid => {
            merged.games[gid]       = {};
            merged.gameAttempts[gid] = Math.max(srcLocal.gameAttempts?.[gid] || 0,
                                                 srcRemote?.gameAttempts?.[gid] || 0);
            for (let r = 1; r <= 15; r++) {
                const l   = srcLocal.games?.[gid]?.[r]  || {};
                const rem = srcRemote?.games?.[gid]?.[r] || {};
                const lbt = l.bestTime   != null ? l.bestTime   : null;
                const rbt = rem.bestTime != null ? rem.bestTime : null;
                merged.games[gid][r] = {
                    completed: Boolean(l.completed || rem.completed),
                    bestTime:  (lbt != null && rbt != null) ? Math.min(lbt, rbt)
                             : (lbt != null ? lbt : rbt),
                    highScore: Math.max(l.highScore || 0, rem.highScore || 0),
                    accuracy:  l.accuracy  != null ? l.accuracy
                             : rem.accuracy != null ? rem.accuracy : null,
                    attempts:  Math.max(l.attempts || 0, rem.attempts || 0)
                };
            }
        });
        return merged;
    }

    /* -------------------------------------------------------------------------
       UI — SYNC STATUS BADGE
       ------------------------------------------------------------------------- */
    setSyncStatus(status, err = null) {
        const badge = document.getElementById('firebase-sync-status');
        if (!badge) return;

        if (status === 'SYNCING') {
            badge.innerHTML = `<span class="inline-flex items-center gap-1.5 text-[11px] text-cyan-400 font-medium"><i class="fas fa-spinner fa-spin"></i> Syncing…</span>`;
        } else if (status === 'SYNCED') {
            const t = this.lastSyncTime
                ? this.lastSyncTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
                : 'now';
            badge.innerHTML = `<span class="inline-flex items-center gap-1.5 text-[11px] text-emerald-400 font-medium" title="Synced to Firebase Cloud"><i class="fas fa-cloud-check"></i> Synced (${t})</span>`;
        } else if (status === 'ERROR') {
            const code = err?.code || err?.message || this.lastSyncError?.code || 'Sync Error';
            badge.innerHTML = `<button type="button" onclick="showSyncErrorDetails()" class="inline-flex items-center gap-1.5 text-[11px] text-rose-400 font-medium hover:underline cursor-pointer" title="${code}"><i class="fas fa-triangle-exclamation"></i> Sync Error</button>`;
        } else {
            badge.innerHTML = `<span class="inline-flex items-center gap-1.5 text-[11px] text-gray-400 font-medium"><i class="fas fa-hard-drive"></i> Local Storage</span>`;
        }
    }

    /* -------------------------------------------------------------------------
       UI — AUTH STATE (logged-in / logged-out pill in navbar)
       ------------------------------------------------------------------------- */
    updateUI() {
        const user = this.currentUser;
        const outEl   = document.getElementById('firebase-auth-logged-out');
        const inEl    = document.getElementById('firebase-auth-logged-in');
        const avatarEl = document.getElementById('firebase-user-avatar');
        const nameEl   = document.getElementById('firebase-user-name');
        const emailEl  = document.getElementById('firebase-user-email');
        const initEl   = document.getElementById('firebase-user-initial');

        if (user) {
            outEl?.classList.add('hidden');
            inEl?.classList.remove('hidden');

            const name = user.displayName || user.email?.split('@')[0] || 'Candidate';
            if (nameEl)  nameEl.textContent  = name;
            if (emailEl) emailEl.textContent = user.email || '';

            if (user.photoURL) {
                if (avatarEl) { avatarEl.src = user.photoURL; avatarEl.classList.remove('hidden'); }
                initEl?.classList.add('hidden');
            } else {
                avatarEl?.classList.add('hidden');
                if (initEl) { initEl.textContent = name.charAt(0).toUpperCase(); initEl.classList.remove('hidden'); }
            }

            // Only update badge text if sync is not already showing a live status
            if (!this.isSyncing && !this.lastSyncError) {
                this.setSyncStatus(this.lastSyncTime ? 'SYNCED' : 'LOCAL');
            }
        } else {
            outEl?.classList.remove('hidden');
            inEl?.classList.add('hidden');
            this.setSyncStatus('LOCAL');
        }

        if (typeof window.updateAuthGate === 'function') window.updateAuthGate(user);
    }
}

// ─── Global singleton ───────────────────────────────────────────────────────
window.firebaseSync = new FirebaseSyncManager();
