import asyncio
import os
import subprocess
import edge_tts
import base64

async def main():
    temp_dir = 'scripts/temp_audio/lesson33_son6'
    os.makedirs(temp_dir, exist_ok=True)
    
    # Proposals for Sound 6 of Lesson 33: an_sukun (عَنْ) and alternatives
    proposals = [
        # an_sukun (عَنْ) across voices
        ('an_hedi', '« An » (عَنْ) — Hedi', 'ar-TN-HediNeural', 'عَنْ', '-15%'),
        ('an_moaz', '« An » (عَنْ) — Moaz', 'ar-QA-MoazNeural', 'عَنْ', '-15%'),
        ('an_hamed', '« An » (عَنْ) — Hamed', 'ar-SA-HamedNeural', 'عَنْ', '-15%'),
        ('an_shakir', '« An » (عَنْ) — Shakir', 'ar-EG-ShakirNeural', 'عَنْ', '-15%'),
        
        # Alternatives with Sukun
        ('man_hedi', 'Alternative : « Man » (مَنْ) — Hedi', 'ar-TN-HediNeural', 'مَنْ', '-15%'),
        ('man_moaz', 'Alternative : « Man » (مَنْ) — Moaz', 'ar-QA-MoazNeural', 'مَنْ', '-15%'),
        ('in_hedi', 'Alternative : « In » (إِنْ) — Hedi', 'ar-TN-HediNeural', 'إِنْ', '-15%'),
        ('in_moaz', 'Alternative : « In » (إِنْ) — Moaz', 'ar-QA-MoazNeural', 'إِنْ', '-15%'),
        ('qad_hedi', 'Alternative : « Qad » (قَدْ) — Hedi', 'ar-TN-HediNeural', 'قَدْ', '-15%'),
        ('lam_hedi', 'Alternative : « Lam » (لَمْ) — Hedi', 'ar-TN-HediNeural', 'لَمْ', '-15%'),
    ]

    cards_an = []
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
            <div style="font-family:'Amiri',serif; font-size:46px; color:#34D399;">{text}</div>
            <div style="font-weight:800; color:#FFFFFF; font-size:14px;">{title}</div>
            <button style="background:#10B981; border:none; color:#FFFFFF; font-weight:800; padding:10px 16px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64}').play()">▶ Écouter « {text} »</button>
        </div>
        """
        if 'عَنْ' in text:
            cards_an.append(card_html)
        else:
            cards_alt.append(card_html)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Comparaison : Leçon 33 — Son 6/6 (عَنْ / Sukūn)</title>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin:0; padding:0; font-family:'Plus Jakarta Sans', sans-serif; }}
body {{ background:#0B0F19; color:#F8FAFC; padding:40px 16px; display:flex; justify-content:center; }}
.container {{ max-width:960px; width:100%; }}
h1 {{ text-align:center; margin-bottom:12px; font-size:26px; color:#34D399; }}
h2 {{ text-align:center; margin-top:32px; margin-bottom:14px; font-size:20px; color:#6EE7B7; }}
p {{ text-align:center; color:#94A3B8; margin-bottom:24px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(270px, 1fr)); gap:16px; margin-top:16px; }}
</style>
</head>
<body>
<div class="container">
    <h1>🎯 Leçon 33 — Choix pour le Son 6/6 (Sukūn : عَنْ)</h1>
    <p>Écoutez les versions pour corriger <strong>عَنْ (An — 'Ayn Fatha + Nūn Sukūn)</strong> ou le remplacer par une alternative :</p>
    
    <h2>Option A : Prononciations de « An » (عَنْ)</h2>
    <div class="grid">
        {''.join(cards_an)}
    </div>

    <h2>Option B : Alternatives courantes avec Sukūn (مَنْ ، إِنْ ، قَدْ ، لَمْ)</h2>
    <div class="grid">
        {''.join(cards_alt)}
    </div>
</div>
</body>
</html>
"""
    with open('test_lesson33_son6.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated test_lesson33_son6.html successfully!')

if __name__ == '__main__':
    asyncio.run(main())
