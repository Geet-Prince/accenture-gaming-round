# generate_index_full.py
import re

print("Constructing full index.html...")

with open('accenture_gaming_assessment_simulator.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Extract script 2
scripts = list(re.finditer(r'<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>', orig))
script2_code = scripts[1].group(1)

# Enhance SoundFX with audio context resume
script2_enhanced = script2_code.replace(
    """init() {
                if (!this.ctx) {
                    const AudioCtx = window.AudioContext || window.webkitAudioContext;
                    if (AudioCtx) this.ctx = new AudioCtx();
                }
            }""",
    """init() {
                if (!this.ctx) {
                    const AudioCtx = window.AudioContext || window.webkitAudioContext;
                    if (AudioCtx) this.ctx = new AudioCtx();
                }
                if (this.ctx && this.ctx.state === 'suspended') {
                    this.ctx.resume().catch(() => {});
                }
            }"""
)

# Enhance MemoryMazeGame.render to include on-screen mobile Touch D-Pad
mm_target = """                html += `</div></div>`;
                this.mount.innerHTML = html;
            }"""

mm_replace = """                html += `</div>`;
                
                // On-screen mobile touch D-Pad for smartphone & tablet usability across India
                if (this.phase === 'NAVIGATE') {
                    html += `
                        <div class="flex flex-col items-center gap-1.5 mt-3 select-none">
                            <button onclick="app.handleDirection('UP')" class="w-12 h-12 rounded-xl bg-acc-cardDark hover:bg-acc-purple/30 active:bg-acc-purple border border-acc-borderDark text-white flex items-center justify-center text-lg shadow-md transition touch-manipulation" title="Move Up">
                                <i class="fas fa-arrow-up"></i>
                            </button>
                            <div class="flex items-center gap-3">
                                <button onclick="app.handleDirection('LEFT')" class="w-12 h-12 rounded-xl bg-acc-cardDark hover:bg-acc-purple/30 active:bg-acc-purple border border-acc-borderDark text-white flex items-center justify-center text-lg shadow-md transition touch-manipulation" title="Move Left">
                                    <i class="fas fa-arrow-left"></i>
                                </button>
                                <button onclick="app.handleDirection('DOWN')" class="w-12 h-12 rounded-xl bg-acc-cardDark hover:bg-acc-purple/30 active:bg-acc-purple border border-acc-borderDark text-white flex items-center justify-center text-lg shadow-md transition touch-manipulation" title="Move Down">
                                    <i class="fas fa-arrow-down"></i>
                                </button>
                                <button onclick="app.handleDirection('RIGHT')" class="w-12 h-12 rounded-xl bg-acc-cardDark hover:bg-acc-purple/30 active:bg-acc-purple border border-acc-borderDark text-white flex items-center justify-center text-lg shadow-md transition touch-manipulation" title="Move Right">
                                    <i class="fas fa-arrow-right"></i>
                                </button>
                            </div>
                            <span class="text-[11px] text-gray-400 mt-0.5"><i class="fas fa-mobile-screen mr-1"></i>Mobile Touch D-Pad • Arrow Keys / WASD also work</span>
                        </div>
                    `;
                }
                
                html += `</div>`;
                this.mount.innerHTML = html;
            }"""
script2_enhanced = script2_enhanced.replace(mm_target, mm_replace, 1)

# Enhance KeyDoorMazeGame.render to include on-screen mobile Touch D-Pad
kd_target = """                html += `</div>`;
                this.mount.innerHTML = html;
            }
        }

        /* ==========================================================================
           GAME 5: MEMORY RECALL"""

kd_replace = """                html += `</div>`;

                // On-screen mobile touch D-Pad for smartphone & tablet usability across India
                html += `
                    <div class="flex flex-col items-center gap-1.5 mt-3 select-none">
                        <button onclick="app.handleDirection('UP')" class="w-12 h-12 rounded-xl bg-acc-cardDark hover:bg-acc-purple/30 active:bg-acc-purple border border-acc-borderDark text-white flex items-center justify-center text-lg shadow-md transition touch-manipulation" title="Move Up">
                            <i class="fas fa-arrow-up"></i>
                        </button>
                        <div class="flex items-center gap-3">
                            <button onclick="app.handleDirection('LEFT')" class="w-12 h-12 rounded-xl bg-acc-cardDark hover:bg-acc-purple/30 active:bg-acc-purple border border-acc-borderDark text-white flex items-center justify-center text-lg shadow-md transition touch-manipulation" title="Move Left">
                                <i class="fas fa-arrow-left"></i>
                            </button>
                            <button onclick="app.handleDirection('DOWN')" class="w-12 h-12 rounded-xl bg-acc-cardDark hover:bg-acc-purple/30 active:bg-acc-purple border border-acc-borderDark text-white flex items-center justify-center text-lg shadow-md transition touch-manipulation" title="Move Down">
                                <i class="fas fa-arrow-down"></i>
                            </button>
                            <button onclick="app.handleDirection('RIGHT')" class="w-12 h-12 rounded-xl bg-acc-cardDark hover:bg-acc-purple/30 active:bg-acc-purple border border-acc-borderDark text-white flex items-center justify-center text-lg shadow-md transition touch-manipulation" title="Move Right">
                                <i class="fas fa-arrow-right"></i>
                            </button>
                        </div>
                        <span class="text-[11px] text-gray-400 mt-0.5"><i class="fas fa-mobile-screen mr-1"></i>Mobile Touch D-Pad • Arrow Keys / WASD also work</span>
                    </div>
                `;

                this.mount.innerHTML = html;
            }
        }

        /* ==========================================================================
           GAME 5: MEMORY RECALL"""
script2_enhanced = script2_enhanced.replace(kd_target, kd_replace, 1)

# Enhance openAnalyticsModal
analytics_target = """body.innerHTML = html;
                document.getElementById('modal-analytics').classList.remove('hidden');
            }"""

analytics_replace = """// Add Diagnostic Performance summary & Print / Save PDF action
                html += `
                    <div class="mt-6 p-4 rounded-xl bg-acc-bgDark border border-acc-borderDark flex flex-wrap items-center justify-between gap-4">
                        <div>
                            <span class="text-xs font-semibold text-emerald-400 flex items-center gap-1.5">
                                <i class="fas fa-shield-halved"></i> Diagnostic Benchmark Status
                            </span>
                            <p class="text-xs text-gray-300 mt-0.5">Recommended minimum benchmark for Accenture ASE & AAH interviews: <strong>Clear 10+ Levels per game</strong> with &ge;80% accuracy.</p>
                        </div>
                        <button onclick="window.print()" class="px-4 py-2 rounded-xl bg-acc-purple hover:bg-acc-darkPurple text-white text-xs font-bold shadow-lg shadow-acc-purple/20 flex items-center gap-2 transition">
                            <i class="fas fa-print"></i>
                            <span>Print / Save Diagnostic Report (PDF)</span>
                        </button>
                    </div>
                `;
                body.innerHTML = html;
                document.getElementById('modal-analytics').classList.remove('hidden');
            }"""
script2_enhanced = script2_enhanced.replace(analytics_target, analytics_replace, 1)

# Extract original simulation views
view_dash_start = orig.find('<!-- ==========================================\n             VIEW 1: DASHBOARD / HOME SCREEN')
main_end_idx = orig.find('</main>')
sim_views_html = orig[view_dash_start:main_end_idx]

# Extract modals
modals_block = orig[main_end_idx + len('</main>'):scripts[1].start()]

print("Simulation components ready.")
