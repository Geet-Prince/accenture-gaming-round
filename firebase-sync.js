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
        this.updateUI();
    }

    /* --------------------------------------------------------------------------
       CLOUD FIRESTORE SYNCHRONIZATION
       -------------------------------------------------------------------------- */
    async syncCloudAndLocal(user) {
        if (!this.db || !user || !window.app) return;

        this.setSyncStatus('SYNCING');
        try {
            const userRef = this.db.collection('users').doc(user.uid);
            const doc = await userRef.get();

            let cloudProgress = null;
            if (doc.exists) {
                const data = doc.data();
                cloudProgress = data.progress || null;
            }

            const localProgress = window.app.progress || window.app.loadProgress();
            const mergedProgress = this.mergeProgress(localProgress, cloudProgress);

            // Save merged progress locally
            window.app.progress = mergedProgress;
            localStorage.setItem(window.app.storageKey, JSON.stringify(mergedProgress));

            // Push merged progress to cloud
            await userRef.set({
                uid: user.uid,
                email: user.email || '',
                displayName: user.displayName || user.email?.split('@')[0] || 'Candidate',
                photoURL: user.photoURL || '',
                lastLoginAt: firebase.firestore.FieldValue.serverTimestamp(),
                lastSyncedAt: new Date().toISOString(),
                progress: mergedProgress
            }, { merge: true });

            this.lastSyncTime = new Date();
            this.setSyncStatus('SYNCED');

            // Refresh app dashboard UI
            if (window.app && typeof window.app.renderDashboard === 'function') {
                window.app.renderDashboard();
            }
        } catch (err) {
            console.error('[Firebase Sync Error]', err);
            this.setSyncStatus('ERROR');
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
                const userRef = this.db.collection('users').doc(this.currentUser.uid);
                await userRef.set({
                    lastSyncedAt: new Date().toISOString(),
                    progress: progress
                }, { merge: true });

                this.lastSyncTime = new Date();
                this.setSyncStatus('SYNCED');
            } catch (e) {
                console.error('[Cloud Save Error]', e);
                this.setSyncStatus('ERROR');
            }
        }, 1200);
    }

    /* --------------------------------------------------------------------------
       UI UPDATES & STATUS INDICATORS
       -------------------------------------------------------------------------- */
    setSyncStatus(status) {
        const badge = document.getElementById('firebase-sync-status');
        if (!badge) return;

        if (status === 'SYNCING') {
            badge.innerHTML = `<span class="inline-flex items-center gap-1.5 text-[11px] text-cyan-400 font-medium"><i class="fas fa-spinner fa-spin"></i> Syncing...</span>`;
        } else if (status === 'SYNCED') {
            const timeStr = this.lastSyncTime ? this.lastSyncTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : 'now';
            badge.innerHTML = `<span class="inline-flex items-center gap-1.5 text-[11px] text-emerald-400 font-medium" title="Synced to Firebase Cloud"><i class="fas fa-cloud-check"></i> Synced (${timeStr})</span>`;
        } else if (status === 'ERROR') {
            badge.innerHTML = `<span class="inline-flex items-center gap-1.5 text-[11px] text-rose-400 font-medium" title="Sync Error - Check Firebase configuration"><i class="fas fa-triangle-exclamation"></i> Sync Error</span>`;
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
    }
}

// Global instance
window.firebaseSync = new FirebaseSyncManager();
