/**
 * Firebase Configuration for Accenture Gaming Assessment Simulator
 * Project: accenture-gaming-round
 */

// Check if user saved custom keys in localStorage through the in-app modal
const savedCustomConfig = localStorage.getItem('accenture_firebase_custom_config');

window.FIREBASE_CONFIG = savedCustomConfig ? JSON.parse(savedCustomConfig) : {
    apiKey: "AIzaSyBLq0ZdrD-RVsbhbdpTHuckBIOLz0UsSuM",
    authDomain: "accenture-gaming-round.firebaseapp.com",
    projectId: "accenture-gaming-round",
    storageBucket: "accenture-gaming-round.firebasestorage.app",
    messagingSenderId: "736707201769",
    appId: "1:736707201769:web:10f038a419b3cecf5bbe78",
    measurementId: "G-ERNX8HNKDX"
};

// Helper to check if credentials have been replaced with real project keys
window.isFirebaseConfigured = function() {
    const cfg = window.FIREBASE_CONFIG;
    return Boolean(cfg && cfg.apiKey && !cfg.apiKey.includes('YOUR_API_KEY_HERE') && cfg.projectId);
};
