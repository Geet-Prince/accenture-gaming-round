/**
 * Firebase Auth & Cloud Firestore Synchronization Manager
 * Accenture Gamified Assessment Simulator
 *
 * Document ID Strategy: Always use user.uid as the Firestore document ID.
 * This guarantees security rules (request.auth.uid == userDocId) always pass.
 * Username and email are stored as fields inside the document for display.
 */

class FirebaseSyncManager {
    constructor() {
        this.app = null;
        this.auth = null;
        this.db = null;
        this.currentUser = null;
        this.lastSyncError = null;
        this.isSyncing = false;
        this.lastSyncTime = null;
        this.debounceTimeout = null;

        this.init();
    }

    init() {
        if (typeof firebase === 'undefined') {
            console.warn('[Firebase] SDK not loaded.');
            return false;
        }

        try {
            if (!firebase.apps.length) {
                this.app = firebase.initializeApp(window.FIREBASE_CONFIG);
            } else {
                this.app = firebase.app();
            }

            this.auth = firebase.auth();
            this.db = firebase.firestore();

            // Initialize Analytics if supported
            if (window.FIREBASE_CONFIG && window.FIREBASE_CONFIG.measurementId && typeof firebase.analytics === 'function') {
                try {
                    this.analytics = firebase.analytics();
                } catch (e) {
                    console.debug('[Firebase Analytics]', e);
                }
            }

            // Auth state listener — fires on page load for persisted sessions
            this.auth.onAuthStateChanged(user => {
                this.currentUser = user;
                this.updateUI();

                if (user) {
                    // Only sync from onAuthStateChanged if not already mid-sync
                    // (signInWithGoogle / signInWithEmail also trigger sync directly)
                    if (!this.isSyncing) {
                        this._doSync(user).catch(err => {
                            console.warn('[AuthStateChanged Sync Error]', err);
                        });
                    }
                }
            });

            return true;
        } catch (err) {
            console.error('[Firebase Init Error]', err);
            return false;
        }
    }

    /* --------------------------------------------------------------------------
       AUTHENTICATION METHODS
       -------------------------------------------------------------------------- */
    async signInWithGoogle() {
        if (!this.auth) {
            throw new Error('Firebase is not initialized. Please configure your Firebase keys first.');
        }
        const provider = new firebase.auth.GoogleAuthProvider();
        provider.setCustomParameters({ prompt: 'select_account' });
        const cred = await this.auth.signInWithPopup(provider);
        if (cred && cred.user) {
            this.currentUser = cred.user;
            this.updateUI();
            // Explicitly sync immediately after Google sign-in
            await this._doSync(cred.user);
        }
        return cred;
    }

    async signInWithEmail(email, password) {
        if (!this.auth) {
            throw new Error('Firebase is not initialized. Please configure your Firebase keys first.');
        }
        const cred = await this.auth.signInWithEmailAndPassword(email.trim(), password);
        if (cred && cred.user) {
            this.currentUser = cred.user;
            this.updateUI();
            await this._doSync(cred.user);
        }
        return cred;
    }

    async signUpWithEmail(email, password, displayName = '') {
        if (!this.auth) {
            throw new Error('Firebase is not initialized. Please configure your Firebase keys first.');
        }
        const cred = await this.auth.createUserWithEmailAndPassword(email.trim(), password);
        if (displayName && cred.user) {
            await cred.user.updateProfile({ displayName: displayName.trim() });
        }
        if (cred && cred.user) {
            this.currentUser = cred.user;
            this.updateUI();
            await this._doSync(cred.user);
        }
        return cred;
    }

    async signOut() {
        if (!this.auth) return;
        await this.auth.signOut();
        this.currentUser = null;
        this.lastSyncError = null;
        this.isSyncing = false;
        if (this.debounceTimeout) {
            clearTimeout(this.debounceTimeout);
            this.debounceTimeout = null;
        }
        this.updateUI();
    }

    /* --------------------------------------------------------------------------
       CLOUD FIRESTORE SYNCHRONIZATION
       --------------------------------------------------------------------------
       IMPORTANT: Document ID is ALWAYS user.uid.
       This is the only strategy that satisfies the Firestore security rule:
         allow create/update: if request.auth.uid == userDocId
       Username and email are stored as fields (not as the document ID).
       -------------------------------------------------------------------------- */

    /**
     * Internal sync method — always writes to users/{uid}.
     * Called by auth methods and onAuthStateChanged.
     */
    async _doSync(user) {
        if (!this.db || !user) return;

        // Prevent parallel sync runs
        if (this.isSyncing) {
            console.debug('[Firebase Sync] Already syncing, skipping duplicate call.');
            return;
        }
        this.isSyncing = true;
        this.setSyncStatus('SYNCING');

        try {
            const docId = user.uid;                                         // Always UID
            const userRef = this.db.collection('users').doc(docId);

            // --- Step 1: Read existing cloud document ---
            let cloudData = null;
            try {
                const snap = await userRef.get();
                if (snap.exists) {
                    cloudData = snap.data();
                    console.log('[Firebase Sync] Existing doc found for uid:', docId);
                } else {
                    console.log('[Firebase Sync] New user — creating Firestore document for uid:', docId);
                }
            } catch (readErr) {
                // Permission denied on read — still attempt write (create may be allowed)
                console.warn('[Firebase Sync] Read failed (may be new user):', readErr.code || readErr.message);
            }

            // --- Step 2: Merge local + cloud progress ---
            const localProgress = this._loadLocalProgress();
            const cloudProgress = cloudData ? (cloudData.progress || null) : null;
            const mergedProgress = this._mergeProgress(localProgress, cloudProgress);

            // --- Step 3: Persist merged progress to localStorage & app ---
            const appInstance = window.app || (typeof app !== 'undefined' ? app : null);
            const storageKey = (appInstance && appInstance.storageKey) ? appInstance.storageKey : 'accenture_exam_sim_v3';
            if (appInstance) appInstance.progress = mergedProgress;
            try { localStorage.setItem(storageKey, JSON.stringify(mergedProgress)); } catch (_) {}

            // --- Step 4: Build and write the Firestore payload ---
            const username = user.email
                ? user.email.split('@')[0]
                : (user.displayName || 'Candidate');
            const nowIso = new Date().toISOString();

            const payload = {
                uid:         user.uid,
                username:    username,
                email:       user.email || '',
                displayName: user.displayName || username,
                photoURL:    user.photoURL || '',
                createdAt:   (cloudData && cloudData.createdAt) ? cloudData.createdAt : nowIso,
                lastLoginAt: nowIso,
                lastSyncedAt: nowIso,
                progress:    mergedProgress
            };

            await userRef.set(payload, { merge: true });
            console.log('[Firebase Sync] ✅ Document written successfully to users/' + docId);

            this.lastSyncTime = new Date();
            this.lastSyncError = null;
            this.setSyncStatus('SYNCED');

            // Refresh dashboard UI after cloud data is merged in
            if (appInstance && typeof appInstance.renderDashboard === 'function') {
                appInstance.renderDashboard();
            }
        } catch (err) {
            console.error('[Firebase Sync Error]', err.code || err.message, err);
            this.lastSyncError = err;
            this.setSyncStatus('ERROR', err);
            throw err;
        } finally {
            this.isSyncing = false;
        }
    }

    /** Public alias so existing callers (triggerManualSync, window.onload) still work */
    async syncCloudAndLocal(user) {
        return this._doSync(user || this.currentUser);
    }

    /* --------------------------------------------------------------------------
       PROGRESS HELPERS
       -------------------------------------------------------------------------- */
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
        // Prefer live in-memory progress from the running app instance
        if (appInstance && appInstance.progress && appInstance.progress.games &&
            Object.keys(appInstance.progress.games).length > 0) {
            return appInstance.progress;
        }
        // Fall back to localStorage
        const storageKey = (appInstance && appInstance.storageKey) ? appInstance.storageKey : 'accenture_exam_sim_v3';
        try {
            const raw = localStorage.getItem(storageKey);
            if (raw) {
                const parsed = JSON.parse(raw);
                if (parsed && parsed.games && Object.keys(parsed.games).length > 0) return parsed;
            }
        } catch (_) {}
        // Last resort: let the app generate a fresh structure
        if (appInstance && typeof appInstance.loadProgress === 'function') {
            return appInstance.loadProgress();
        }
        return this._createInitialProgress();
    }

    _mergeProgress(local, remote) {
        const base = this._createInitialProgress();
        const srcLocal  = (local  && local.games)  ? local  : base;
        const srcRemote = (remote && remote.games)  ? remote : null;

        const merged = {
            totalAttempts: Math.max(srcLocal.totalAttempts || 0, srcRemote ? (srcRemote.totalAttempts || 0) : 0),
            games:         {},
            gameAttempts:  {}
        };

        const allGameIds = ['pathfinder', 'bubblemath', 'memorymaze', 'keydoor', 'memoryrecall'];
        allGameIds.forEach(gid => {
            merged.games[gid] = {};
            merged.gameAttempts[gid] = Math.max(
                srcLocal.gameAttempts?.[gid]  || 0,
                srcRemote ? (srcRemote.gameAttempts?.[gid] || 0) : 0
            );

            for (let r = 1; r <= 15; r++) {
                const l   = srcLocal.games?.[gid]?.[r]  || {};
                const rem = srcRemote ? (srcRemote.games?.[gid]?.[r] || {}) : {};

                let bestTime = null;
                const lbt  = (l.bestTime   != null) ? l.bestTime   : null;
                const rbt  = (rem.bestTime != null) ? rem.bestTime : null;
                if (lbt !== null && rbt !== null) bestTime = Math.min(lbt, rbt);
                else if (lbt !== null)            bestTime = lbt;
                else if (rbt !== null)            bestTime = rbt;

                merged.games[gid][r] = {
                    completed: Boolean(l.completed || rem.completed),
                    bestTime:  bestTime,
                    highScore: Math.max(l.highScore || 0, rem.highScore || 0),
                    accuracy:  (l.accuracy  != null) ? l.accuracy  : (rem.accuracy  != null ? rem.accuracy  : null),
                    attempts:  Math.max(l.attempts  || 0, rem.attempts  || 0)
                };
            }
        });
        return merged;
    }

    /* --------------------------------------------------------------------------
       DEBOUNCED CLOUD SAVE (called after each game level completion)
       -------------------------------------------------------------------------- */
    queueCloudSave(progress) {
        if (!this.currentUser || !this.db) return;

        this.setSyncStatus('SYNCING');
        if (this.debounceTimeout) clearTimeout(this.debounceTimeout);

        this.debounceTimeout = setTimeout(async () => {
            try {
                const docId   = this.currentUser.uid;            // Always UID
                const userRef = this.db.collection('users').doc(docId);
                const username = this.currentUser.email
                    ? this.currentUser.email.split('@')[0]
                    : (this.currentUser.displayName || 'Candidate');

                const updatePayload = {
                    uid:          this.currentUser.uid,
                    username:     username,
                    email:        this.currentUser.email || '',
                    displayName:  this.currentUser.displayName || username,
                    photoURL:     this.currentUser.photoURL || '',
                    lastSyncedAt: new Date().toISOString(),
                    progress:     progress
                };

                await userRef.set(updatePayload, { merge: true });
                this.lastSyncTime  = new Date();
                this.lastSyncError = null;
                this.setSyncStatus('SYNCED');
            } catch (e) {
                console.error('[Cloud Save Error]', e.code || e.message, e);
                this.lastSyncError = e;
                this.setSyncStatus('ERROR', e);
            }
        }, 1200);
    }

    /* --------------------------------------------------------------------------
       UI UPDATES & STATUS INDICATORS
       -------------------------------------------------------------------------- */
    setSyncStatus(status, err = null) {
        const badge = document.getElementById('firebase-sync-status');
        if (!badge) return;

        if (status === 'SYNCING') {
            badge.innerHTML = `<span class="inline-flex items-center gap-1.5 text-[11px] text-cyan-400 font-medium"><i class="fas fa-spinner fa-spin"></i> Syncing...</span>`;
        } else if (status === 'SYNCED') {
            const timeStr = this.lastSyncTime
                ? this.lastSyncTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
                : 'now';
            badge.innerHTML = `<span class="inline-flex items-center gap-1.5 text-[11px] text-emerald-400 font-medium" title="Synced to Firebase Cloud"><i class="fas fa-cloud-check"></i> Synced (${timeStr})</span>`;
        } else if (status === 'ERROR') {
            const errCode = (err && (err.code || err.message))
                ? (err.code || err.message)
                : (this.lastSyncError ? (this.lastSyncError.code || this.lastSyncError.message) : 'Sync Error');
            badge.innerHTML = `<button type="button" onclick="showSyncErrorDetails()" class="inline-flex items-center gap-1.5 text-[11px] text-rose-400 font-medium hover:underline cursor-pointer" title="Click for error details: ${errCode}"><i class="fas fa-triangle-exclamation"></i> Sync Error</button>`;
        } else {
            badge.innerHTML = `<span class="inline-flex items-center gap-1.5 text-[11px] text-gray-400 font-medium"><i class="fas fa-hard-drive"></i> Local Storage</span>`;
        }
    }

    updateUI() {
        const user = this.currentUser;
        const loggedOutContainer = document.getElementById('firebase-auth-logged-out');
        const loggedInContainer  = document.getElementById('firebase-auth-logged-in');
        const userAvatar = document.getElementById('firebase-user-avatar');
        const userName   = document.getElementById('firebase-user-name');
        const userEmail  = document.getElementById('firebase-user-email');

        if (user) {
            if (loggedOutContainer) loggedOutContainer.classList.add('hidden');
            if (loggedInContainer)  loggedInContainer.classList.remove('hidden');

            const name = user.displayName || user.email?.split('@')[0] || 'Candidate';
            if (userName)  userName.textContent  = name;
            if (userEmail) userEmail.textContent = user.email || '';

            if (userAvatar) {
                if (user.photoURL) {
                    userAvatar.src = user.photoURL;
                    userAvatar.classList.remove('hidden');
                    const initial = document.getElementById('firebase-user-initial');
                    if (initial) initial.classList.add('hidden');
                } else {
                    userAvatar.classList.add('hidden');
                    const initial = document.getElementById('firebase-user-initial');
                    if (initial) {
                        initial.textContent = name.charAt(0).toUpperCase();
                        initial.classList.remove('hidden');
                    }
                }
            }

            if (!this.isSyncing && !this.lastSyncError) {
                this.setSyncStatus(this.lastSyncTime ? 'SYNCED' : 'LOCAL');
            }
        } else {
            if (loggedOutContainer) loggedOutContainer.classList.remove('hidden');
            if (loggedInContainer)  loggedInContainer.classList.add('hidden');
            this.setSyncStatus('LOCAL');
        }

        if (typeof window.updateAuthGate === 'function') {
            window.updateAuthGate(user);
        }
    }
}

// Global singleton instance
window.firebaseSync = new FirebaseSyncManager();
