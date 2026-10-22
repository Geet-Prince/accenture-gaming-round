/**
 * Firebase Auth & Cloud Firestore Synchronization Manager
 * Accenture Gamified Assessment Simulator
 */

class FirebaseSyncManager {
    constructor() {
        this.app = null;
        this.auth = null;
        this.db = null;
        this.currentUser = null;
        this.currentUserDocId = null;
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

            // Setup Auth State Listener
            this.auth.onAuthStateChanged(user => {
                this.currentUser = user;
                this.updateUI();

                if (user && window.app) {
                    this.syncCloudAndLocal(user);
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
        return await this.auth.signInWithPopup(provider);
    }

    async signInWithEmail(email, password) {
        if (!this.auth) {
            throw new Error('Firebase is not initialized. Please configure your Firebase keys first.');
        }
        return await this.auth.signInWithEmailAndPassword(email.trim(), password);
    }

    async signUpWithEmail(email, password, displayName = '') {
        if (!this.auth) {
            throw new Error('Firebase is not initialized. Please configure your Firebase keys first.');
        }
        const cred = await this.auth.createUserWithEmailAndPassword(email.trim(), password);
        if (displayName && cred.user) {
            await cred.user.updateProfile({ displayName: displayName.trim() });
        }
        return cred;
    }

    async signOut() {
        if (!this.auth) return;
        await this.auth.signOut();
        this.currentUser = null;
        this.currentUserDocId = null;
        this.updateUI();
    }

    /* --------------------------------------------------------------------------
       CLOUD FIRESTORE SYNCHRONIZATION
       -------------------------------------------------------------------------- */
    getUserDocId(user) {
        if (!user) return null;
        if (user.email) {
            const parts = user.email.toLowerCase().trim().split('@');
            const username = parts[0].replace(/[^a-z0-9._-]/g, '');
            const domain = (parts[1] || '').split('.')[0].replace(/[^a-z0-9_-]/g, '');

            // For standard @gmail.com accounts (guaranteed globally unique by Google)
            if (parts[1] === 'gmail.com') {
                return username || user.uid;
            } else {
                // For college or custom domains (e.g. rahul@vit.ac.in -> rahul_vit)
                return domain ? `${username}_${domain}` : (username || user.uid);
            }
        } else if (user.displayName) {
            const cleanName = user.displayName.toLowerCase().trim().replace(/\s+/g, '_').replace(/[^a-z0-9._-]/g, '');
            return `${cleanName}_${user.uid.slice(0, 5)}`;
        }
        return user.uid;
    }

    async syncCloudAndLocal(user) {
        if (!this.db || !user || !window.app) return;

        this.setSyncStatus('SYNCING');
        try {
            let docId = this.getUserDocId(user);
            let userRef = this.db.collection('users').doc(docId);
            let doc = null;

            try {
                doc = await userRef.get();
            } catch (readErr) {
                // If another user already owns this exact ID, safety fallback with UID fragment
                docId = `${docId}_${user.uid.slice(0, 5)}`;
                userRef = this.db.collection('users').doc(docId);
                try { doc = await userRef.get(); } catch (e) { /* ignore */ }
            }

            this.currentUserDocId = docId;

            let cloudProgress = null;
            if (doc && doc.exists) {
                const data = doc.data();
                cloudProgress = data.progress || null;
            } else {
                // Check if candidate data was previously stored under user.uid (legacy migration)
                try {
                    const legacyRef = this.db.collection('users').doc(user.uid);
                    const legacyDoc = await legacyRef.get();
                    if (legacyDoc && legacyDoc.exists) {
                        cloudProgress = legacyDoc.data().progress || null;
                    }
                } catch (e) {
                    // Ignore legacy lookup errors
                }
            }

            const localProgress = window.app.progress || window.app.loadProgress();
            const mergedProgress = this.mergeProgress(localProgress, cloudProgress);

            // Save merged progress locally
            window.app.progress = mergedProgress;
            localStorage.setItem(window.app.storageKey, JSON.stringify(mergedProgress));

            const username = user.email ? user.email.split('@')[0] : (user.displayName || 'Candidate');
            const nowIso = new Date().toISOString();

            const payload = {
                uid: user.uid,
                username: username,
                email: user.email || '',
                displayName: user.displayName || username,
                photoURL: user.photoURL || '',
                lastLoginAt: nowIso,
                lastSyncedAt: nowIso,
                progress: mergedProgress
            };

            // Attempt 1: Save under username doc ID (e.g. users/geetprince)
            try {
                await userRef.set(payload, { merge: true });
                this.currentUserDocId = docId;
            } catch (err1) {
                console.warn('[Firebase Sync] Write to users/' + docId + ' failed. Falling back to users/' + user.uid, err1);
                // Attempt 2: Fallback to standard user.uid doc ID (works with classic rules)
                const uidRef = this.db.collection('users').doc(user.uid);
                await uidRef.set(payload, { merge: true });
                this.currentUserDocId = user.uid;
            }

            this.lastSyncTime = new Date();
            this.lastSyncError = null;
            this.setSyncStatus('SYNCED');

            // Refresh app dashboard UI
            if (window.app && typeof window.app.renderDashboard === 'function') {
                window.app.renderDashboard();
            }
        } catch (err) {
            console.error('[Firebase Sync Error]', err);
            this.lastSyncError = err;
            this.setSyncStatus('ERROR', err);
        }
    }

    mergeProgress(local, remote) {
        if (!remote || !remote.games) return local;
        if (!local || !local.games) return remote;

        const merged = {
            totalAttempts: Math.max(local.totalAttempts || 0, remote.totalAttempts || 0),
            games: {},
            gameAttempts: {}
        };

        const allGameIds = ['pathfinder', 'bubblemath', 'memorymaze', 'keydoor', 'memoryrecall'];

        allGameIds.forEach(gid => {
            merged.games[gid] = {};
            merged.gameAttempts[gid] = Math.max(local.gameAttempts?.[gid] || 0, remote.gameAttempts?.[gid] || 0);

            for (let r = 1; r <= 15; r++) {
                const l = local.games?.[gid]?.[r] || {};
                const rem = remote.games?.[gid]?.[r] || {};

                let bestTime = null;
                if (l.bestTime !== null && rem.bestTime !== null) {
                    bestTime = Math.min(l.bestTime, rem.bestTime);
                } else {
                    bestTime = l.bestTime !== null ? l.bestTime : rem.bestTime;
                }

                merged.games[gid][r] = {
                    completed: Boolean(l.completed || rem.completed),
                    bestTime: bestTime,
                    highScore: Math.max(l.highScore || 0, rem.highScore || 0),
                    accuracy: Math.max(l.accuracy || 0, rem.accuracy || 0),
                    attempts: Math.max(l.attempts || 0, rem.attempts || 0)
                };
            }
        });

        return merged;
    }

    queueCloudSave(progress) {
        if (!this.currentUser || !this.db) return;

        this.setSyncStatus('SYNCING');
        if (this.debounceTimeout) clearTimeout(this.debounceTimeout);

        this.debounceTimeout = setTimeout(async () => {
            try {
                const docId = this.currentUserDocId || this.getUserDocId(this.currentUser) || this.currentUser.uid;
                const updatePayload = {
                    lastSyncedAt: new Date().toISOString(),
                    progress: progress
                };

                try {
                    const userRef = this.db.collection('users').doc(docId);
                    await userRef.set(updatePayload, { merge: true });
                } catch (e1) {
                    const fallbackRef = this.db.collection('users').doc(this.currentUser.uid);
                    await fallbackRef.set(updatePayload, { merge: true });
                }

                this.lastSyncTime = new Date();
                this.lastSyncError = null;
                this.setSyncStatus('SYNCED');
            } catch (e) {
                console.error('[Cloud Save Error]', e);
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
            const timeStr = this.lastSyncTime ? this.lastSyncTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : 'now';
            badge.innerHTML = `<span class="inline-flex items-center gap-1.5 text-[11px] text-emerald-400 font-medium" title="Synced to Firebase Cloud"><i class="fas fa-cloud-check"></i> Synced (${timeStr})</span>`;
        } else if (status === 'ERROR') {
            const errCode = (err && (err.code || err.message)) ? (err.code || err.message) : (this.lastSyncError ? (this.lastSyncError.code || this.lastSyncError.message) : 'Sync Error');
            badge.innerHTML = `<button type="button" onclick="showSyncErrorDetails()" class="inline-flex items-center gap-1.5 text-[11px] text-rose-400 font-medium hover:underline cursor-pointer" title="Click to view error details: ${errCode}"><i class="fas fa-triangle-exclamation"></i> Sync Error</button>`;
        } else {
            badge.innerHTML = `<span class="inline-flex items-center gap-1.5 text-[11px] text-gray-400 font-medium"><i class="fas fa-hard-drive"></i> Local Storage</span>`;
        }
    }

    updateUI() {
        const user = this.currentUser;
        const loggedOutContainer = document.getElementById('firebase-auth-logged-out');
        const loggedInContainer = document.getElementById('firebase-auth-logged-in');
        const userAvatar = document.getElementById('firebase-user-avatar');
        const userName = document.getElementById('firebase-user-name');
        const userEmail = document.getElementById('firebase-user-email');

        if (user) {
            if (loggedOutContainer) loggedOutContainer.classList.add('hidden');
            if (loggedInContainer) loggedInContainer.classList.remove('hidden');

            const name = user.displayName || user.email?.split('@')[0] || 'Candidate';
            if (userName) userName.textContent = name;
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
            this.setSyncStatus('SYNCED');
        } else {
            if (loggedOutContainer) loggedOutContainer.classList.remove('hidden');
            if (loggedInContainer) loggedInContainer.classList.add('hidden');
            this.setSyncStatus('LOCAL');
        }

        if (typeof window.updateAuthGate === 'function') {
            window.updateAuthGate(user);
        }
    }
}

// Global instance
window.firebaseSync = new FirebaseSyncManager();
