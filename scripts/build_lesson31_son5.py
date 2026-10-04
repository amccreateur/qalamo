import asyncio
import os
import subprocess
import edge_tts
import base64

async def main():
    temp_dir = 'scripts/temp_audio/lesson31_son5'
    os.makedirs(temp_dir, exist_ok=True)
    
    # Proposals for Sound 5 of Lesson 31: qifa (قِفَ) and alternatives
    proposals = [
        # qifa (قِفَ) variations
        ('qifa_hedi', 'Qi-Fa (قِفَ) — Hedi', 'ar-TN-HediNeural', 'قِفَ', '-15%'),
        ('qifa_moaz', 'Qi-Fa (قِفَ) — Moaz', 'ar-QA-MoazNeural', 'قِفَ', '-15%'),
        ('qifa_hamed', 'Qi-Fa (قِفَ) — Hamed', 'ar-SA-HamedNeural', 'قِفَ', '-15%'),
        ('qifa_shakir', 'Qi-Fa (قِفَ) — Shakir', 'ar-EG-ShakirNeural', 'قِفَ', '-15%'),
        
        # Alternatives in I + A with Qāf (ق)
        ('qiba_hedi', 'Qi-Ba (قِبَ) — Hedi', 'ar-TN-HediNeural', 'قِبَ', '-15%'),
        ('qiba_moaz', 'Qi-Ba (قِبَ) — Moaz', 'ar-QA-MoazNeural', 'قِبَ', '-15%'),
        ('qita_hedi', 'Qi-Ta (قِتَ) — Hedi', 'ar-TN-HediNeural', 'قِتَ', '-15%'),
        ('qita_moaz', 'Qi-Ta (قِتَ) — Moaz', 'ar-QA-MoazNeural', 'قِتَ', '-15%'),
        ('qima_hedi', 'Qi-Ma (قِمَ) — Hedi', 'ar-TN-HediNeural', 'قِمَ', '-15%'),
        ('qima_moaz', 'Qi-Ma (قِمَ) — Moaz', 'ar-QA-MoazNeural', 'قِمَ', '-15%'),
        ('qira_hedi', 'Qi-Ra (قِرَ) — Hedi', 'ar-TN-HediNeural', 'قِرَ', '-15%'),
        ('qida_hedi', 'Qi-Da (قِدَ) — Hedi', 'ar-TN-HediNeural', 'قِدَ', '-15%'),
    ]

    cards_qifa = []
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
            <div style="font-family:'Amiri',serif; font-size:46px; color:#38BDF8;">{text}</div>
            <div style="font-weight:800; color:#FFFFFF; font-size:14px;">{title}</div>
            <button style="background:#0284C7; border:none; color:#FFFFFF; font-weight:800; padding:10px 16px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64}').play()">▶ Écouter « {text} »</button>
        </div>
        """
        if 'Qi-Fa' in title:
            cards_qifa.append(card_html)
        else:
            cards_alt.append(card_html)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Comparaison : Leçon 31 — 5ème Son (قِفَ / Alternatives)</title>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin:0; padding:0; font-family:'Plus Jakarta Sans', sans-serif; }}
body {{ background:#0B0F19; color:#F8FAFC; padding:40px 16px; display:flex; justify-content:center; }}
.container {{ max-width:960px; width:100%; }}
h1 {{ text-align:center; margin-bottom:12px; font-size:26px; color:#38BDF8; }}
h2 {{ text-align:center; margin-top:32px; margin-bottom:14px; font-size:20px; color:#34D399; }}
p {{ text-align:center; color:#94A3B8; margin-bottom:24px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(270px, 1fr)); gap:16px; margin-top:16px; }}
</style>
</head>
<body>
<div class="container">
    <h1>🎯 Leçon 31 — Choix pour le 5ème Son (Lettre Qāf Kasrah: قِـ)</h1>
    <p>Écoutez les versions pour corriger <strong>قِفَ (Qi-Fa)</strong> ou le remplacer par une alternative plus naturelle :</p>
    
    <h2>Option A : Conserver « Qi-Fa » (قِفَ) avec une voix nette</h2>
    <div class="grid">
        {''.join(cards_qifa)}
    </div>

    <h2>Option B : Remplacer par une syllabe plus fluide (ex: Qi-Ba قِبَ, Qi-Ta قِتَ, Qi-Ma قِمَ)</h2>
    <div class="grid">
        {''.join(cards_alt)}
    </div>
</div>
</body>
</html>
"""
    with open('test_lesson31_son5.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated test_lesson31_son5.html successfully!')

if __name__ == '__main__':
    asyncio.run(main())
