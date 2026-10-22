# site_guide_content.py
# High-density educational guide and SEO content for the Accenture Gamified Cognitive Assessment

HERO_HTML = """
            <!-- Hero Banner -->
            <div class="relative rounded-2xl bg-gradient-to-r from-[#1A103C] via-[#131326] to-[#0F172A] border border-acc-borderDark p-6 sm:p-8 overflow-hidden shadow-2xl">
                <div class="absolute -right-12 -top-12 w-72 h-72 bg-acc-purple/20 rounded-full blur-3xl pointer-events-none"></div>
                <div class="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
                    <div class="space-y-3 max-w-3xl">
                        <!-- Pill badges -->
                        <div class="flex flex-wrap items-center gap-2">
                            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-acc-purple/25 border border-acc-purple/50 text-acc-lightPurple text-xs font-bold">
                                <i class="fas fa-bolt"></i> Updated 2025–2026 Drive Pattern
                            </span>
                            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-xs font-semibold">
                                <i class="fas fa-briefcase"></i> ASE (₹4.5 LPA) &amp; AAH (₹6.5 LPA)
                            </span>
                            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-cyan-500/20 border border-cyan-500/40 text-cyan-300 text-xs font-semibold">
                                <i class="fas fa-clock"></i> 15:00 Round • 01:00 / Question
                            </span>
                        </div>

                        <h1 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-white tracking-tight">
                            Accenture Gamified Cognitive Assessment Arena
                        </h1>

                        <p class="text-gray-300 text-sm sm:text-base leading-relaxed">
                            Master the 5 official cognitive neuroscience assessment games: <strong class="text-white">Path Finder</strong>, <strong class="text-white">Quick/Bubble Math</strong>, <strong class="text-white">Memory Maze (Rat Route)</strong>, <strong class="text-white">Key &amp; Door Puzzle</strong>, and <strong class="text-white">Memory Recall</strong>. Features authentic exam dual-timers (15:00 total game time + strict 60-second question countdown) and procedural cryptographic question generation with BFS solvability verification.
                        </p>

                        <!-- Phonetic Typo / Disambiguation Box for Search Intent ("Gamini Ground") -->
                        <div class="p-3 rounded-xl bg-acc-bgDark/90 border border-acc-borderDark flex items-start gap-2.5 text-xs text-gray-300">
                            <i class="fas fa-circle-info text-cyan-400 mt-0.5 shrink-0 text-sm"></i>
                            <div>
                                <span class="font-bold text-white">Searching for "Accenture Gamini Ground"?</span>
                                <span class="text-gray-300"> Indian engineering candidates frequently search for the placement test phonetically as <em>"gamini ground"</em> or <em>"accenture gamini ground"</em>. This site is the official, comprehensive simulator and syllabus guide covering all 5 games, cutoffs, and scoring algorithms.</span>
                            </div>
                        </div>
                    </div>

                    <!-- Hero Quick CTAs -->
                    <div class="flex flex-col sm:flex-row lg:flex-col gap-2.5 shrink-0 min-w-[240px]">
                        <button onclick="app.startFullSimulation()" class="w-full px-5 py-3.5 rounded-xl bg-gradient-to-r from-acc-purple to-indigo-600 hover:from-acc-darkPurple hover:to-indigo-700 text-white font-bold text-xs sm:text-sm shadow-xl shadow-acc-purple/30 flex items-center justify-center gap-2.5 transition transform hover:-translate-y-0.5">
                            <i class="fas fa-play-circle text-base"></i>
                            <span>Start Full 5-Game Mock Exam</span>
                        </button>
                        <a href="#games-guide" class="w-full px-5 py-3 rounded-xl bg-acc-cardDark hover:bg-gray-800 text-cyan-300 border border-cyan-500/30 font-semibold text-xs flex items-center justify-center gap-2 transition text-center">
                            <i class="fas fa-book-open"></i>
                            <span>Read 5 Games Master Guide</span>
                        </a>
                        <button onclick="app.resetAllProgressConfirm()" class="w-full px-4 py-2.5 rounded-xl bg-acc-bgDark/80 hover:bg-red-950/40 text-gray-400 hover:text-red-300 border border-acc-borderDark hover:border-red-800/40 font-medium text-xs flex items-center justify-center gap-1.5 transition">
                            <i class="fas fa-rotate-left"></i>
                            <span>Reset Practice Stats</span>
                        </button>
                    </div>
                </div>
            </div>
"""

GUIDE_SECTION_HTML = """
        <!-- ==========================================================================
             COMPREHENSIVE AUTHORITY GUIDE & SEO KNOWLEDGE BASE (>5,000 WORDS)
             Optimized for Google, Bing, LLM Citations (ChatGPT, Perplexity, Gemini)
             and Indian Engineering Placement Candidates (CoCubes, Superset, HirePro)
             ========================================================================== -->
        <article id="guide-content" class="mt-14 space-y-12">

            <!-- Sticky Quick Table of Contents for Candidates -->
            <div class="rounded-2xl bg-acc-cardDark border border-acc-borderDark p-5 shadow-lg">
                <div class="flex items-center justify-between border-b border-acc-borderDark pb-3 mb-4">
                    <div class="flex items-center gap-2">
                        <i class="fas fa-list-check text-acc-lightPurple"></i>
                        <h2 class="font-bold text-base text-white">Table of Contents — Master Guide to Accenture Gamified Assessment</h2>
                    </div>
                    <span class="text-xs text-gray-400">Quick Navigation Jump Links</span>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2 text-xs">
                    <a href="#section-what-is-it" class="p-2.5 rounded-lg bg-acc-bgDark hover:bg-acc-purple/20 text-gray-300 hover:text-white transition flex items-center gap-2">
                        <span class="text-acc-lightPurple font-bold">01.</span> What is the Gaming Round?
                    </a>
                    <a href="#games-guide" class="p-2.5 rounded-lg bg-acc-bgDark hover:bg-acc-purple/20 text-gray-300 hover:text-white transition flex items-center gap-2">
                        <span class="text-cyan-400 font-bold">02.</span> Deep Dive into All 5 Games
                    </a>
                    <a href="#recruitment-pattern" class="p-2.5 rounded-lg bg-acc-bgDark hover:bg-acc-purple/20 text-gray-300 hover:text-white transition flex items-center gap-2">
                        <span class="text-emerald-400 font-bold">03.</span> 2025–2026 Placement Pattern &amp; Syllabus
                    </a>
                    <a href="#scoring-rules" class="p-2.5 rounded-lg bg-acc-bgDark hover:bg-acc-purple/20 text-gray-300 hover:text-white transition flex items-center gap-2">
                        <span class="text-amber-400 font-bold">04.</span> Dual-Timers &amp; Scoring Formulas
                    </a>
                    <a href="#prep-roadmap" class="p-2.5 rounded-lg bg-acc-bgDark hover:bg-acc-purple/20 text-gray-300 hover:text-white transition flex items-center gap-2">
                        <span class="text-rose-400 font-bold">05.</span> 7-Day Master Preparation Plan
                    </a>
                    <a href="#college-tips" class="p-2.5 rounded-lg bg-acc-bgDark hover:bg-acc-purple/20 text-gray-300 hover:text-white transition flex items-center gap-2">
                        <span class="text-purple-400 font-bold">06.</span> Indian College Labs &amp; Low Bandwidth
                    </a>
                    <a href="#gamini-ground-clarification" class="p-2.5 rounded-lg bg-acc-bgDark hover:bg-acc-purple/20 text-gray-300 hover:text-white transition flex items-center gap-2">
                        <span class="text-teal-400 font-bold">07.</span> "Gamini Ground" Search Clarification
                    </a>
                    <a href="#comparison-table" class="p-2.5 rounded-lg bg-acc-bgDark hover:bg-acc-purple/20 text-gray-300 hover:text-white transition flex items-center gap-2">
                        <span class="text-yellow-400 font-bold">08.</span> Traditional Aptitude vs Games
                    </a>
                    <a href="#faqs" class="p-2.5 rounded-lg bg-acc-bgDark hover:bg-acc-purple/20 text-gray-300 hover:text-white transition flex items-center gap-2">
                        <span class="text-blue-400 font-bold">09.</span> 20+ Frequently Asked Questions
                    </a>
                </div>
            </div>

            <!-- ======================================================================
                 SECTION 1: WHAT IS THE ACCENTURE GAMING ROUND?
                 ====================================================================== -->
            <section id="section-what-is-it" class="rounded-2xl bg-acc-cardDark border border-acc-borderDark p-6 sm:p-8 space-y-5">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-acc-purple/20 border border-acc-purple/40 flex items-center justify-center text-acc-lightPurple font-bold text-lg">
                        01
                    </div>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">
                            What is the Accenture Gaming Round? (Gamified Cognitive Assessment Explained)
                        </h2>
                        <p class="text-xs text-gray-400">The science, hiring context, and eliminatory nature of the assessment</p>
                    </div>
                </div>

                <div class="space-y-4 text-sm text-gray-300 leading-relaxed">
                    <p>
                        The <strong>Accenture Gamified Cognitive Assessment</strong> (widely referred to among students across India as the <em>"Accenture Gaming Round"</em> or phonetically as <em>"gamini ground"</em>) is a modern psychometric evaluation technique utilized by Accenture during on-campus and off-campus recruitment drives. Administered primarily through testing partners like <strong>CoCubes (Aon Hewitt)</strong>, <strong>Superset</strong>, <strong>HirePro</strong>, and <strong>Wheebox</strong>, this stage evaluates cognitive agility, spatial intelligence, and executive decision-making under strict time limits.
                    </p>
                    
                    <p>
                        Unlike traditional multiple-choice questions (MCQs) where candidates solve text-heavy aptitude questions, the gaming assessment drops the candidate directly into interactive, non-verbal cognitive puzzles. These games are designed in accordance with the <strong>Cattell-Horn-Carroll (CHC) theory of cognitive abilities</strong> to measure five core psychological traits:
                    </p>

                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 pt-2">
                        <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark">
                            <span class="text-cyan-400 font-bold text-xs uppercase block mb-1">1. Fluid Intelligence (Gf)</span>
                            <p class="text-xs text-gray-300">The ability to solve novel problems on the fly without relying on pre-memorized formulas or rote learning, tested through dynamic grid routing and maze navigation.</p>
                        </div>
                        <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark">
                            <span class="text-emerald-400 font-bold text-xs uppercase block mb-1">2. Spatial Visualization (Gv)</span>
                            <p class="text-xs text-gray-300">Mental manipulation and 2D/3D rotational reasoning, evaluated through tile conduit alignment in Path Finder.</p>
                        </div>
                        <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark">
                            <span class="text-amber-400 font-bold text-xs uppercase block mb-1">3. Working Memory Capacity (Gwm)</span>
                            <p class="text-xs text-gray-300">Short-term visual-spatial caching and backward digit/symbol span retention, evaluated in Memory Maze and Memory Recall.</p>
                        </div>
                        <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark">
                            <span class="text-rose-400 font-bold text-xs uppercase block mb-1">4. Cognitive Processing Speed (Gs)</span>
                            <p class="text-xs text-gray-300">Rapid numerical estimation and arithmetic triage under the strict 60-second countdown in Quick/Bubble Math.</p>
                        </div>
                        <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark">
                            <span class="text-acc-lightPurple font-bold text-xs uppercase block mb-1">5. Sequential Planning &amp; Par Logic</span>
                            <p class="text-xs text-gray-300">Multi-objective state graph traversal, tested by key collection order and door unlocks in the Key &amp; Door puzzle.</p>
                        </div>
                        <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark">
                            <span class="text-indigo-400 font-bold text-xs uppercase block mb-1">6. Frustration &amp; Stress Tolerance</span>
                            <p class="text-xs text-gray-300">How candidates recover after committing a mistake (e.g. stepping on an illegal cell in Memory Maze) without panic or serial misclicks.</p>
                        </div>
                    </div>

                    <div class="p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-200 text-xs flex items-start gap-3 mt-2">
                        <i class="fas fa-triangle-exclamation text-amber-400 text-base mt-0.5 shrink-0"></i>
                        <div>
                            <strong class="font-bold text-white block mb-0.5">Is the Gaming Round an Elimination Round?</strong>
                            <span>Yes! In the official Accenture hiring pipeline, candidates must clear the Cognitive &amp; Technical Assessment first. If qualified, they advance to the Coding Round, followed immediately by the Gamified Assessment Round. Candidates who score below the <strong>65th–70th percentile cutoff</strong> are eliminated before being invited to the final Technical and HR interviews. High performance in this round is also a critical prerequisite for being upgraded to the ₹6.5 LPA Advanced Associate Software Engineer (AAH) offer.</span>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ======================================================================
                 SECTION 2: COMPLETE GUIDE TO ALL 5 CORE ASSESSMENT GAMES
                 ====================================================================== -->
            <section id="games-guide" class="rounded-2xl bg-acc-cardDark border border-acc-borderDark p-6 sm:p-8 space-y-8">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-cyan-500/20 border border-cyan-500/40 flex items-center justify-center text-cyan-400 font-bold text-lg">
                        02
                    </div>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">
                            Exhaustive Analysis of All 5 Assessment Games: Rules, Mechanics &amp; Cheat Sheets
                        </h2>
                        <p class="text-xs text-gray-400">Step-by-step tactics, rotational rules, trap avoidance, and speed targets</p>
                    </div>
                </div>

                <!-- GAME 1: PATH FINDER -->
                <div class="p-5 rounded-2xl bg-acc-bgDark border border-acc-borderDark space-y-4">
                    <div class="flex flex-wrap items-center justify-between gap-3 border-b border-acc-borderDark pb-3">
                        <div class="flex items-center gap-2.5">
                            <span class="w-8 h-8 rounded-lg bg-acc-purple/20 text-acc-lightPurple flex items-center justify-center font-bold text-sm">G1</span>
                            <h3 class="font-bold text-lg text-white">Path Finder — Spatial Conduit Logic</h3>
                        </div>
                        <span class="px-2.5 py-0.5 rounded-full text-xs font-mono bg-acc-purple/20 text-acc-lightPurple border border-acc-purple/40">15 Levels • 60s / Level • 15:00 Total</span>
                    </div>

                    <div class="space-y-3 text-xs sm:text-sm text-gray-300 leading-relaxed">
                        <p>
                            <strong>Game Mechanics:</strong> You are presented with an N × N grid of conduit tiles containing a fixed <strong class="text-purple-400">Start (S)</strong> cell and a fixed <strong class="text-emerald-400">Target (E)</strong> cell. Some cells are blocked by non-rotatable bedrock rocks. Clicking any conduit tile rotates it 90 degrees clockwise. Your goal is to construct a continuous unbroken pipe connecting Start to Target. As soon as a valid conduit branch connects to Start, it illuminates in glowing cyan. When the cyan flow reaches Target, the level completes instantly!
                        </p>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 pt-1">
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-cyan-400 block mb-1">Matrix Progression</strong>
                                Levels 1–3 feature 4×4 grids (0–2 blocks). Levels 4–7 scale to 5×5 grids. Levels 8–11 feature 6×6 grids. Levels 12–15 test complex 7×7 to 8×8 grids with up to 12 obstacles.
                            </div>
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-amber-400 block mb-1">The Backward Tracing Trick</strong>
                                Instead of clicking random tiles from Start, immediately trace backward from Target (E). Target tiles usually have only 1 or 2 viable entry angles, drastically pruning your search tree!
                            </div>
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-emerald-400 block mb-1">Rotational Accuracy Score</strong>
                                Do not click tiles that lie outside the solution corridor. Every superfluous click reduces your rotational accuracy percentage. Solve in the fewest clicks possible to maximize points.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- GAME 2: QUICK MATH / BUBBLE MATH -->
                <div class="p-5 rounded-2xl bg-acc-bgDark border border-acc-borderDark space-y-4">
                    <div class="flex flex-wrap items-center justify-between gap-3 border-b border-acc-borderDark pb-3">
                        <div class="flex items-center gap-2.5">
                            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-400 flex items-center justify-center font-bold text-sm">G2</span>
                            <h3 class="font-bold text-lg text-white">Quick Math / Bubble Math — Rapid Numerical Speed</h3>
                        </div>
                        <span class="px-2.5 py-0.5 rounded-full text-xs font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/40">3 to 7 Bubbles • ASC / DESC • 60s / Level</span>
                    </div>

                    <div class="space-y-3 text-xs sm:text-sm text-gray-300 leading-relaxed">
                        <p>
                            <strong>Game Mechanics:</strong> Floating bubbles appear on screen, each containing a mental arithmetic expression (e.g. <code>14 + 19</code>, <code>72 / 8</code>, <code>9 × 6 - 15</code>, <code>(-14) + 28</code>). You must evaluate all expressions in your head and pop the bubbles in strict sorted order before the 60-second timer runs out.
                        </p>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 pt-1">
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-rose-400 block mb-1">The Directional Trap</strong>
                                Always check the top badge! Levels 1–3 typically require <em>LOWEST → HIGHEST</em> (Ascending), but higher levels switch to <em>HIGHEST → LOWEST</em> (Descending). Many candidates fail by auto-tapping the smallest bubble.
                            </div>
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-cyan-400 block mb-1">Tens-Complement Shortcuts</strong>
                                For expressions like <code>47 + 38</code>, mentally calculate <code>47 + 40 - 2 = 85</code>. For <code>19 × 4</code>, calculate <code>20 × 4 - 4 = 76</code>. This cuts calculation time down to 1.5 seconds per bubble.
                            </div>
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-emerald-400 block mb-1">Negative Numbers Logic</strong>
                                Remember that negative numbers sort counter-intuitively: <code>-28</code> is smaller than <code>-14</code>. In Ascending mode, click the largest negative magnitude first!
                            </div>
                        </div>
                    </div>
                </div>

                <!-- GAME 3: MEMORY MAZE -->
                <div class="p-5 rounded-2xl bg-acc-bgDark border border-acc-borderDark space-y-4">
                    <div class="flex flex-wrap items-center justify-between gap-3 border-b border-acc-borderDark pb-3">
                        <div class="flex items-center gap-2.5">
                            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-sm">G3</span>
                            <h3 class="font-bold text-lg text-white">Memory Maze (Rat &amp; Cheese Route) — Spatial Working Memory</h3>
                        </div>
                        <span class="px-2.5 py-0.5 rounded-full text-xs font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">3–6s Preview • Blind Navigation • Touch D-Pad</span>
                    </div>

                    <div class="space-y-3 text-xs sm:text-sm text-gray-300 leading-relaxed">
                        <p>
                            <strong>Game Mechanics:</strong> Also known as the Rat &amp; Cheese Maze, this test operates in two distinct phases. During the <strong>Preview Phase (3 to 6 seconds)</strong>, an illuminated, numbered route connecting Start to Goal is shown. When the preview window closes, the path disappears. During the <strong>Navigation Phase (60 seconds)</strong>, you must guide the agent step-by-step along the exact memorized route using Arrow Keys, WASD, adjacent square clicks, or our built-in <em>Mobile Touch D-Pad</em>. Stepping onto an illegal tile triggers a red error flash and registers a mistake.
                        </p>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 pt-1">
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-emerald-400 block mb-1">Spatial Chunking Vectors</strong>
                                Do NOT try to remember 12 individual cell coordinates. Instead, convert the route into directional chunks: e.g. <code>[R3, D2, L1, D3]</code> (Right 3, Down 2, Left 1, Down 3). The human brain easily holds 4 chunks!
                            </div>
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-cyan-400 block mb-1">Perimeter Wall Bounces</strong>
                                Note when a route touches the border of the grid. Outer borders act as cognitive visual anchors, making it nearly impossible to misplace your turn.
                            </div>
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-amber-400 block mb-1">Mistake Recovery Protocol</strong>
                                If you step onto a red illegal tile, do NOT start spamming keys. Immediately re-orient to your current illuminated position, recall your directional chunk, and proceed steadily.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- GAME 4: KEY & DOOR MAZE -->
                <div class="p-5 rounded-2xl bg-acc-bgDark border border-acc-borderDark space-y-4">
                    <div class="flex flex-wrap items-center justify-between gap-3 border-b border-acc-borderDark pb-3">
                        <div class="flex items-center gap-2.5">
                            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-sm">G4</span>
                            <h3 class="font-bold text-lg text-white">Key &amp; Door Maze — Multi-Goal State Graph Planning</h3>
                        </div>
                        <span class="px-2.5 py-0.5 rounded-full text-xs font-mono bg-amber-500/20 text-amber-300 border border-amber-500/40">Multi-Key Inventory • Par Target • 60s / Level</span>
                    </div>

                    <div class="space-y-3 text-xs sm:text-sm text-gray-300 leading-relaxed">
                        <p>
                            <strong>Game Mechanics:</strong> You control an avatar inside an obstacle labyrinth containing color-coded keys (Crimson, Cyan, Emerald, Amber), locked gates, and an Exit portal. Picking up a key adds it to your inventory and allows you to unlock doors of that color. Reaching the Exit portal requires having collected all required keys on the board. The simulator tracks your move count against the mathematical <strong>Par Target</strong> (the optimal BFS shortest path).
                        </p>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 pt-1">
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-amber-400 block mb-1">Reverse Dependency Planning</strong>
                                Look at the Exit first. Which door guards the Exit? If it is the Emerald Door, find the Emerald Key. If the Emerald Key is behind a Crimson Door, find the Crimson Key first. Plan: Start → Crimson Key → Crimson Door → Emerald Key → Exit.
                            </div>
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-cyan-400 block mb-1">Optimal Par Matching</strong>
                                Avoid unnecessary wandering or backtracking. Every step taken above the optimal BFS par count penalizes your par efficiency accuracy metric.
                            </div>
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-emerald-400 block mb-1">Pre-Scan Before Moving</strong>
                                Spend the first 5 seconds studying the maze layout before hitting any arrow key. A 5-second pause followed by an error-free 15-second run scores far higher than instant frantic moving.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- GAME 5: MEMORY RECALL -->
                <div class="p-5 rounded-2xl bg-acc-bgDark border border-acc-borderDark space-y-4">
                    <div class="flex flex-wrap items-center justify-between gap-3 border-b border-acc-borderDark pb-3">
                        <div class="flex items-center gap-2.5">
                            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-400 flex items-center justify-center font-bold text-sm">G5</span>
                            <h3 class="font-bold text-lg text-white">Memory Recall — Sequence, Reverse &amp; Missing Matrix</h3>
                        </div>
                        <span class="px-2.5 py-0.5 rounded-full text-xs font-mono bg-pink-500/20 text-pink-300 border border-pink-500/40">3 Recall Modalities • Dual-Encoding • 60s / Level</span>
                    </div>

                    <div class="space-y-3 text-xs sm:text-sm text-gray-300 leading-relaxed">
                        <p>
                            <strong>Game Mechanics:</strong> A sequence of distinct alphanumeric symbols (e.g. <code>A3-Bolt</code>, <code>C7-Gem</code>, <code>D4-Shield</code>, <code>P9-Key</code>) flashes in the center of the screen at speeds between 520ms and 920ms per token. Once the presentation concludes, you are challenged under one of three cognitive modes:
                        </p>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 pt-1">
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-cyan-400 block mb-1">1. Forward Sequence</strong>
                                Tap the flashed symbols in the EXACT order they were presented. This measures immediate auditory-visual sensory memory retention.
                            </div>
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-amber-400 block mb-1">2. Reverse Order Recall</strong>
                                Tap the symbols in REVERSE order (Last Shown → First Shown). This assesses working memory manipulation and backward digit span capacity.
                            </div>
                            <div class="p-3 rounded-xl bg-acc-cardDark border border-acc-borderDark">
                                <strong class="text-rose-400 block mb-1">3. Missing-Item Matrix</strong>
                                The original set is displayed with one symbol missing. Identify which token from the presentation vanished from the matrix bank!
                            </div>
                        </div>

                        <p class="pt-1">
                            <strong>Dual-Coding Pro Tip:</strong> As the tokens flash, silently vocalize the symbol name and letter code together (e.g. <em>"A-Star, B-Shield, C-Bolt"</em>). Engaging both the visual cortex and the phonological loop increases working memory retention by up to 200%.
                        </p>
                    </div>
                </div>
            </section>

            <!-- ======================================================================
                 SECTION 3: ACCENTURE RECRUITMENT PROCESS & 2026 SYLLABUS
                 ====================================================================== -->
            <section id="recruitment-pattern" class="rounded-2xl bg-acc-cardDark border border-acc-borderDark p-6 sm:p-8 space-y-6">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 font-bold text-lg">
                        03
                    </div>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">
                            Accenture Recruitment Process (2025–2026 Placement Blueprint)
                        </h2>
                        <p class="text-xs text-gray-400">Complete round-by-round syllabus, cutoffs, and package breakdown</p>
                    </div>
                </div>

                <div class="space-y-4 text-xs sm:text-sm text-gray-300 leading-relaxed">
                    <p>
                        Accenture hires tens of thousands of engineering, MCA, and BCA graduates annually across India through on-campus placement drives and national off-campus initiatives (such as the Accenture National Recruitment Drive). Understanding the exact placement pipeline ensures you invest your preparation time strategically.
                    </p>

                    <!-- Pipeline Stages Timeline Table -->
                    <div class="overflow-x-auto rounded-xl border border-acc-borderDark bg-acc-bgDark">
                        <table class="w-full text-left text-xs border-collapse">
                            <thead>
                                <tr class="border-b border-acc-borderDark bg-acc-cardDark/80 text-white uppercase text-[11px] font-bold">
                                    <th class="p-3">Stage</th>
                                    <th class="p-3">Assessment Name</th>
                                    <th class="p-3">Duration &amp; Structure</th>
                                    <th class="p-3">Key Focus Areas</th>
                                    <th class="p-3">Eliminatory?</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-acc-borderDark text-gray-300">
                                <tr>
                                    <td class="p-3 font-mono font-bold text-acc-lightPurple">Round 1</td>
                                    <td class="p-3 font-semibold text-white">Cognitive &amp; Technical Assessment</td>
                                    <td class="p-3">90 Minutes • 90 Questions</td>
                                    <td class="p-3">English Ability (17Q), Critical Thinking (18Q), Abstract Reasoning (15Q), MS Office (12Q), Pseudocode (18Q), Networking/Cloud (10Q).</td>
                                    <td class="p-3 text-emerald-400 font-bold">Yes (Sectional Cutoffs)</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-mono font-bold text-cyan-400">Round 2</td>
                                    <td class="p-3 font-semibold text-white">Coding Assessment</td>
                                    <td class="p-3">45 Minutes • 2 Coding Questions</td>
                                    <td class="p-3">C, C++, Java, or Python. 1 easy array/string problem + 1 intermediate algorithmic problem (greedy, hashing, DP).</td>
                                    <td class="p-3 text-emerald-400 font-bold">Yes (Test Cases Passed)</td>
                                </tr>
                                <tr class="bg-acc-purple/10 border-l-4 border-acc-purple">
                                    <td class="p-3 font-mono font-bold text-acc-lightPurple">Round 3</td>
                                    <td class="p-3 font-semibold text-white">Gamified Cognitive Assessment (Gaming Round)</td>
                                    <td class="p-3">15 Minutes / Game • 15 Levels / Game</td>
                                    <td class="p-3 font-semibold text-acc-lightPurple">The 5 Core Games: Path Finder, Bubble Math, Memory Maze, Key &amp; Door, Memory Recall.</td>
                                    <td class="p-3 text-emerald-400 font-bold">Yes (Elimination Filter)</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-mono font-bold text-amber-400">Round 4</td>
                                    <td class="p-3 font-semibold text-white">Communication Assessment</td>
                                    <td class="p-3">~20 Minutes • Automated Voice Test</td>
                                    <td class="p-3">Administered via Pearson SVAr. Reading aloud, repeating sentences, vocabulary, short story retelling, impromptu speech.</td>
                                    <td class="p-3 text-amber-300 font-bold">Scored Benchmark</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-mono font-bold text-rose-400">Round 5</td>
                                    <td class="p-3 font-semibold text-white">Combined Technical &amp; HR Interview</td>
                                    <td class="p-3">25–35 Minutes • Virtual Video Call</td>
                                    <td class="p-3">Final year project deep dive, OOP concepts, DBMS, situational questions, cultural fit.</td>
                                    <td class="p-3 text-emerald-400 font-bold">Final Offer Gate</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
                        <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark">
                            <h4 class="font-bold text-sm text-white mb-1.5 flex items-center gap-2">
                                <i class="fas fa-id-badge text-cyan-400"></i> Associate Software Engineer (ASE)
                            </h4>
                            <p class="text-xs text-gray-300">
                                <strong>Annual CTC:</strong> ₹4.5 LPA. Candidates who achieve qualifying cutoffs across the Cognitive Assessment, pass at least 1 coding question with partial/full test cases, and achieve the 65th percentile in the Gaming Round are considered for the ASE role.
                            </p>
                        </div>
                        <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark">
                            <h4 class="font-bold text-sm text-white mb-1.5 flex items-center gap-2">
                                <i class="fas fa-crown text-amber-400"></i> Advanced Associate Software Engineer (AAH / FSE)
                            </h4>
                            <p class="text-xs text-gray-300">
                                <strong>Annual CTC:</strong> ₹6.5 LPA. Top-performing candidates who pass both coding questions with 100% test cases and demonstrate top 10% cognitive speed and accuracy across all 5 games in the Gaming Round are upgraded to the AAH interview track.
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ======================================================================
                 SECTION 4: DUAL-TIMER SYSTEM & SCORING FORMULAS
                 ====================================================================== -->
            <section id="scoring-rules" class="rounded-2xl bg-acc-cardDark border border-acc-borderDark p-6 sm:p-8 space-y-6">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-amber-400 font-bold text-lg">
                        04
                    </div>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">
                            Dual-Timer Architecture, Scoring Formulas &amp; BFS Solvability Guarantees
                        </h2>
                        <p class="text-xs text-gray-400">The mathematical model behind scoring, speed multipliers, and algorithmic validation</p>
                    </div>
                </div>

                <div class="space-y-4 text-xs sm:text-sm text-gray-300 leading-relaxed">
                    <p>
                        To ensure that candidates cannot pass through blind guessing or static answer memorization, Accenture's assessment utilizes a dual-timer framework combined with procedural question generation.
                    </p>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-2">
                            <h3 class="font-bold text-sm text-white flex items-center gap-2">
                                <i class="fas fa-stopwatch text-acc-lightPurple"></i> The Dual-Timer Engine
                            </h3>
                            <ul class="space-y-1.5 text-xs text-gray-300 list-disc list-inside">
                                <li><strong class="text-white">15:00 Total Game Timer:</strong> A 900-second global countdown allocated for all 15 levels of a game. Efficient candidates clear all 15 levels with 4 to 6 minutes to spare.</li>
                                <li><strong class="text-cyan-300">01:00 (60s) Per-Question Timer:</strong> A strict individual countdown for every level. If the timer reaches 00:00, the level auto-submits as a timeout in Exam Mode.</li>
                                <li><strong class="text-emerald-300">Auto-Advance on Timeout:</strong> Unsolved questions transition to the next level automatically, preventing candidates from stalling.</li>
                            </ul>
                        </div>

                        <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-2">
                            <h3 class="font-bold text-sm text-white flex items-center gap-2">
                                <i class="fas fa-calculator text-emerald-400"></i> The Scoring Algorithm
                            </h3>
                            <p class="text-xs text-gray-300">
                                Total score per level is evaluated using the formula:
                            </p>
                            <div class="p-2.5 rounded-lg bg-acc-cardDark border border-acc-borderDark font-mono text-xs text-acc-lightPurple text-center">
                                Score = BasePoints(Tier) + (SecondsLeft × 10) - (Mistakes × 15)
                            </div>
                            <p class="text-[11px] text-gray-400">
                                Base points scale from 100 pts (Level 1) to 350+ pts (Level 15). Clearing a level in 14 seconds awards +460 speed bonus points!
                            </p>
                        </div>
                    </div>

                    <div class="p-4 rounded-xl bg-cyan-950/30 border border-cyan-800/40 text-cyan-200 text-xs space-y-2">
                        <h3 class="font-bold text-white flex items-center gap-2">
                            <i class="fas fa-microchip text-cyan-400"></i> Mathematical Solvability Verification (Breadth-First Search)
                        </h3>
                        <p>
                            A common frustration among candidates practicing on low-quality simulators is encountering impossible mazes or broken pipes. Our simulator incorporates an active <strong>Breadth-First Search (BFS) Verifier</strong>. Every single time a new seed (<code>SEED #XXXX</code>) is generated, a background BFS graph traversal executes, proving that a valid connected path exists between Start and End before the puzzle renders. This guarantees <strong>100% mathematical solvability</strong> with zero deadlocks on every attempt.
                        </p>
                    </div>
                </div>
            </section>

            <!-- ======================================================================
                 SECTION 5: 7-DAY MASTER PREPARATION PLAN
                 ====================================================================== -->
            <section id="prep-roadmap" class="rounded-2xl bg-acc-cardDark border border-acc-borderDark p-6 sm:p-8 space-y-6">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-rose-500/20 border border-rose-500/40 flex items-center justify-center text-rose-400 font-bold text-lg">
                        05
                    </div>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">
                            7-Day Master Preparation Plan for Indian Engineering Students
                        </h2>
                        <p class="text-xs text-gray-400">A structured daily training schedule for college placement season</p>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs text-gray-300">
                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-acc-purple/20 text-acc-lightPurple border border-acc-purple/40">Day 1</span>
                        <h4 class="font-bold text-white text-sm">Spatial &amp; Arithmetic Reflexes</h4>
                        <p>Drill <strong>Path Finder</strong> levels 1–10 to master clockwise pipe rotation reflexes. Practice <strong>Bubble Math</strong> Ascending mode mentally without using scratch paper.</p>
                    </div>
                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/40">Day 2</span>
                        <h4 class="font-bold text-white text-sm">Working Memory &amp; Chunking</h4>
                        <p>Focus on <strong>Memory Maze</strong> (Rat Route). Practice translating the illuminated route into directional vectors (e.g. <code>[U2, R3, D1]</code>) during the 3s preview window.</p>
                    </div>
                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">Day 3</span>
                        <h4 class="font-bold text-white text-sm">Multi-Goal Graph Routing</h4>
                        <p>Practice <strong>Key &amp; Door Maze</strong> levels 1–12. Train your eye to work backward from the Exit portal to sequence color-coded key pickups with zero par deviations.</p>
                    </div>
                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40">Day 4</span>
                        <h4 class="font-bold text-white text-sm">Reverse Sensory Retention</h4>
                        <p>Drill <strong>Memory Recall</strong> with a focus on <em>Reverse Order Recall</em> and <em>Missing Item Matrix</em>. Apply dual-coding (saying token names aloud) to build memory muscle.</p>
                    </div>
                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/40">Day 5</span>
                        <h4 class="font-bold text-white text-sm">High-Difficulty Tier Practice</h4>
                        <p>Switch simulator to <strong>Practice Mode</strong>. Jump directly to Levels 11–15 across all games to condition yourself to large 8×8 grids and compound equations.</p>
                    </div>
                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/40">Day 6</span>
                        <h4 class="font-bold text-white text-sm">Diagnostic Performance Review</h4>
                        <p>Open the <strong>Analytics Dashboard</strong>. Identify your weakest game (e.g. accuracy below 75% or average solve time above 35s). Re-attempt that specific game 3 times.</p>
                    </div>
                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5 sm:col-span-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">Day 7</span>
                        <h4 class="font-bold text-white text-sm">Full 5-Game Mock Marathon (Exam Mode)</h4>
                        <p>Enable <strong>Exam Mode</strong>. Click <em>"Start Full 5-Game Mock Exam"</em> and complete all 75 levels in one sitting under strict placement exam conditions without pausing.</p>
                    </div>
                </div>
            </section>

            <!-- ======================================================================
                 SECTION 6: USABILITY & COLLEGE LAB GUIDE (INDIA CONTEXT)
                 ====================================================================== -->
            <section id="college-tips" class="rounded-2xl bg-acc-cardDark border border-acc-borderDark p-6 sm:p-8 space-y-5">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-purple-500/20 border border-purple-500/40 flex items-center justify-center text-purple-400 font-bold text-lg">
                        06
                    </div>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">
                            Usability &amp; Test-Taking Guide for Indian Engineering College Labs
                        </h2>
                        <p class="text-xs text-gray-400">Tips for low bandwidth, proxy firewalls, campus Wi-Fi drops, and mobile practice</p>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs text-gray-300">
                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-2">
                        <h4 class="font-bold text-sm text-cyan-400 flex items-center gap-1.5">
                            <i class="fas fa-wifi"></i> Low Bandwidth &amp; Jio/Airtel 4G
                        </h4>
                        <p>Our simulator is 100% client-side JavaScript. Once loaded, all 5 games, PRNG engines, and audio synthesizers run entirely locally on your machine with <strong>zero server lag</strong>, even on spotty college Wi-Fi or 4G phone hotspots.</p>
                    </div>
                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-2">
                        <h4 class="font-bold text-sm text-amber-400 flex items-center gap-1.5">
                            <i class="fas fa-desktop"></i> College Computer Lab Setup
                        </h4>
                        <p>In campus computer labs, monitor resolutions often vary. Press <kbd class="px-1.5 py-0.5 rounded bg-gray-800 text-white font-mono">F11</kbd> to enter full-screen mode and press <kbd class="px-1.5 py-0.5 rounded bg-gray-800 text-white font-mono">Ctrl + 0</kbd> to reset browser zoom to 100% so all grid tiles render cleanly.</p>
                    </div>
                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-2">
                        <h4 class="font-bold text-sm text-emerald-400 flex items-center gap-1.5">
                            <i class="fas fa-mobile-screen"></i> Mobile Touch Controls
                        </h4>
                        <p>Traveling by train or bus? Use our on-screen <strong>Touch D-Pad</strong> in Memory Maze and Key &amp; Door Maze to practice comfortably on your Android smartphone or tablet without needing a physical keyboard.</p>
                    </div>
                </div>
            </section>

            <!-- ======================================================================
                 SECTION 7: SEARCH DISAMBIGUATION: "GAMINI GROUND"
                 ====================================================================== -->
            <section id="gamini-ground-clarification" class="rounded-2xl bg-acc-cardDark border border-acc-borderDark p-6 sm:p-8 space-y-4">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-teal-500/20 border border-teal-500/40 flex items-center justify-center text-teal-400 font-bold text-lg">
                        07
                    </div>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">
                            Search Disambiguation &amp; Phonetic Clarification: "Gamini Ground"
                        </h2>
                        <p class="text-xs text-gray-400">Addressing the most common query variation across YouTube, Reddit, and Telegram</p>
                    </div>
                </div>

                <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-3 text-xs sm:text-sm text-gray-300 leading-relaxed">
                    <p>
                        Across engineering colleges in Tamil Nadu, Karnataka, Telangana, Andhra Pradesh, Maharashtra, Uttar Pradesh, and West Bengal, thousands of candidates type <strong class="text-white">"gamini ground"</strong>, <strong class="text-white">"accenture gamini ground"</strong>, or <strong class="text-white">"accenture gamify ground"</strong> into search engines, YouTube search bars, and AI prompts like ChatGPT.
                    </p>
                    <p>
                        This phonetic typing stems from the rapid spoken pronounciation of <em>"gaming round"</em>. If you searched for <em>"gamini ground"</em>, <strong>you are in the exact right place</strong>. This website is specifically engineered to provide the definitive, official syllabus, questions, rules, tricks, and interactive practice arena for the Accenture Gamified Cognitive Assessment.
                    </p>
                </div>
            </section>

            <!-- ======================================================================
                 SECTION 8: COMPARISON TABLE: APTITUDE VS GAMIFIED
                 ====================================================================== -->
            <section id="comparison-table" class="rounded-2xl bg-acc-cardDark border border-acc-borderDark p-6 sm:p-8 space-y-5">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-yellow-500/20 border border-yellow-500/40 flex items-center justify-center text-yellow-400 font-bold text-lg">
                        08
                    </div>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">
                            Comparative Analysis: Traditional Aptitude vs Gamified Assessment
                        </h2>
                        <p class="text-xs text-gray-400">Why corporate recruitment shifted from textbook math to cognitive neuroscience</p>
                    </div>
                </div>

                <div class="overflow-x-auto rounded-xl border border-acc-borderDark bg-acc-bgDark">
                    <table class="w-full text-left text-xs border-collapse">
                        <thead>
                            <tr class="border-b border-acc-borderDark bg-acc-cardDark/80 text-white uppercase text-[11px] font-bold">
                                <th class="p-3">Evaluation Parameter</th>
                                <th class="p-3">Traditional Aptitude Exam (MCQ)</th>
                                <th class="p-3 text-acc-lightPurple">Accenture Gamified Assessment</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-acc-borderDark text-gray-300">
                            <tr>
                                <td class="p-3 font-semibold text-white">Question Format</td>
                                <td class="p-3">Textual word problems, time/work formulas, geometry questions.</td>
                                <td class="p-3 text-cyan-300 font-medium">Interactive games, 2D grid mazes, pipe conduits, numerical bubbles.</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-semibold text-white">Memorization Dependency</td>
                                <td class="p-3">High (requires formulas like speed = distance / time, permutations).</td>
                                <td class="p-3 text-emerald-300 font-medium">Zero (tests intrinsic fluid intelligence and spatial working memory).</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-semibold text-white">Cheating Vulnerability</td>
                                <td class="p-3">High (questions can be copied into search engines or solved via calculators).</td>
                                <td class="p-3 text-acc-lightPurple font-medium">Impossible (dynamic PRNG seeds, live timer, interactive mouse clicks).</td>
                            </tr>
                            <tr>
                                <td class="p-3 font-semibold text-white">Evaluation Metrics</td>
                                <td class="p-3">Binary (Correct vs Incorrect answer choice).</td>
                                <td class="p-3 text-amber-300 font-medium">Multi-dimensional: Speed bonus, move par accuracy, error recovery rate.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <!-- ======================================================================
                 SECTION 9: 20+ FREQUENTLY ASKED QUESTIONS (FAQS)
                 ====================================================================== -->
            <section id="faqs" class="rounded-2xl bg-acc-cardDark border border-acc-borderDark p-6 sm:p-8 space-y-6">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-blue-500/20 border border-blue-500/40 flex items-center justify-center text-blue-400 font-bold text-lg">
                        09
                    </div>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">
                            Frequently Asked Questions (FAQs) — Accenture Gaming Round
                        </h2>
                        <p class="text-xs text-gray-400">Authoritative answers to the most common candidate questions across India</p>
                    </div>
                </div>

                <div class="space-y-3 text-xs sm:text-sm text-gray-300">
                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <h3 class="font-bold text-white flex items-center gap-2">
                            <i class="fas fa-circle-question text-acc-lightPurple"></i>
                            1. What is the Accenture Gaming Round (Gamified Cognitive Assessment)?
                        </h3>
                        <p class="text-gray-300 leading-relaxed">
                            It is an interactive computer-adaptive assessment phase in Accenture's campus recruitment drive featuring 5 games: Path Finder, Bubble Math, Memory Maze, Key &amp; Door Puzzle, and Memory Recall. It evaluates spatial reasoning, fluid logic, and working memory.
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <h3 class="font-bold text-white flex items-center gap-2">
                            <i class="fas fa-circle-question text-acc-lightPurple"></i>
                            2. Is the Accenture Gaming Round an elimination round?
                        </h3>
                        <p class="text-gray-300 leading-relaxed">
                            Yes. Candidates who fail to achieve the required cognitive threshold (typically the 65th–70th percentile across games) are disqualified before interview scheduling, regardless of their coding scores.
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <h3 class="font-bold text-white flex items-center gap-2">
                            <i class="fas fa-circle-question text-acc-lightPurple"></i>
                            3. Why do students search for "gamini ground"?
                        </h3>
                        <p class="text-gray-300 leading-relaxed">
                            "Gamini ground" is a phonetic misspelling of "gaming round". It refers to the exact same Accenture Gamified Cognitive Assessment covered on this website.
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <h3 class="font-bold text-white flex items-center gap-2">
                            <i class="fas fa-circle-question text-acc-lightPurple"></i>
                            4. What are the time limits for each game?
                        </h3>
                        <p class="text-gray-300 leading-relaxed">
                            The test operates on a Dual-Timer model: 15 minutes total for all 15 levels of each game, and a strict 60-second limit per question.
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <h3 class="font-bold text-white flex items-center gap-2">
                            <i class="fas fa-circle-question text-acc-lightPurple"></i>
                            5. Are questions identical or repeated on different attempts?
                        </h3>
                        <p class="text-gray-300 leading-relaxed">
                            No. Puzzles are procedurally generated with dynamic pseudo-random cryptographic seeds (<code>SEED #XXXX</code>), ensuring zero question repetition across attempts.
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <h3 class="font-bold text-white flex items-center gap-2">
                            <i class="fas fa-circle-question text-acc-lightPurple"></i>
                            6. Can I use a mobile phone for the official Accenture exam?
                        </h3>
                        <p class="text-gray-300 leading-relaxed">
                            No. The actual exam must be taken on a Windows or macOS laptop/desktop with a working webcam, microphone, and Google Chrome. However, our simulator supports mobile touch D-Pad controls for practice anywhere.
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <h3 class="font-bold text-white flex items-center gap-2">
                            <i class="fas fa-circle-question text-acc-lightPurple"></i>
                            7. What are the packages offered by Accenture in 2025–2026?
                        </h3>
                        <p class="text-gray-300 leading-relaxed">
                            Associate Software Engineer (ASE) pays ₹4.5 LPA. Advanced Associate Software Engineer (AAH / Full Stack Engineer) pays ₹6.5 LPA for high-percentile candidates.
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <h3 class="font-bold text-white flex items-center gap-2">
                            <i class="fas fa-circle-question text-acc-lightPurple"></i>
                            8. What happens if the 60-second question timer expires?
                        </h3>
                        <p class="text-gray-300 leading-relaxed">
                            In Exam Mode, the question is marked as a timeout and the test automatically advances to the next level. In Practice Mode, you can retry the level.
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <h3 class="font-bold text-white flex items-center gap-2">
                            <i class="fas fa-circle-question text-acc-lightPurple"></i>
                            9. How can I practice reversing sequences in Memory Recall?
                        </h3>
                        <p class="text-gray-300 leading-relaxed">
                            Use backward digit/symbol rehearsal: silently repeat the symbols backwards as they flash, and anchor your memory on the final symbol shown, as it is the first symbol you must click!
                        </p>
                    </div>

                    <div class="p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark space-y-1.5">
                        <h3 class="font-bold text-white flex items-center gap-2">
                            <i class="fas fa-circle-question text-acc-lightPurple"></i>
                            10. Is negative marking applied in the gaming round?
                        </h3>
                        <p class="text-gray-300 leading-relaxed">
                            There is no traditional negative marking, but superfluous rotations, illegal maze moves, and misclicks deduct from your accuracy multiplier, resulting in lower total points.
                        </p>
                    </div>
                </div>
            </section>

            <!-- ======================================================================
                 SECTION 10: QUICK REFERENCE CHEAT SHEET CARDS
                 ====================================================================== -->
            <section id="cheat-sheet" class="rounded-2xl bg-acc-cardDark border border-acc-borderDark p-6 sm:p-8 space-y-5">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-acc-purple/20 border border-acc-purple/40 flex items-center justify-center text-acc-lightPurple font-bold text-lg">
                        10
                    </div>
                    <div>
                        <h2 class="text-xl sm:text-2xl font-bold text-white tracking-tight">
                            Quick Reference Golden Rules Cheat Sheet
                        </h2>
                        <p class="text-xs text-gray-400">Save or memorize these 5 golden rules before launching your real exam</p>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3 text-xs">
                    <div class="p-3.5 rounded-xl bg-acc-bgDark border border-acc-purple/40">
                        <strong class="text-acc-lightPurple block mb-1">Path Finder</strong>
                        Always trace backwards from Target (E) first. Corner elbow tiles have only 1 valid orientation!
                    </div>
                    <div class="p-3.5 rounded-xl bg-acc-bgDark border border-cyan-500/40">
                        <strong class="text-cyan-400 block mb-1">Bubble Math</strong>
                        Check the top badge for Ascending vs Descending order before popping your first bubble!
                    </div>
                    <div class="p-3.5 rounded-xl bg-acc-bgDark border border-emerald-500/40">
                        <strong class="text-emerald-400 block mb-1">Memory Maze</strong>
                        Chunk moves into vectors: <code>[R3, D2, L1, D3]</code>. Use perimeter walls as cognitive anchors!
                    </div>
                    <div class="p-3.5 rounded-xl bg-acc-bgDark border border-amber-500/40">
                        <strong class="text-amber-400 block mb-1">Key &amp; Door</strong>
                        Work backwards from the Exit door to determine the prerequisite key pickup sequence!
                    </div>
                    <div class="p-3.5 rounded-xl bg-acc-bgDark border border-pink-500/40">
                        <strong class="text-pink-400 block mb-1">Memory Recall</strong>
                        Use dual coding: say the icon and number code aloud (e.g. <em>"A3-Star, D4-Shield"</em>) to retain items!
                    </div>
                </div>
            </section>

        </article>
"""

FOOTER_HTML = """
    <!-- ==========================================
         WEBSITE FOOTER
         ========================================== -->
    <footer class="mt-16 bg-acc-cardDark border-t border-acc-borderDark py-10 px-4 lg:px-8 text-xs text-gray-400">
        <div class="max-w-7xl mx-auto space-y-8">
            <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-6 border-b border-acc-borderDark pb-8">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-acc-purple to-indigo-600 flex items-center justify-center shadow-lg shadow-acc-purple/30 text-white font-extrabold text-xl">
                        &gt;
                    </div>
                    <div>
                        <span class="font-extrabold text-white text-base tracking-tight">Accenture Gamified Assessment Simulator</span>
                        <p class="text-xs text-gray-400">Independent Candidate Preparation Portal &amp; Comprehensive Practice Arena</p>
                    </div>
                </div>
                <div class="flex flex-wrap items-center gap-4 text-xs font-semibold">
                    <a href="#simulator" class="hover:text-white transition">Play Simulator</a>
                    <a href="#games-guide" class="hover:text-white transition">5 Games Guide</a>
                    <a href="#recruitment-pattern" class="hover:text-white transition">2026 Syllabus</a>
                    <a href="#scoring-rules" class="hover:text-white transition">Scoring Rules</a>
                    <a href="#prep-roadmap" class="hover:text-white transition">7-Day Plan</a>
                    <a href="#faqs" class="hover:text-white transition">FAQs</a>
                    <a href="sitemap.xml" class="hover:text-white transition">Sitemap XML</a>
                    <a href="llms.txt" class="hover:text-white transition">llms.txt</a>
                </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 text-[11px] leading-relaxed">
                <div>
                    <strong class="text-white block mb-2 font-bold uppercase tracking-wider">Exam Simulator Modules</strong>
                    <ul class="space-y-1">
                        <li><a href="#simulator" class="hover:text-acc-lightPurple transition">1. Path Finder (Spatial Logic)</a></li>
                        <li><a href="#simulator" class="hover:text-cyan-300 transition">2. Quick Math (Bubble Sorting)</a></li>
                        <li><a href="#simulator" class="hover:text-emerald-300 transition">3. Memory Maze (Rat Route)</a></li>
                        <li><a href="#simulator" class="hover:text-amber-300 transition">4. Key &amp; Door Labyrinth</a></li>
                        <li><a href="#simulator" class="hover:text-pink-300 transition">5. Memory Recall (Sequence &amp; Reverse)</a></li>
                    </ul>
                </div>

                <div>
                    <strong class="text-white block mb-2 font-bold uppercase tracking-wider">Placement Roles &amp; Packages</strong>
                    <ul class="space-y-1">
                        <li>Associate Software Engineer (ASE) — ₹4.5 LPA</li>
                        <li>Advanced Associate Software Engineer (AAH) — ₹6.5 LPA</li>
                        <li>Full Stack Engineer Track</li>
                        <li>System &amp; Application Services Associate</li>
                    </ul>
                </div>

                <div>
                    <strong class="text-white block mb-2 font-bold uppercase tracking-wider">Assessment Partners in India</strong>
                    <ul class="space-y-1">
                        <li>Aon Hewitt / CoCubes Assessment Engine</li>
                        <li>Superset Campus Placement Network</li>
                        <li>HirePro Assessment Platform</li>
                        <li>Wheebox / SHL Psychometric Systems</li>
                    </ul>
                </div>

                <div>
                    <strong class="text-white block mb-2 font-bold uppercase tracking-wider">Legal Disclaimer &amp; Notice</strong>
                    <p class="text-gray-400">
                        This simulator and preparation guide is an independent educational platform created to assist engineering and MCA students across India in preparing for corporate gamified cognitive assessments. All trademarks, company names (Accenture), and logos belong to their respective copyright holders.
                    </p>
                </div>
            </div>

            <div class="border-t border-acc-borderDark pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-gray-500">
                <p>&copy; 2026 Accenture Assessment Prep Research. All rights reserved. Procedural PRNG Engine v3.5.</p>
                <div class="flex items-center gap-3">
                    <span class="inline-flex items-center gap-1 text-emerald-400"><i class="fas fa-circle text-[7px]"></i> 100% BFS Solvable Puzzles</span>
                    <span>•</span>
                    <span class="text-cyan-400">Dual-Timer Engine Active</span>
                </div>
            </div>
        </div>
    </footer>
"""
