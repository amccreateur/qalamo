import asyncio
import os
import subprocess
import edge_tts
import base64

async def main():
    temp_dir = 'scripts/temp_audio/qaf_kasra_fix'
    os.makedirs(temp_dir, exist_ok=True)
    
    proposals = [
        # Qi-Ba (قِبَ)
        ('qiba_moaz', 'Qi-Ba (قِبَ) — Moaz (Qaf profond)', 'ar-QA-MoazNeural', 'قِبَ', '-15%'),
        ('qiba_hamed', 'Qi-Ba (قِبَ) — Hamed (Qaf saoudien)', 'ar-SA-HamedNeural', 'قِبَ', '-15%'),
        ('qiba_shakir', 'Qi-Ba (قِبَ) — Shakir (Qaf égyptien)', 'ar-EG-ShakirNeural', 'قِبَ', '-15%'),
        ('qiba_hedi', 'Qi-Ba (قِبَ) — Hedi (Tunisien)', 'ar-TN-HediNeural', 'قِبَ', '-15%'),
        
        # Qi-Ta (قِتَ)
        ('qita_moaz', 'Qi-Ta (قِتَ) — Moaz', 'ar-QA-MoazNeural', 'قِتَ', '-15%'),
        ('qita_hamed', 'Qi-Ta (قِتَ) — Hamed', 'ar-SA-HamedNeural', 'قِتَ', '-15%'),
        ('qita_hedi', 'Qi-Ta (قِتَ) — Hedi', 'ar-TN-HediNeural', 'قِتَ', '-15%'),

        # Qi-Ma (قِمَ)
        ('qima_moaz', 'Qi-Ma (قِمَ) — Moaz', 'ar-QA-MoazNeural', 'قِمَ', '-15%'),
        ('qima_hamed', 'Qi-Ma (قِمَ) — Hamed', 'ar-SA-HamedNeural', 'قِمَ', '-15%'),
        ('qima_hedi', 'Qi-Ma (قِمَ) — Hedi', 'ar-TN-HediNeural', 'قِمَ', '-15%'),

        # Qi-Da (قِدَ)
        ('qida_moaz', 'Qi-Da (قِدَ) — Moaz', 'ar-QA-MoazNeural', 'قِدَ', '-15%'),
        ('qida_hedi', 'Qi-Da (قِدَ) — Hedi', 'ar-TN-HediNeural', 'قِدَ', '-15%'),
    ]

    cards_qiba = []
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
            <div style="font-family:'Amiri',serif; font-size:46px; color:#A78BFA;">{text}</div>
            <div style="font-weight:800; color:#FFFFFF; font-size:14px;">{title}</div>
            <button style="background:#8B5CF6; border:none; color:#FFFFFF; font-weight:800; padding:10px 16px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64}').play()">▶ Écouter « {text} »</button>
        </div>
        """
        if 'Qi-Ba' in title:
            cards_qiba.append(card_html)
        else:
            cards_alt.append(card_html)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Correction : Leçon 31 — 5/10 (Qāf Kasrah: قِـ)</title>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin:0; padding:0; font-family:'Plus Jakarta Sans', sans-serif; }}
body {{ background:#0B0F19; color:#F8FAFC; padding:40px 16px; display:flex; justify-content:center; }}
.container {{ max-width:960px; width:100%; }}
h1 {{ text-align:center; margin-bottom:12px; font-size:26px; color:#A78BFA; }}
h2 {{ text-align:center; margin-top:32px; margin-bottom:14px; font-size:20px; color:#34D399; }}
p {{ text-align:center; color:#94A3B8; margin-bottom:24px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(270px, 1fr)); gap:16px; margin-top:16px; }}
.badge {{ background:rgba(139,92,246,0.15); border:1px solid #8B5CF6; border-radius:12px; padding:14px; margin-bottom:20px; text-align:center; color:#C4B5FD; font-weight:bold; }}
</style>
</head>
<body>
<div class="container">
    <div class="badge">
        🎯 Objectif 5/10 : Un son Qāf (قِـ) profond, bien distinct du Kāf (كِـ)
    </div>
    <h1>Leçon 31 — Question 5/10</h1>
    <p>Écoutez les versions ci-dessous et dites-moi laquelle vous entendez le plus distinctement :</p>
    
    <h2>Option A : Prononciation de « Qi-Ba » (قِبَ) avec un Qaf profond</h2>
    <div class="grid">
        {''.join(cards_qiba)}
    </div>

    <h2>Option B : Alternatives (Qi-Ta قِتَ, Qi-Ma قِمَ, Qi-Da قِدَ)</h2>
    <div class="grid">
        {''.join(cards_alt)}
    </div>
</div>
</body>
</html>
"""
    with open('test_qaf_kasra_fix.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated test_qaf_kasra_fix.html successfully!')

if __name__ == '__main__':
    asyncio.run(main())
