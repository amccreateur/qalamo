import asyncio
import os
import subprocess
import edge_tts
import base64

async def main():
    temp_dir = 'scripts/temp_audio/dad_tests'
    os.makedirs(temp_dir, exist_ok=True)
    
    # We test combinations with Ḍād where the "D" sound is distinct and never sounds like "Z"
    voices_and_texts = [
        # Hamed (Saudi - strong classical D sound for Ḍād)
        ('hamed_duri', 'Hamed — ضُرِ (Ḍou-Ri)', 'ar-SA-HamedNeural', 'ضُرِ', '-15%'),
        ('hamed_dubi', 'Hamed — ضُبِ (Ḍou-Bi)', 'ar-SA-HamedNeural', 'ضُبِ', '-15%'),
        ('hamed_dumi', 'Hamed — ضُمِ (Ḍou-Mi)', 'ar-SA-HamedNeural', 'ضُمِ', '-15%'),
        ('hamed_dari', 'Hamed — ضَرِ (Ḍa-Ri)', 'ar-SA-HamedNeural', 'ضَرِ', '-15%'),
        ('hamed_dabi', 'Hamed — ضَبِ (Ḍa-Bi)', 'ar-SA-HamedNeural', 'ضَبِ', '-15%'),

        # Shakir (Egyptian - classical Al-Azhar D sound for Ḍād)
        ('shakir_duri', 'Shakir — ضُرِ (Ḍou-Ri)', 'ar-EG-ShakirNeural', 'ضُرِ', '-15%'),
        ('shakir_dubi', 'Shakir — ضُبِ (Ḍou-Bi)', 'ar-EG-ShakirNeural', 'ضُبِ', '-15%'),
        ('shakir_dumi', 'Shakir — ضُمِ (Ḍou-Mi)', 'ar-EG-ShakirNeural', 'ضُمِ', '-15%'),
        ('shakir_dabi', 'Shakir — ضَبِ (Ḍa-Bi)', 'ar-EG-ShakirNeural', 'ضَبِ', '-15%'),

        # Moaz (Gulf - very sharp D sound)
        ('moaz_duri', 'Moaz — ضُرِ (Ḍou-Ri)', 'ar-QA-MoazNeural', 'ضُرِ', '-15%'),
        ('moaz_dubi', 'Moaz — ضُبِ (Ḍou-Bi)', 'ar-QA-MoazNeural', 'ضُبِ', '-15%'),
        ('moaz_dumi', 'Moaz — ضُمِ (Ḍou-Mi)', 'ar-QA-MoazNeural', 'ضُمِ', '-15%'),
        ('moaz_dabi', 'Moaz — ضَبِ (Ḍa-Bi)', 'ar-QA-MoazNeural', 'ضَبِ', '-15%'),

        # Zariyah (Saudi)
        ('zariyah_dubi', 'Zariyah — ضُبِ (Ḍou-Bi)', 'ar-SA-ZariyahNeural', 'ضُبِ', '-15%'),
        ('zariyah_duri', 'Zariyah — ضُرِ (Ḍou-Ri)', 'ar-SA-ZariyahNeural', 'ضُرِ', '-15%'),
    ]

    cards = []
    for cid, title, voice, text, rate in voices_and_texts:
        raw = f'{temp_dir}/{cid}_raw.mp3'
        clean = f'{temp_dir}/{cid}.mp3'
        c_comm = edge_tts.Communicate(text, voice, rate=rate)
        await c_comm.save(raw)
        subprocess.run(['ffmpeg', '-y', '-i', raw, '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,volume=6dB,alimiter=limit=0.95', clean], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        with open(clean, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        
        cards.append(f"""
        <div style="background:#151C2C; border:1.5px solid #2A364F; border-radius:16px; padding:18px; text-align:center; display:flex; flex-direction:column; gap:10px;">
            <div style="font-family:'Amiri',serif; font-size:46px; color:#F59E0B;">{text}</div>
            <div style="font-weight:800; color:#FFFFFF; font-size:14px;">{title}</div>
            <button style="background:#D97706; border:none; color:#FFFFFF; font-weight:800; padding:10px 16px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64}').play()">▶ Écouter « {text} »</button>
        </div>
        """)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Correction : Ḍād (ض) — Vrai son « Dou / Da » (Pas « Zou »)</title>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin:0; padding:0; font-family:'Plus Jakarta Sans', sans-serif; }}
body {{ background:#0B0F19; color:#F8FAFC; padding:40px 16px; display:flex; justify-content:center; }}
.container {{ max-width:960px; width:100%; }}
h1 {{ text-align:center; margin-bottom:12px; font-size:26px; color:#F59E0B; }}
p {{ text-align:center; color:#94A3B8; margin-bottom:24px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:16px; margin-top:16px; }}
.badge {{ background:rgba(245,158,11,0.15); border:1px solid #F59E0B; border-radius:12px; padding:14px; margin-bottom:20px; text-align:center; color:#FBBF24; font-weight:bold; }}
</style>
</head>
<body>
<div class="container">
    <div class="badge">
        🎯 Objectif : Vrai son « Dou / Ḍād (ض) » bien claquant, sans aucune déformation en « Zou »
    </div>
    <h1>Écoute des voix avec le vrai son « Dou » (ض)</h1>
    <p>Cliquez pour écouter et dites-moi laquelle prononce parfaitement le <strong>Ḍād (ض)</strong> :</p>
    
    <div class="grid">
        {''.join(cards)}
    </div>
</div>
</body>
</html>
"""
    with open('test_dad_damma.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated test_dad_damma.html successfully!')

if __name__ == '__main__':
    asyncio.run(main())
