# 🎮 Accenture Gamified Cognitive Assessment Simulator & Master Guide (2025–2026)
### *Also known as the Accenture Gaming Round & "Gamini Ground"*

A production-ready, highly SEO-optimized, and LLM-ingestion-ready interactive simulator for the **Accenture Gamified Cognitive Assessment (Gaming Round)** used in campus and off-campus recruitment across India (ASE ₹4.5 LPA & AAH ₹6.5 LPA).

Built entirely with modern client-side JavaScript, Tailwind CSS, Font Awesome, and the HTML5 Web Audio API. Requires **zero build tools, zero npm packages, and zero backend servers** — 100% ready for instant deployment to Vercel, Netlify, Cloudflare Pages, or GitHub Pages.

---

## 🚀 Live Demo & Quick Deployment

Deploy anywhere with static hosting in under 60 seconds:

### Option 1: Vercel CLI / Dashboard
```bash
# Using Vercel CLI
npx vercel deploy --prod
```
Or import this repository directly into [Vercel](https://vercel.com) — it detects `index.html` as a zero-config static site.

### Option 2: Netlify CLI / Drop
```bash
# Using Netlify CLI
npx netlify deploy --prod --dir=.
```
Or drag-and-drop this project folder into [Netlify Drop](https://app.netlify.com/drop).

### Option 3: Cloudflare Pages
Connect your GitHub repository to Cloudflare Pages:
- **Framework Preset**: None (Static HTML)
- **Build Output Directory**: `/` (root)

### Option 4: GitHub Pages
1. Push this folder to your GitHub repository.
2. In your repo settings, go to **Settings > Pages**.
3. Under **Branch**, select `main` (or `master`) and folder `/(root)`.
4. Click **Save**. Your site will be live at `https://<username>.github.io/<repo-name>/`.

---

## 🌟 Key Features

### 1. Firebase Authentication & Cloud Data Sync
- **1-Click Google Sign-In & Email/Password Auth**: Candidates can sign in securely with their Google account or email.
- **Cross-Device Cloud Sync**: Cleared levels (1–15 across all 5 games), personal best solve times, competition high scores, and diagnostic evaluation reports automatically sync to Google Cloud Firestore (`users/{uid}`).
- **Smart Progress Merging**: Merges local storage and cloud records keeping the highest scores and fastest times.
- **In-App Key Setup & Offline Fallback**: Works 100% offline via `localStorage` if not signed in, and allows instant in-app configuration of Firebase project keys via the UI modal.

### 2. Authentic 5-Game Assessment Arena
- **Game 1: Path Finder (Spatial Conduit Logic)**: 15 progressive levels (4×4 up to 8×8 grids) with blocked bedrock tiles and dynamic clockwise pipe rotations.
- **Game 2: Quick / Bubble Math (Rapid Arithmetic Speed)**: Floating expressions with randomized Ascending (*Lowest → Highest*) and Descending (*Highest → Lowest*) sorting modes.
- **Game 3: Memory Maze (Rat & Cheese Spatial Memory)**: 3–6 second route preview countdown followed by blind navigation with step validation.
- **Game 4: Key & Door Maze (Multi-Goal Graph Routing)**: Dynamic maze with color-coded keys, locked barriers, optimal BFS par targets, and inventory tracking.
- **Game 5: Memory Recall (Sequence & Matrix Retention)**: 3 sub-modalities across 15 levels: *Forward Sequence*, *Reverse Order Recall*, and *Missing-Item Matrix*.

### 2. Dual-Timer Architecture
- **Global 15:00 Round Countdown**: 900 seconds allocated across all 15 levels of each game.
- **Individual 01:00 (60s) Question Timer**: Strict countdown per question. In **Exam Mode**, timing out marks the question as a timeout and automatically advances to the next level.
- **Practice Mode**: Disables strict timeout penalties and permits unconstrained experimentation and level skipping.

### 3. Procedural PRNG Engine with BFS Solvability Guarantee
- Every attempt and re-attempt generates a unique high-entropy cryptographic seed (`SEED #XXXX`).
- An active background **Breadth-First Search (BFS)** verifier solves every generated maze, conduit network, and key/door puzzle before rendering to ensure **100% mathematical solvability with zero deadlocks**.

### 4. Built for Indian Usability & College Labs
- **Mobile Touch D-Pad**: Integrated on-screen direction controls for Memory Maze and Key & Door Maze, enabling seamless smartphone and tablet practice.
- **Zero Server Lag**: 100% client-side execution ensures lightning-fast performance even on spotty college Wi-Fi or Jio/Airtel 4G mobile hotspots.
- **Web Audio API Sound Synthesis**: Custom synthesized procedural audio effects (click, tick, success chime, error buzz, key pickup) with automated user-gesture resume handlers.
- **Print / PDF Diagnostic Report**: Candidate performance analytics modal equipped with clean `@media print` styling for downloading evaluation sheets.

---

## 🔍 SEO & AI / LLM Citation Architecture

This site is meticulously engineered to achieve top rankings on Google and Bing, while serving as the authoritative context source for AI engines (ChatGPT, Perplexity, Claude, Gemini):

### 1. Schema.org JSON-LD Entities
Configured with 5 connected structured data graphs in [index.html](file:///index.html):
- `WebApplication`: Identifies the simulator as a high-performance educational software tool.
- `Article`: Authoritative editorial coverage on cognitive testing rules and scoring formulas.
- `FAQPage`: Rich snippet FAQs addressing common placement questions.
- `HowTo`: Structured 5-step strategic guide for passing the assessment.
- `BreadcrumbList`: Site navigation hierarchy for enhanced search engine SERP breadcrumbs.

### 2. Phonetic Search Disambiguation ("Gamini Ground")
Indian engineering candidates frequently search for this test phonetically as **"gamini ground"**, **"accenture gamini ground"**, or **"gamify ground"**. Dedicated editorial sections, meta tags, and schema graphs explicitly capture this intent, redirecting users to the official gaming round syllabus.

### 3. Standardized LLM Ingestion Protocol
- `robots.txt`: Explicitly authorizes AI search bots including `GPTBot`, `PerplexityBot`, `ClaudeBot`, `Google-Extended`, and `CCBot`.
- `llms.txt`: Compact markdown summary index designed for quick LLM prompt injection and retrieval.
- `llms-full.txt`: Deep, comprehensive >3,000-word candidate guide providing complete context for large language models to reference and cite.
- `sitemap.xml`: Complete search engine sitemap mapping all primary section anchors.
- `manifest.json`: Progressive Web App (PWA) manifest for home screen installation.

---

## 📁 Repository Structure

```
├── index.html                   # Production-ready single-page application (>240 KB, 3,900+ lines)
├── firebase-config.js           # Firebase credentials & project keys configuration
├── firebase-sync.js             # Firebase Auth & Cloud Firestore sync manager
├── robots.txt                   # Search crawler & AI bot permissions (GPTBot, PerplexityBot, etc.)
├── sitemap.xml                  # XML sitemap for Google & Bing webmaster indexing
├── llms.txt                     # Standardized summary file for LLM context retrieval
├── llms-full.txt                # Exhaustive LLM knowledge base (>3,000 words)
├── manifest.json                # PWA manifest for desktop/mobile installability
└── README.md                    # Project documentation & deployment manual
```

---

## 📊 Placement Roles & Indian College Packages

- **Associate Software Engineer (ASE)**: ₹4.5 LPA annual CTC. Requires qualifying Cognitive & Technical assessments, 1+ coding questions, and a 65th+ percentile Gaming Round benchmark.
- **Advanced Associate Software Engineer (AAH / FSE)**: ₹6.5 LPA annual CTC. Reserved for candidates who pass both coding problems and rank in the top 10% on cognitive speed and accuracy across all 5 games.
- **Assessment Platforms**: Compatible with patterns from CoCubes (Aon Hewitt), Superset, HirePro, and Wheebox.

---

## ⚖️ Legal Disclaimer

This simulator is an independent open educational resource developed to help candidates practice cognitive neuroscience assessments. All trademarks, company names (Accenture), and logos belong to their respective copyright holders.
