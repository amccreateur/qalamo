import asyncio
import os
import subprocess
import edge_tts
import base64

async def main():
    os.makedirs('assets/audio/generated', exist_ok=True)
    temp_dir = 'scripts/temp_audio/lesson30_proposals'
    os.makedirs(temp_dir, exist_ok=True)
    
    # 1. Generate subi (صُبِ) by Hedi
    raw_subi = f'{temp_dir}/subi_raw.mp3'
    clean_subi = 'assets/audio/generated/subi.mp3'
    comm = edge_tts.Communicate('صُبِ', 'ar-TN-HediNeural', rate='-15%')
    await comm.save(raw_subi)
    subprocess.run(['ffmpeg', '-y', '-i', raw_subi, '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,volume=6dB,alimiter=limit=0.95', clean_subi], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Also suri_emph.mp3 as fallback
    subprocess.run(['ffmpeg', '-y', '-i', raw_subi, '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,volume=6dB,alimiter=limit=0.95', 'assets/audio/generated/suri_emph.mp3'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print('Generated subi.mp3 successfully!')

    # 2. Generate candidates for Sound 2 of Lesson 30
    candidates = [
        ('duri_hedi_conn', 'Ḍou-Ri (ضُرِ) — Hedi', 'ar-TN-HediNeural', 'ضُرِ', '-15%'),
        ('duri_moaz_conn', 'Ḍou-Ri (ضُرِ) — Moaz', 'ar-QA-MoazNeural', 'ضُرِ', '-15%'),
        ('duri_shakir_conn', 'Ḍou-Ri (ضُرِ) — Shakir', 'ar-EG-ShakirNeural', 'ضُرِ', '-15%'),
        ('duri_hamed_conn', 'Ḍou-Ri (ضُرِ) — Hamed', 'ar-SA-HamedNeural', 'ضُرِ', '-15%'),
        
        ('dubi_hedi', 'Ḍou-Bi (ضُبِ) — Hedi', 'ar-TN-HediNeural', 'ضُبِ', '-15%'),
        ('dubi_moaz', 'Ḍou-Bi (ضُبِ) — Moaz', 'ar-QA-MoazNeural', 'ضُبِ', '-15%'),
        ('dumi_hedi', 'Ḍou-Mi (ضُمِ) — Hedi', 'ar-TN-HediNeural', 'ضُمِ', '-15%'),
        ('dumi_moaz', 'Ḍou-Mi (ضُمِ) — Moaz', 'ar-QA-MoazNeural', 'ضُمِ', '-15%'),
        ('dufa_hedi', 'Ḍou-Fa (ضُفَ) — Hedi', 'ar-TN-HediNeural', 'ضُفَ', '-15%'),
        ('duli_hedi', 'Ḍou-Li (ضُلِ) — Hedi', 'ar-TN-HediNeural', 'ضُلِ', '-15%'),
    ]

    cards_duri = []
    cards_alt = []

    for cid, title, voice, text, rate in candidates:
        craw = f'{temp_dir}/{cid}_raw.mp3'
        cclean = f'{temp_dir}/{cid}.mp3'
        c_comm = edge_tts.Communicate(text, voice, rate=rate)
        await c_comm.save(craw)
        subprocess.run(['ffmpeg', '-y', '-i', craw, '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,volume=6dB,alimiter=limit=0.95', cclean], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        with open(cclean, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        
        card_html = f"""
        <div style="background:#151C2C; border:1.5px solid #2A364F; border-radius:16px; padding:18px; text-align:center; display:flex; flex-direction:column; gap:10px;">
            <div style="font-family:'Amiri',serif; font-size:46px; color:#38BDF8;">{text}</div>
            <div style="font-weight:800; color:#FFFFFF; font-size:14px;">{title}</div>
            <button style="background:#0284C7; border:none; color:#FFFFFF; font-weight:800; padding:10px 16px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64}').play()">▶ Écouter</button>
        </div>
        """
        if 'Ḍou-Ri' in title:
            cards_duri.append(card_html)
        else:
            cards_alt.append(card_html)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Comparaison : Leçon 30 — 2ème Son</title>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin:0; padding:0; font-family:'Plus Jakarta Sans', sans-serif; }}
body {{ background:#0B0F19; color:#F8FAFC; padding:40px 16px; display:flex; justify-content:center; }}
.container {{ max-width:900px; width:100%; }}
h1 {{ text-align:center; margin-bottom:12px; font-size:26px; color:#38BDF8; }}
h2 {{ text-align:center; margin-top:32px; margin-bottom:14px; font-size:20px; color:#34D399; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(260px, 1fr)); gap:16px; margin-top:16px; }}
.applied {{ background:rgba(16,185,129,0.15); border:1px solid #10B981; border-radius:12px; padding:16px; margin-bottom:24px; text-align:center; }}
</style>
</head>
<body>
<div class="container">
    <div class="applied">
        <span style="color:#34D399; font-weight:bold; font-size:16px;">✅ 1er Son appliqué : صُبِ (Ṣou-Bi — Hedi)</span>
    </div>

    <h1>🎯 Leçon 30 — Choix pour le 2ème Son</h1>
    <p style="text-align:center; color:#94A3B8; margin-bottom:24px;">Voici les options pour corriger ou remplacer le son 2 (avec la lettre <strong>Ḍād / ض</strong>) :</p>
    
    <h2>Option A : Conserver « Ḍou-Ri » (ضُرِ) avec une voix plus nette</h2>
    <div class="grid">
        {''.join(cards_duri)}
    </div>

    <h2>Option B : Remplacer par une syllabe plus naturelle (ex: Ḍou-Bi ضُبِ ou Ḍou-Mi ضُمِ)</h2>
    <div class="grid">
        {''.join(cards_alt)}
    </div>
</div>
</body>
</html>
"""
    with open('test_lesson30_son2.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated test_lesson30_son2.html successfully!')

if __name__ == '__main__':
    asyncio.run(main())
