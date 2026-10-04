import asyncio
import os
import subprocess
import edge_tts
import base64

async def main():
    temp_dir = 'scripts/temp_audio/lesson40_son5'
    os.makedirs(temp_dir, exist_ok=True)
    
    # Proposals for Sound 5 of Lesson 40: hassa (حَسَّ) and alternatives with Shaddah
    proposals = [
        # hassa (حَسَّ) variations
        ('hassa_hedi', '« Ḥassa » (حَسَّ) — Hedi', 'ar-TN-HediNeural', 'حَسَّ', '-15%'),
        ('hassa_moaz', '« Ḥassa » (حَسَّ) — Moaz', 'ar-QA-MoazNeural', 'حَسَّ', '-15%'),
        ('hassa_hamed', '« Ḥassa » (حَسَّ) — Hamed', 'ar-SA-HamedNeural', 'حَسَّ', '-15%'),
        ('hassa_shakir', '« Ḥassa » (حَسَّ) — Shakir', 'ar-EG-ShakirNeural', 'حَسَّ', '-15%'),
        
        # Alternatives with Shaddah
        ('adda_hedi', 'Alternative : « ‘Adda » (عَدَّ) — Hedi', 'ar-TN-HediNeural', 'عَدَّ', '-15%'),
        ('adda_moaz', 'Alternative : « ‘Adda » (عَدَّ) — Moaz', 'ar-QA-MoazNeural', 'عَدَّ', '-15%'),
        ('haqqa_hedi', 'Alternative : « Ḥaqqa » (حَقَّ) — Hedi', 'ar-TN-HediNeural', 'حَقَّ', '-15%'),
        ('marra_hedi', 'Alternative : « Marra » (مَرَّ) — Hedi', 'ar-TN-HediNeural', 'مَرَّ', '-15%'),
        ('dalla_hedi', 'Alternative : « Dalla » (دَلَّ) — Hedi', 'ar-TN-HediNeural', 'دَلَّ', '-15%'),
        ('zhanna_hedi', 'Alternative : « Ẓanna » (ظَنَّ) — Hedi', 'ar-TN-HediNeural', 'ظَنَّ', '-15%'),
    ]

    cards_hassa = []
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
            <div style="font-family:'Amiri',serif; font-size:46px; color:#F43F5E;">{text}</div>
            <div style="font-weight:800; color:#FFFFFF; font-size:14px;">{title}</div>
            <button style="background:#E11D48; border:none; color:#FFFFFF; font-weight:800; padding:10px 16px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64}').play()">▶ Écouter « {text} »</button>
        </div>
        """
        if 'حَسَّ' in text:
            cards_hassa.append(card_html)
        else:
            cards_alt.append(card_html)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Comparaison : Leçon 40 — Son 5/6 (Shaddah : حَسَّ / Alternatives)</title>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin:0; padding:0; font-family:'Plus Jakarta Sans', sans-serif; }}
body {{ background:#0B0F19; color:#F8FAFC; padding:40px 16px; display:flex; justify-content:center; }}
.container {{ max-width:960px; width:100%; }}
h1 {{ text-align:center; margin-bottom:12px; font-size:26px; color:#F43F5E; }}
h2 {{ text-align:center; margin-top:32px; margin-bottom:14px; font-size:20px; color:#FB7185; }}
p {{ text-align:center; color:#94A3B8; margin-bottom:24px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(270px, 1fr)); gap:16px; margin-top:16px; }}
</style>
</head>
<body>
<div class="container">
    <h1>🎯 Leçon 40 — Choix pour le Son 5/6 (La Shaddah : ّ )</h1>
    <p>Écoutez les versions pour corriger <strong>حَسَّ (Ḥassa)</strong> ou le remplacer par un mot avec Shaddah très distinct :</p>
    
    <h2>Option A : Prononciations de « Ḥassa » (حَسَّ)</h2>
    <div class="grid">
        {''.join(cards_hassa)}
    </div>

    <h2>Option B : Alternatives courantes avec Shaddah (عَدَّ ، حَقَّ ، مَرَّ ، دَلَّ ، ظَنَّ)</h2>
    <div class="grid">
        {''.join(cards_alt)}
    </div>
</div>
</body>
</html>
"""
    with open('test_lesson40_son5.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated test_lesson40_son5.html successfully!')

if __name__ == '__main__':
    asyncio.run(main())
