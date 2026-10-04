import asyncio
import base64
import os
import sys
import subprocess
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 28 Arabic Letters with Kasra
LETTERS = [
    {"id": "alif_kasra", "char": "إِ", "name": "Alif Kasrah", "text_direct": "إِ", "text_alt": "إِي", "category": "Voyelle pure", "phonetic": "’I"},
    {"id": "ba_kasra", "char": "بِ", "name": "Bā' Kasrah", "text_direct": "بِـ", "text_alt": "بِي", "category": "Labiale", "phonetic": "Bi"},
    {"id": "ta_kasra", "char": "تِ", "name": "Tā' Kasrah", "text_direct": "تِـ", "text_alt": "تِي", "category": "Dentale fine", "phonetic": "Ti"},
    {"id": "tha_kasra", "char": "ثِ", "name": "Thā' Kasrah", "text_direct": "ثِـ", "text_alt": "ثِي", "category": "Interdentale", "phonetic": "Thi"},
    {"id": "jeem_kasra", "char": "جِ", "name": "Jeem Kasrah", "text_direct": "جِـ", "text_alt": "جِي", "category": "Palatale", "phonetic": "Dji"},
    {"id": "hha_kasra", "char": "حِ", "name": "Ḥā' Kasrah", "text_direct": "حِـ", "text_alt": "حِي", "category": "Gorge douce", "phonetic": "Ḥi"},
    {"id": "kha_kasra", "char": "خِ", "name": "Khā' Kasrah", "text_direct": "خِـ", "text_alt": "خِي", "category": "Emphatique / Gutturale", "phonetic": "Khi"},
    {"id": "dal_kasra", "char": "دِ", "name": "Dāl Kasrah", "text_direct": "دِ", "text_alt": "دِي", "category": "Dentale fine", "phonetic": "Di"},
    {"id": "dhal_kasra", "char": "ذِ", "name": "Dhāl Kasrah", "text_direct": "ذِ", "text_alt": "ذِي", "category": "Interdentale", "phonetic": "Dhi"},
    {"id": "ra_kasra", "char": "رِ", "name": "Rā' Kasrah", "text_direct": "رِ", "text_alt": "رِي", "category": "Roulée fine", "phonetic": "Ri"},
    {"id": "zay_kasra", "char": "زِ", "name": "Zāy Kasrah", "text_direct": "زِ", "text_alt": "زِي", "category": "Sifflante sonore", "phonetic": "Zi"},
    {"id": "seen_kasra", "char": "سِ", "name": "Sīn Kasrah", "text_direct": "سِـ", "text_alt": "سِي", "category": "Sifflante fine", "phonetic": "Si"},
    {"id": "sheen_kasra", "char": "شِ", "name": "Shīn Kasrah", "text_direct": "شِـ", "text_alt": "شِي", "category": "Chuintante", "phonetic": "Shi"},
    {"id": "sad_kasra", "char": "صِ", "name": "Ṣād Kasrah", "text_direct": "صِـ", "text_alt": "صِي", "category": "Emphatique", "phonetic": "Ṣi"},
    {"id": "dad_kasra", "char": "ضِ", "name": "Ḍād Kasrah", "text_direct": "ضِـ", "text_alt": "ضِي", "category": "Emphatique", "phonetic": "Ḍi"},
    {"id": "ttaa_kasra", "char": "طِ", "name": "Ṭā' Kasrah", "text_direct": "طِـ", "text_alt": "طِي", "category": "Emphatique", "phonetic": "Ṭi"},
    {"id": "zha_kasra", "char": "ظِ", "name": "Ẓā' Kasrah", "text_direct": "ظِـ", "text_alt": "ظِي", "category": "Emphatique", "phonetic": "Ẓi"},
    {"id": "ayn_kasra", "char": "عِ", "name": "ʿAyn Kasrah", "text_direct": "عِـ", "text_alt": "عِي", "category": "Gorge profonde", "phonetic": "ʿI"},
    {"id": "ghayn_kasra", "char": "غِ", "name": "Ghayn Kasrah", "text_direct": "غِـ", "text_alt": "غِي", "category": "Emphatique", "phonetic": "Ghi"},
    {"id": "fa_kasra", "char": "فِ", "name": "Fā' Kasrah", "text_direct": "فِـ", "text_alt": "فِي", "category": "Labio-dentale", "phonetic": "Fi"},
    {"id": "qaf_kasra", "char": "قِ", "name": "Qāf Kasrah", "text_direct": "قِـ", "text_alt": "قِي", "category": "Uvulaire profonde", "phonetic": "Qi"},
    {"id": "kaf_kasra", "char": "كِ", "name": "Kāf Kasrah", "text_direct": "كِـ", "text_alt": "كِي", "category": "Palatale fine", "phonetic": "Ki"},
    {"id": "lam_kasra", "char": "لِ", "name": "Lām Kasrah", "text_direct": "لِـ", "text_alt": "لِي", "category": "Liquide", "phonetic": "Li"},
    {"id": "meem_kasra", "char": "مِ", "name": "Mīm Kasrah", "text_direct": "مِـ", "text_alt": "مِي", "category": "Nasale labiale", "phonetic": "Mi"},
    {"id": "noon_kasra", "char": "نِ", "name": "Nūn Kasrah", "text_direct": "نِـ", "text_alt": "نِي", "category": "Nasale dentale", "phonetic": "Ni"},
    {"id": "haa_kasra", "char": "هِ", "name": "Hā' Kasrah", "text_direct": "هِـ", "text_alt": "هِي", "category": "Laryngale douce", "phonetic": "Hi"},
    {"id": "waw_kasra", "char": "وِ", "name": "Wāw Kasrah", "text_direct": "وِ", "text_alt": "وِي", "category": "Semi-voyelle", "phonetic": "Wi"},
    {"id": "yaa_kasra", "char": "يِ", "name": "Yā' Kasrah", "text_direct": "يِـ", "text_alt": "يِي", "category": "Semi-voyelle", "phonetic": "Yi"},
]

VOICES = [
    {"key": "shakir", "name": "Shakir (Prolongé)", "voice": "ar-EG-ShakirNeural", "badge": "Shakir", "color": "#3B82F6", "rate": "-22%"},
    {"key": "hamed", "name": "Hamed (Prolongé)", "voice": "ar-SA-HamedNeural", "badge": "Hamed", "color": "#10B981", "rate": "-22%"},
    {"key": "moaz", "name": "Moaz (Prolongé)", "voice": "ar-QA-MoazNeural", "badge": "Moaz", "color": "#F59E0B", "rate": "-22%"},
    {"key": "hedi", "name": "Hedi (Prolongé)", "voice": "ar-TN-HediNeural", "badge": "Hedi", "color": "#8B5CF6", "rate": "-22%"},
]

CACHE_DIR = "scripts/temp_audio/kasra_proposals"
os.makedirs(CACHE_DIR, exist_ok=True)

async def generate_proposal(text_direct: str, text_alt: str, voice: str, rate: str, out_path: str):
    raw_path = out_path.replace(".mp3", "_raw.mp3")
    
    # Prioritize sustained text_alt (e.g. بِي, تِي) with slower rate for clear, prolonged duration
    for t in [text_alt, text_direct, text_direct.replace("ـ", "")]:
        try:
            communicate = edge_tts.Communicate(t, voice, rate=rate)
            await communicate.save(raw_path)
            if os.path.exists(raw_path) and os.path.getsize(raw_path) > 300:
                # Clean audio with ffmpeg: gentle threshold so tail is preserved
                cmd = [
                    "ffmpeg", "-y", "-i", raw_path,
                    "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-55dB,volume=6dB,alimiter=limit=0.95",
                    out_path
                ]
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if os.path.exists(raw_path):
                    os.remove(raw_path)
                return
        except Exception:
            continue

def get_b64(path: str) -> str:
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

async def main():
    print("Generation des propositions audio pour les 28 lettres avec Kasra...")
    
    for item in LETTERS:
        for v in VOICES:
            out_file = f"{CACHE_DIR}/{item['id']}_{v['key']}.mp3"
            await generate_proposal(item["text_direct"], item["text_alt"], v["voice"], v["rate"], out_file)
            print(f"  [OK] {item['name']} ({v['key']})")

    print("\nAssemblage de la page HTML interactive...")
    
    cards_html = []
    
    for idx, item in enumerate(LETTERS, 1):
        # Current app audio
        current_path = f"assets/audio/generated/{item['id']}.mp3"
        current_b64 = get_b64(current_path)
        
        proposals_b64 = {}
        for v in VOICES:
            v_path = f"{CACHE_DIR}/{item['id']}_{v['key']}.mp3"
            proposals_b64[v['key']] = get_b64(v_path)
        
        btn_current = f"""
        <button class="audio-btn btn-current" onclick="playAudio('{item['id']}_current', this)">
            <span class="btn-icon">▶</span>
            <span class="btn-label">Actuel</span>
        </button>
        <audio id="{item['id']}_current" src="data:audio/mp3;base64,{current_b64}"></audio>
        """ if current_b64 else ""

        btns_proposals = []
        for v in VOICES:
            b64 = proposals_b64[v['key']]
            if b64:
                btns_proposals.append(f"""
                <div class="voice-opt">
                    <button class="audio-btn" style="--btn-color: {v['color']}" onclick="playAudio('{item['id']}_{v['key']}', this)">
                        <span class="btn-icon">▶</span>
                        <span class="btn-label">{v['badge']}</span>
                    </button>
                    <label class="radio-label">
                        <input type="radio" name="choice_{item['id']}" value="{v['key']}" onchange="recordChoice('{item['id']}', '{v['badge']}', '{item['name']}')">
                        <span>Choisir</span>
                    </label>
                    <audio id="{item['id']}_{v['key']}" src="data:audio/mp3;base64,{b64}"></audio>
                </div>
                """)
        
        card = f"""
        <div class="letter-card" data-category="{item['category']}">
            <div class="letter-header">
                <div class="letter-badge">#{idx}</div>
                <div class="letter-char">{item['char']}</div>
                <div class="letter-info">
                    <div class="letter-title">{item['name']}</div>
                    <div class="letter-meta">
                        <span class="pill-category">{item['category']}</span>
                        <span class="pill-phonetic">{item['phonetic']}</span>
                    </div>
                </div>
            </div>

            <div class="audio-grid">
                <div class="voice-opt current-opt">
                    {btn_current}
                    <label class="radio-label">
                        <input type="radio" name="choice_{item['id']}" value="current" checked onchange="recordChoice('{item['id']}', 'Actuel', '{item['name']}')">
                        <span>Garder actuel</span>
                    </label>
                </div>
                {''.join(btns_proposals)}
            </div>
            
            <div class="choice-indicator" id="choice_badge_{item['id']}">
                Sélection : <strong>Actuel</strong>
            </div>
        </div>
        """
        cards_html.append(card)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Qalamo — Les 28 Lettres avec Kasrah (ـِ) : Console de Choix Audio</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-main: #0B0F19;
            --bg-card: #151C2C;
            --bg-card-hover: #1A2338;
            --border-card: #2A364F;
            --primary: #3B82F6;
            --success: #10B981;
            --warning: #F59E0B;
            --purple: #8B5CF6;
            --text-main: #F8FAFC;
            --text-muted: #94A3B8;
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        body {{
            background: var(--bg-main);
            color: var(--text-main);
            padding: 30px 16px 130px;
            display: flex;
            justify-content: center;
        }}
        .container {{
            width: 100%;
            max-width: 1200px;
        }}
        header {{
            text-align: center;
            margin-bottom: 28px;
            background: linear-gradient(135deg, #1E293B, #0F172A);
            border: 1px solid var(--border-card);
            padding: 28px 20px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}
        h1 {{
            font-size: 28px;
            font-weight: 800;
            background: linear-gradient(135deg, #60A5FA, #34D399, #FBBF24);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }}
        p.subtitle {{
            color: var(--text-muted);
            font-size: 15px;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
        }}
        .summary-bar {{
            margin-top: 18px;
            display: flex;
            gap: 12px;
            justify-content: center;
            flex-wrap: wrap;
        }}
        .stat-pill {{
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 700;
            color: #E2E8F0;
        }}
        
        .filter-tabs {{
            display: flex;
            gap: 8px;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 24px;
        }}
        .filter-btn {{
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            color: var(--text-muted);
            padding: 8px 18px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .filter-btn.active, .filter-btn:hover {{
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }}

        .letters-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 16px;
        }}
        .letter-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            border-radius: 18px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            transition: transform 0.2s, border-color 0.2s;
        }}
        .letter-card:hover {{
            transform: translateY(-2px);
            border-color: var(--primary);
            background: var(--bg-card-hover);
        }}
        .letter-header {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}
        .letter-badge {{
            font-size: 12px;
            font-weight: 800;
            color: var(--text-muted);
            background: rgba(255, 255, 255, 0.05);
            padding: 4px 8px;
            border-radius: 8px;
        }}
        .letter-char {{
            font-family: 'Amiri', serif;
            font-size: 48px;
            font-weight: 700;
            color: #60A5FA;
            line-height: 1;
            min-width: 54px;
            text-align: center;
        }}
        .letter-info {{
            flex: 1;
        }}
        .letter-title {{
            font-size: 17px;
            font-weight: 800;
            color: #FFFFFF;
            margin-bottom: 4px;
        }}
        .letter-meta {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .pill-category {{
            background: rgba(59, 130, 246, 0.15);
            color: #93C5FD;
            font-size: 11px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 6px;
        }}
        .pill-phonetic {{
            background: rgba(16, 185, 129, 0.15);
            color: #6EE7B7;
            font-size: 11px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 6px;
        }}

        .audio-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            background: rgba(0, 0, 0, 0.25);
            padding: 12px;
            border-radius: 14px;
        }}
        .voice-opt {{
            display: flex;
            flex-direction: column;
            gap: 6px;
            align-items: center;
        }}
        .current-opt {{
            grid-column: span 2;
            flex-direction: row;
            justify-content: space-between;
            padding-bottom: 8px;
            border-bottom: 1px dashed var(--border-card);
            margin-bottom: 4px;
        }}
        .audio-btn {{
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.07);
            border: 1.5px solid var(--btn-color, var(--border-card));
            color: #FFFFFF;
            padding: 8px 12px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.15s;
        }}
        .audio-btn:hover {{
            background: var(--btn-color, var(--primary));
            color: #FFFFFF;
            transform: scale(1.02);
        }}
        .audio-btn.playing {{
            background: var(--btn-color, var(--primary)) !important;
            box-shadow: 0 0 12px var(--btn-color, var(--primary));
        }}
        .btn-current {{
            --btn-color: #64748B;
            width: auto;
            padding: 6px 14px;
        }}
        .btn-icon {{
            font-size: 11px;
        }}
        .radio-label {{
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 11px;
            font-weight: 700;
            color: var(--text-muted);
            cursor: pointer;
        }}
        .radio-label input {{
            cursor: pointer;
            accent-color: var(--primary);
        }}
        .choice-indicator {{
            font-size: 12px;
            color: var(--text-muted);
            text-align: right;
            padding-top: 4px;
        }}
        .choice-indicator strong {{
            color: #60A5FA;
        }}

        /* Floating bottom bar */
        .bottom-bar {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(12px);
            border-top: 1px solid var(--border-card);
            padding: 16px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            z-index: 1000;
            box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
        }}
        .bottom-summary {{
            font-size: 14px;
            font-weight: 700;
            color: #E2E8F0;
        }}
        .action-btns {{
            display: flex;
            gap: 12px;
        }}
        .btn-action {{
            background: linear-gradient(135deg, var(--primary), #2563EB);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 12px;
            font-weight: 800;
            font-size: 14px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
            transition: all 0.2s;
        }}
        .btn-action:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(59, 130, 246, 0.6);
        }}
        .copied-toast {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--success);
            color: white;
            padding: 14px 28px;
            border-radius: 12px;
            font-weight: 800;
            box-shadow: 0 10px 25px rgba(16, 185, 129, 0.4);
            display: none;
            z-index: 2000;
        }}
    </style>
</head>
<body>
    <div class="copied-toast" id="toast">✅ Vos choix ont été copiés ! Vous pouvez les coller directement dans le chat.</div>

    <div class="container">
        <header>
            <h1>Console d'Écoute : Les 28 Lettres avec Kasrah (ـِ)</h1>
            <p class="subtitle">
                Écoutez et comparez les différentes voix pour chaque lettre de l'alphabet avec la voyelle <strong>Kasrah (i)</strong> :
                comparez la version <strong>Actuelle</strong> avec <strong>Shakir</strong> (Saoudien classique), <strong>Hamed</strong> (Saoudien clair), <strong>Moaz</strong> (Posé) et <strong>Hedi</strong> (Tunisien articulé).
            </p>
            <div class="summary-bar">
                <div class="stat-pill">📚 28 Lettres Complètes</div>
                <div class="stat-pill">🎙️ 5 Écoutes par Lettre (140 Audios)</div>
                <div class="stat-pill">🔊 Studio HD Pure Syllable</div>
            </div>
        </header>

        <div class="filter-tabs">
            <button class="filter-btn active" onclick="filterCategory('all', this)">Toutes (28)</button>
            <button class="filter-btn" onclick="filterCategory('Emphatique', this)">Emphatiques (صِ, ضِ, طِ, ظِ, غِ, خِ, قِ)</button>
            <button class="filter-btn" onclick="filterCategory('Gorge', this)">Gorge (حِ, عِ, هِ)</button>
            <button class="filter-btn" onclick="filterCategory('Sifflante', this)">Sifflantes (سِ, زِ, شِ)</button>
            <button class="filter-btn" onclick="filterCategory('Dentale', this)">Dentales (تِ, دِ, ثِ, ذِ)</button>
        </div>

        <div class="letters-grid">
            {''.join(cards_html)}
        </div>
    </div>

    <div class="bottom-bar">
        <div class="bottom-summary" id="bottom_counter">
            28 / 28 lettres disponibles (Toutes sur "Actuel" par défaut)
        </div>
        <div class="action-btns">
            <button class="btn-action" onclick="copyChoices()">📋 Copier mes choix pour l'assistant</button>
        </div>
    </div>

    <script>
        let userChoices = {{}};
        let currentPlayingBtn = null;

        function playAudio(id, btn) {{
            document.querySelectorAll('audio').forEach(a => {{
                a.pause();
                a.currentTime = 0;
            }});
            document.querySelectorAll('.audio-btn').forEach(b => b.classList.remove('playing'));
            
            const audio = document.getElementById(id);
            if (audio) {{
                audio.play();
                if (btn) {{
                    btn.classList.add('playing');
                    audio.onended = () => btn.classList.remove('playing');
                }}
            }}
        }}

        function recordChoice(letterId, voiceName, letterName) {{
            userChoices[letterId] = {{ voice: voiceName, name: letterName }};
            const badge = document.getElementById('choice_badge_' + letterId);
            if (badge) {{
                badge.innerHTML = 'Sélection : <strong style="color: #34D399">' + voiceName + '</strong>';
            }}
            updateBottomCounter();
        }}

        function updateBottomCounter() {{
            const changed = Object.values(userChoices).filter(c => c.voice !== 'Actuel').length;
            document.getElementById('bottom_counter').innerText = 
                changed > 0 ? (changed + ' modification(s) sélectionnée(s) sur 28 lettres') : '28 lettres (Toutes sur "Actuel" par défaut)';
        }}

        function filterCategory(cat, btn) {{
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            document.querySelectorAll('.letter-card').forEach(card => {{
                if (cat === 'all') {{
                    card.style.display = 'flex';
                }} else {{
                    const cardCat = card.getAttribute('data-category') || '';
                    if (cardCat.includes(cat)) {{
                        card.style.display = 'flex';
                    }} else {{
                        card.style.display = 'none';
                    }}
                }}
            }});
        }}

        function copyChoices() {{
            let text = "Voici mes préférences pour les lettres avec Kasrah :\\n\\n";
            let changedCount = 0;
            
            document.querySelectorAll('.letter-card').forEach(card => {{
                const input = card.querySelector('input[type="radio"]:checked');
                const title = card.querySelector('.letter-title').innerText;
                const char = card.querySelector('.letter-char').innerText;
                const val = input ? input.value : 'current';
                
                let voiceName = 'Actuel';
                if (val === 'shakir') voiceName = 'Shakir';
                if (val === 'hamed') voiceName = 'Hamed';
                if (val === 'moaz') voiceName = 'Moaz';
                if (val === 'hedi') voiceName = 'Hedi';
                
                text += "- " + char + " (" + title + ") : " + voiceName + "\\n";
                if (val !== 'current') changedCount++;
            }});

            navigator.clipboard.writeText(text).then(() => {{
                const toast = document.getElementById('toast');
                toast.style.display = 'block';
                setTimeout(() => {{ toast.style.display = 'none'; }}, 3500);
            }}).catch(() => {{
                alert(text);
            }});
        }}
    </script>
</body>
</html>
    """

    out_html = "test_all_kasra_proposals.html"
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"\n[SUCCESS] Console de comparaison créée: {out_html}")

if __name__ == "__main__":
    asyncio.run(main())
