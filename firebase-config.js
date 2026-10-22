/**
 * Firebase Configuration for Accenture Gaming Assessment Simulator
 * 
 * Instructions:
 * 1. Create a free project at https://console.firebase.google.com/
 * 2. In Project Settings > General, scroll to "Your apps" and add a Web App ("</>").
 * 3. Copy the firebaseConfig keys and paste them below, OR configure them directly
 *    inside the website UI via the "Firebase Setup" button in the navigation bar!
 */

// Check if user saved custom keys in localStorage through the in-app modal
const savedCustomConfig = localStorage.getItem('accenture_firebase_custom_config');

window.FIREBASE_CONFIG = savedCustomConfig ? JSON.parse(savedCustomConfig) : {
    apiKey: "AIzaSy_YOUR_API_KEY_HERE",
    authDomain: "accenture-gaming-round.firebaseapp.com",
    projectId: "accenture-gaming-round",
    storageBucket: "accenture-gaming-round.appspot.com",
    messagingSenderId: "123456789012",
    appId: "1:123456789012:web:abcdef1234567890"
};

// Helper to check if credentials have been replaced with real project keys
window.isFirebaseConfigured = function() {
    const cfg = window.FIREBASE_CONFIG;
    return cfg && cfg.apiKey && !cfg.apiKey.includes('YOUR_API_KEY_HERE') && cfg.projectId && !cfg.projectId.includes('accenture-gaming-round-demo');
};
