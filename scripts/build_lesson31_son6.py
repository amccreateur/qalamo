import asyncio
import os
import subprocess
import edge_tts
import base64

async def main():
    temp_dir = 'scripts/temp_audio/lesson31_son6'
    os.makedirs(temp_dir, exist_ok=True)
    
    # Proposals for Sound 6 of Lesson 31: ghila (غِلَ) and alternatives with Ghayn (غِ)
    proposals = [
        # ghila (غِلَ) variations
        ('ghila_hedi', 'Ghi-La (غِلَ) — Hedi', 'ar-TN-HediNeural', 'غِلَ', '-15%'),
        ('ghila_moaz', 'Ghi-La (غِلَ) — Moaz', 'ar-QA-MoazNeural', 'غِلَ', '-15%'),
        ('ghila_hamed', 'Ghi-La (غِلَ) — Hamed', 'ar-SA-HamedNeural', 'غِلَ', '-15%'),
        ('ghila_shakir', 'Ghi-La (غِلَ) — Shakir', 'ar-EG-ShakirNeural', 'غِلَ', '-15%'),
        
        # Alternatives with Ghayn Kasrah (غِ)
        ('ghiba_hedi', 'Ghi-Ba (غِبَ) — Hedi', 'ar-TN-HediNeural', 'غِبَ', '-15%'),
        ('ghiba_moaz', 'Ghi-Ba (غِبَ) — Moaz', 'ar-QA-MoazNeural', 'غِبَ', '-15%'),
        ('ghida_hedi', 'Ghi-Da (غِدَ) — Hedi', 'ar-TN-HediNeural', 'غِدَ', '-15%'),
        ('ghida_moaz', 'Ghi-Da (غِدَ) — Moaz', 'ar-QA-MoazNeural', 'غِدَ', '-15%'),
        ('ghita_hedi', 'Ghi-Ta (غِتَ) — Hedi', 'ar-TN-HediNeural', 'غِتَ', '-15%'),
        ('ghira_hedi', 'Ghi-Ra (غِرَ) — Hedi', 'ar-TN-HediNeural', 'غِرَ', '-15%'),
    ]

    cards_ghila = []
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
            <div style="font-family:'Amiri',serif; font-size:46px; color:#10B981;">{text}</div>
            <div style="font-weight:800; color:#FFFFFF; font-size:14px;">{title}</div>
            <button style="background:#059669; border:none; color:#FFFFFF; font-weight:800; padding:10px 16px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64}').play()">▶ Écouter « {text} »</button>
        </div>
        """
        if 'Ghi-La' in title:
            cards_ghila.append(card_html)
        else:
            cards_alt.append(card_html)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Comparaison : Leçon 31 — 6ème Son (غِلَ / Alternatives)</title>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin:0; padding:0; font-family:'Plus Jakarta Sans', sans-serif; }}
body {{ background:#0B0F19; color:#F8FAFC; padding:40px 16px; display:flex; justify-content:center; }}
.container {{ max-width:960px; width:100%; }}
h1 {{ text-align:center; margin-bottom:12px; font-size:26px; color:#10B981; }}
h2 {{ text-align:center; margin-top:32px; margin-bottom:14px; font-size:20px; color:#34D399; }}
p {{ text-align:center; color:#94A3B8; margin-bottom:24px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(270px, 1fr)); gap:16px; margin-top:16px; }}
</style>
</head>
<body>
<div class="container">
    <h1>🎯 Leçon 31 — Choix pour le 6ème Son (Lettre Ghayn Kasrah: غِـ)</h1>
    <p>Écoutez les versions pour corriger <strong>غِلَ (Ghi-La)</strong> ou le remplacer par une alternative plus naturelle :</p>
    
    <h2>Option A : Conserver « Ghi-La » (غِلَ) avec une voix nette</h2>
    <div class="grid">
        {''.join(cards_ghila)}
    </div>

    <h2>Option B : Alternatives fluides avec Ghayn (غِبَ ، غِدَ ، غِتَ ، غِرَ)</h2>
    <div class="grid">
        {''.join(cards_alt)}
    </div>
</div>
</body>
</html>
"""
    with open('test_lesson31_son6.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated test_lesson31_son6.html successfully!')

if __name__ == '__main__':
    asyncio.run(main())
