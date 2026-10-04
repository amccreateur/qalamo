import asyncio
import base64
import os
import sys
import subprocess
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TEMP = 'scripts/temp_audio/tafi_proposals'
os.makedirs(TEMP, exist_ok=True)

proposals = [
    ('tafi_hedi_connected', 'Hedi (Connecté: طَفِ)', 'ar-TN-HediNeural', 'طَفِ', '-15%'),
    ('tafi_hedi_spaced', 'Hedi (Décomposé: طَ فِ)', 'ar-TN-HediNeural', 'طَ فِ', '-15%'),
    ('tafi_moaz_connected', 'Moaz (Connecté: طَفِ)', 'ar-QA-MoazNeural', 'طَفِ', '-15%'),
    ('tafi_moaz_spaced', 'Moaz (Décomposé: طَ فِ)', 'ar-QA-MoazNeural', 'طَ فِ', '-15%'),
    ('tafi_shakir_connected', 'Shakir (Connecté: طَفِ)', 'ar-EG-ShakirNeural', 'طَفِ', '-15%'),
    ('tafi_shakir_spaced', 'Shakir (Décomposé: طَ فِ)', 'ar-EG-ShakirNeural', 'طَ فِ', '-15%'),
    ('tafi_hamed_connected', 'Hamed (Connecté: طَفِ)', 'ar-SA-HamedNeural', 'طَفِ', '-15%'),
    ('tafi_hamed_spaced', 'Hamed (Décomposé: طَ فِ)', 'ar-SA-HamedNeural', 'طَ فِ', '-15%'),
]

# Alternate words in A + I with Ṭā'
alternatives = [
    ('tabi_hedi', 'Ṭa-Bi (طَبِ) — Hedi', 'ar-TN-HediNeural', 'طَبِ', '-15%'),
    ('tari_hedi', 'Ṭa-Ri (طَرِ) — Hedi', 'ar-TN-HediNeural', 'طَرِ', '-15%'),
    ('tami_hedi', 'Ṭa-Mi (طَمِ) — Hedi', 'ar-TN-HediNeural', 'طَمِ', '-15%'),
]

async def gen():
    cards = []
    for pid, title, voice, text, rate in proposals:
        raw = f"{TEMP}/{pid}_raw.mp3"
        clean = f"{TEMP}/{pid}.mp3"
        comm = edge_tts.Communicate(text, voice, rate=rate)
        await comm.save(raw)
        cmd = ["ffmpeg", "-y", "-i", raw, "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,volume=6dB,alimiter=limit=0.95", clean]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        with open(clean, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            
        cards.append(f"""
        <div style="background:#151C2C; border:1.5px solid #2A364F; border-radius:16px; padding:18px; text-align:center; display:flex; flex-direction:column; gap:10px;">
            <div style="font-family:'Amiri',serif; font-size:48px; color:#8B5CF6;">طَفِ</div>
            <div style="font-weight:800; color:#FFFFFF; font-size:14px;">{title}</div>
            <button style="background:#8B5CF6; border:none; color:#FFFFFF; font-weight:800; padding:10px 16px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64}').play()">▶ Écouter « Ṭa-Fi »</button>
        </div>
        """)
        print(f"Generated: {title}")

    alt_cards = []
    for pid, title, voice, text, rate in alternatives:
        raw = f"{TEMP}/{pid}_raw.mp3"
        clean = f"{TEMP}/{pid}.mp3"
        comm = edge_tts.Communicate(text, voice, rate=rate)
        await comm.save(raw)
        cmd = ["ffmpeg", "-y", "-i", raw, "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,volume=6dB,alimiter=limit=0.95", clean]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        with open(clean, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            
        alt_cards.append(f"""
        <div style="background:#151C2C; border:1.5px solid #2A364F; border-radius:16px; padding:18px; text-align:center; display:flex; flex-direction:column; gap:10px;">
            <div style="font-family:'Amiri',serif; font-size:48px; color:#34D399;">{text}</div>
            <div style="font-weight:800; color:#FFFFFF; font-size:14px;">{title}</div>
            <button style="background:#10B981; border:none; color:#FFFFFF; font-weight:800; padding:10px 16px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64}').play()">▶ Écouter alternative</button>
        </div>
        """)

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Comparaison : Leçon 29 — Son 2 (طَفِ — Ṭa-Fi)</title>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin:0; padding:0; font-family:'Plus Jakarta Sans', sans-serif; }}
body {{ background:#0B0F19; color:#F8FAFC; padding:40px 16px; display:flex; justify-content:center; }}
.container {{ max-width:900px; width:100%; }}
h1 {{ text-align:center; margin-bottom:12px; font-size:26px; color:#A78BFA; }}
h2 {{ text-align:center; margin-top:36px; margin-bottom:14px; font-size:20px; color:#34D399; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(260px, 1fr)); gap:16px; margin-top:16px; }}
</style>
</head>
<body>
<div class="container">
    <h1>🎯 Leçon 29 — Son 2 : « Ṭa-Fi » (طَفِ)</h1>
    <p style="text-align:center; color:#94A3B8; margin-bottom:24px;">Voici les différentes versions audio pour <strong>طَفِ (Ṭā' emphatique + Fi)</strong> :</p>
    <div class="grid">
        {''.join(cards)}
    </div>

    <h2>🔄 Ou remplacer par une autre combinaison :</h2>
    <div class="grid">
        {''.join(alt_cards)}
    </div>
</div>
</body>
</html>"""

    with open("test_tafi_comparison.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Created: test_tafi_comparison.html")

if __name__ == "__main__":
    asyncio.run(gen())
