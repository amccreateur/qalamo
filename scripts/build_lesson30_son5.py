import asyncio
import os
import subprocess
import edge_tts
import base64

async def main():
    os.makedirs('assets/audio/generated', exist_ok=True)
    temp_dir = 'scripts/temp_audio/lesson30_son5'
    os.makedirs(temp_dir, exist_ok=True)
    
    # 1. Generate dubi (ضُبِ) with Moaz for Sound 2
    raw_dubi = 'scripts/temp_audio/lesson30_proposals/moaz_dubi_raw.mp3'
    clean_dubi = 'assets/audio/generated/dubi.mp3'
    comm = edge_tts.Communicate('ضُبِ', 'ar-QA-MoazNeural', rate='-15%')
    await comm.save(raw_dubi)
    subprocess.run(['ffmpeg', '-y', '-i', raw_dubi, '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,volume=6dB,alimiter=limit=0.95', clean_dubi], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Also update duri_emph.mp3 as fallback
    subprocess.run(['ffmpeg', '-y', '-i', raw_dubi, '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,volume=6dB,alimiter=limit=0.95', 'assets/audio/generated/duri_emph.mp3'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print('Generated dubi.mp3 (Moaz) successfully!')

    # 2. Proposals for Sound 5: quri (قُرِ) and alternatives
    proposals = [
        ('quri_moaz', 'Qou-Ri (قُرِ) — Moaz', 'ar-QA-MoazNeural', 'قُرِ', '-15%'),
        ('quri_hamed', 'Qou-Ri (قُرِ) — Hamed', 'ar-SA-HamedNeural', 'قُرِ', '-15%'),
        ('quri_shakir', 'Qou-Ri (قُرِ) — Shakir', 'ar-EG-ShakirNeural', 'قُرِ', '-15%'),
        ('quri_hedi', 'Qou-Ri (قُرِ) — Hedi', 'ar-TN-HediNeural', 'قُرِ', '-15%'),
        
        # Alternatives with Qaf
        ('qubi_moaz', 'Qou-Bi (قُبِ) — Moaz', 'ar-QA-MoazNeural', 'قُبِ', '-15%'),
        ('qubi_hedi', 'Qou-Bi (قُبِ) — Hedi', 'ar-TN-HediNeural', 'قُبِ', '-15%'),
        ('quti_moaz', 'Qou-Ti (قُتِ) — Moaz', 'ar-QA-MoazNeural', 'قُتِ', '-15%'),
        ('quti_hedi', 'Qou-Ti (قُتِ) — Hedi', 'ar-TN-HediNeural', 'قُتِ', '-15%'),
        ('qumi_moaz', 'Qou-Mi (قُمِ) — Moaz', 'ar-QA-MoazNeural', 'قُمِ', '-15%'),
        ('qumi_hedi', 'Qou-Mi (قُمِ) — Hedi', 'ar-TN-HediNeural', 'قُمِ', '-15%'),
    ]

    cards_quri = []
    cards_alt = []

    for cid, title, voice, text, rate in proposals:
        craw = f'{temp_dir}/{cid}_raw.mp3'
        cclean = f'{temp_dir}/{cid}.mp3'
        c_comm = edge_tts.Communicate(text, voice, rate=rate)
        await c_comm.save(craw)
        subprocess.run(['ffmpeg', '-y', '-i', craw, '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,volume=6dB,alimiter=limit=0.95', cclean], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        with open(cclean, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        
        card_html = f"""
        <div style="background:#151C2C; border:1.5px solid #2A364F; border-radius:16px; padding:18px; text-align:center; display:flex; flex-direction:column; gap:10px;">
            <div style="font-family:'Amiri',serif; font-size:46px; color:#EC4899;">{text}</div>
            <div style="font-weight:800; color:#FFFFFF; font-size:14px;">{title}</div>
            <button style="background:#DB2777; border:none; color:#FFFFFF; font-weight:800; padding:10px 16px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64}').play()">▶ Écouter « {text} »</button>
        </div>
        """
        if 'Qou-Ri' in title:
            cards_quri.append(card_html)
        else:
            cards_alt.append(card_html)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Comparaison : Leçon 30 — 5ème Son (قُرِ / Alternatives)</title>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin:0; padding:0; font-family:'Plus Jakarta Sans', sans-serif; }}
body {{ background:#0B0F19; color:#F8FAFC; padding:40px 16px; display:flex; justify-content:center; }}
.container {{ max-width:960px; width:100%; }}
h1 {{ text-align:center; margin-bottom:12px; font-size:26px; color:#EC4899; }}
h2 {{ text-align:center; margin-top:32px; margin-bottom:14px; font-size:20px; color:#F472B6; }}
p {{ text-align:center; color:#94A3B8; margin-bottom:24px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(270px, 1fr)); gap:16px; margin-top:16px; }}
.badge {{ background:rgba(16,185,129,0.15); border:1px solid #10B981; border-radius:12px; padding:14px; margin-bottom:20px; text-align:center; color:#34D399; font-weight:bold; }}
</style>
</head>
<body>
<div class="container">
    <div class="badge">
        ✅ 1er Son : صُبِ (Ṣou-Bi — Hedi)<br>
        ✅ 2ème Son appliqué : ضُبِ (Ḍou-Bi — Moaz)
    </div>
    <h1>🎯 Leçon 30 — Choix pour le 5ème Son (Lettre Qāf / ق)</h1>
    <p>Écoutez les versions pour corriger ou remplacer le 5ème son :</p>
    
    <h2>Option A : Conserver « Qou-Ri » (قُرِ) avec une voix nette</h2>
    <div class="grid">
        {''.join(cards_quri)}
    </div>

    <h2>Option B : Alternatives fluides avec Qāf (قُبِ ، قُتِ ، قُمِ)</h2>
    <div class="grid">
        {''.join(cards_alt)}
    </div>
</div>
</body>
</html>
"""
    with open('test_lesson30_son5.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated test_lesson30_son5.html successfully!')

if __name__ == '__main__':
    asyncio.run(main())
