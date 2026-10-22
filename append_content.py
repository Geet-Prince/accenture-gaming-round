# append_content.py
# Writes the rich guide and content sections to site_content.py

import sys

content = '''
NAVBAR_HTML = """
    <!-- TOP NAVIGATION BAR -->
    <header class="sticky top-0 z-40 bg-acc-cardDark/95 backdrop-blur-md border-b border-acc-borderDark px-4 lg:px-8 py-2.5">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <!-- Brand Logo -->
            <div class="flex items-center gap-3 cursor-pointer" onclick="app.showDashboard()">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-acc-purple to-indigo-600 flex items-center justify-center shadow-lg shadow-acc-purple/30 shrink-0">
                    <span class="text-white font-extrabold text-xl tracking-tighter">&gt;</span>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="font-black text-lg tracking-tight text-white">ACCENTURE</span>
                        <span class="text-[10px] font-bold uppercase px-2 py-0.5 rounded-full bg-acc-purple/20 text-acc-lightPurple border border-acc-purple/40">Simulator &amp; Guide v3.5</span>
                    </div>
                    <p class="text-[11px] text-gray-400 hidden sm:block">Gamified Cognitive Assessment • 15-Min Round • 01:00 / Question • India Drives</p>
                </div>
            </div>

            <!-- Quick In-Page Anchor Navigation Links for Fast User Browsing & SEO Indexing -->
            <nav class="hidden lg:flex items-center gap-1.5 text-xs font-semibold text-gray-300">
                <a href="#simulator" class="px-2.5 py-1.5 rounded-lg hover:bg-acc-bgDark hover:text-white transition flex items-center gap-1.5">
                    <i class="fas fa-gamepad text-acc-lightPurple"></i>
                    <span>Simulator</span>
                </a>
                <a href="#games-guide" class="px-2.5 py-1.5 rounded-lg hover:bg-acc-bgDark hover:text-white transition flex items-center gap-1.5">
                    <i class="fas fa-book-open text-cyan-400"></i>
                    <span>5 Games Guide</span>
                </a>
                <a href="#recruitment-pattern" class="px-2.5 py-1.5 rounded-lg hover:bg-acc-bgDark hover:text-white transition flex items-center gap-1.5">
                    <i class="fas fa-sitemap text-emerald-400"></i>
                    <span>2026 Pattern</span>
                </a>
                <a href="#scoring-rules" class="px-2.5 py-1.5 rounded-lg hover:bg-acc-bgDark hover:text-white transition flex items-center gap-1.5">
                    <i class="fas fa-stopwatch text-amber-400"></i>
                    <span>Scoring &amp; Timers</span>
                </a>
                <a href="#prep-roadmap" class="px-2.5 py-1.5 rounded-lg hover:bg-acc-bgDark hover:text-white transition flex items-center gap-1.5">
                    <i class="fas fa-calendar-check text-rose-400"></i>
                    <span>7-Day Plan</span>
                </a>
                <a href="#faqs" class="px-2.5 py-1.5 rounded-lg hover:bg-acc-bgDark hover:text-white transition flex items-center gap-1.5">
                    <i class="fas fa-circle-question text-purple-400"></i>
                    <span>FAQs</span>
                </a>
            </nav>

            <!-- Mode Switcher & Global Stats -->
            <div class="flex flex-wrap items-center gap-2.5">
                <!-- Mode Switch Pill -->
                <div class="flex items-center bg-acc-bgDark p-1 rounded-xl border border-acc-borderDark text-xs">
                    <button id="mode-btn-exam" onclick="app.setMode('EXAM')" class="px-3 py-1.5 rounded-lg font-bold transition flex items-center gap-1.5 bg-acc-purple text-white shadow">
                        <i class="fas fa-shield-halved"></i>
                        <span>Exam Mode</span>
                    </button>
                    <button id="mode-btn-practice" onclick="app.setMode('PRACTICE')" class="px-3 py-1.5 rounded-lg font-bold transition flex items-center gap-1.5 text-gray-400 hover:text-white">
                        <i class="fas fa-sliders"></i>
                        <span>Practice Mode</span>
                    </button>
                </div>

                <div class="hidden xl:flex items-center gap-3 bg-acc-bgDark px-3.5 py-1.5 rounded-xl border border-acc-borderDark text-xs">
                    <div>
                        <span class="text-gray-400 block text-[10px]">Levels Cleared</span>
                        <span id="nav-total-cleared" class="font-mono font-bold text-xs text-emerald-400">0 / 75</span>
                    </div>
                    <div class="h-5 w-px bg-acc-borderDark"></div>
                    <div>
                        <span class="text-gray-400 block text-[10px]">Total Attempts</span>
                        <span id="nav-total-attempts" class="font-mono font-bold text-xs text-amber-400">0</span>
                    </div>
                    <div class="h-5 w-px bg-acc-borderDark"></div>
                    <div>
                        <span class="text-gray-400 block text-[10px]">Cumulative Score</span>
                        <span id="nav-total-score" class="font-mono font-bold text-xs text-acc-lightPurple">0</span>
                    </div>
                </div>

                <!-- Sound Toggle -->
                <button id="btn-sound" onclick="app.toggleSound()" class="p-2 rounded-xl bg-acc-bgDark hover:bg-gray-800 border border-acc-borderDark text-gray-300 transition" title="Toggle Audio Effects">
                    <i id="icon-sound" class="fas fa-volume-up text-acc-lightPurple"></i>
                </button>

                <!-- Analytics Modal Button -->
                <button onclick="app.openAnalyticsModal()" class="px-3 py-1.5 rounded-xl bg-acc-bgDark hover:bg-gray-800 border border-acc-borderDark text-xs font-semibold text-gray-200 flex items-center gap-1.5 transition">
                    <i class="fas fa-chart-line text-cyan-400"></i>
                    <span class="hidden sm:inline">Analytics</span>
                </button>

                <!-- Dashboard Return Button -->
                <button id="btn-back-home" onclick="app.showDashboard()" class="hidden px-3.5 py-1.5 rounded-xl bg-acc-purple hover:bg-acc-darkPurple text-white text-xs font-bold shadow-lg shadow-acc-purple/25 flex items-center gap-1.5 transition">
                    <i class="fas fa-th-large"></i>
                    <span>All Games</span>
                </button>
            </div>
        </div>
    </header>
"""
'''

with open('site_content.py', 'a', encoding='utf-8') as f:
    f.write(content)

print("Navbar appended successfully.")
