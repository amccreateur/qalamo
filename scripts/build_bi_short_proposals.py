import asyncio
import os
import subprocess
import edge_tts
import base64

async def main():
    temp_dir = 'scripts/temp_audio/bi_short_tests'
    os.makedirs(temp_dir, exist_ok=True)
    
    # 1. Proposals for SHORT "Bi" (بِ - 1 harakah, rapide et net)
    short_proposals = [
        ('bi_moaz_fast', 'Moaz — « Bi » Ultra Court (+30%)', 'ar-QA-MoazNeural', 'بِ', '+30%'),
        ('bi_hamed_fast', 'Hamed — « Bi » Ultra Court (+30%)', 'ar-SA-HamedNeural', 'بِ', '+30%'),
        ('bi_hedi_fast', 'Hedi — « Bi » Ultra Court (+30%)', 'ar-TN-HediNeural', 'بِ', '+30%'),
        ('bi_shakir_fast', 'Shakir — « Bi » Ultra Court (+30%)', 'ar-EG-ShakirNeural', 'بِ', '+30%'),

        ('bi_moaz_medium', 'Moaz — « Bi » Court (+15%)', 'ar-QA-MoazNeural', 'بِ', '+15%'),
        ('bi_hamed_medium', 'Hamed — « Bi » Court (+15%)', 'ar-SA-HamedNeural', 'بِ', '+15%'),
        ('bi_hedi_medium', 'Hedi — « Bi » Court (+15%)', 'ar-TN-HediNeural', 'بِ', '+15%'),
        ('bi_shakir_medium', 'Shakir — « Bi » Court (+15%)', 'ar-EG-ShakirNeural', 'بِ', '+15%'),
    ]

    # Reference Long "Bee" (بِي)
    ref_long = ('bee_ref', 'Référence LONG : « Bī » (بِي)', 'ar-TN-HediNeural', 'بِي', '-15%')
    
    # Generate reference long
    raw_l = f'{temp_dir}/{ref_long[0]}_raw.mp3'
    clean_l = f'{temp_dir}/{ref_long[0]}.mp3'
    comm_l = edge_tts.Communicate(ref_long[3], ref_long[2], rate=ref_long[4])
    await comm_l.save(raw_l)
    subprocess.run(['ffmpeg', '-y', '-i', raw_l, '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,volume=6dB,alimiter=limit=0.95', clean_l], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with open(clean_l, 'rb') as f:
        b64_long = base64.b64encode(f.read()).decode('utf-8')

    cards = []
    for cid, title, voice, text, rate in short_proposals:
        craw = f'{temp_dir}/{cid}_raw.mp3'
        cclean = f'{temp_dir}/{cid}.mp3'
        c_comm = edge_tts.Communicate(text, voice, rate=rate)
        await c_comm.save(craw)
        subprocess.run(['ffmpeg', '-y', '-i', craw, '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,volume=6dB,alimiter=limit=0.95', cclean], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        with open(cclean, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        
        cards.append(f"""
        <div style="background:#151C2C; border:1.5px solid #2A364F; border-radius:16px; padding:18px; text-align:center; display:flex; flex-direction:column; gap:10px;">
            <div style="font-family:'Amiri',serif; font-size:46px; color:#38BDF8;">{text}</div>
            <div style="font-weight:800; color:#FFFFFF; font-size:14px;">{title}</div>
            <button style="background:#0284C7; border:none; color:#FFFFFF; font-weight:800; padding:10px 16px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64}').play()">▶ Écouter « Bi » COURT</button>
        </div>
        """)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Correction : Leçon 39 — Son 1 (Court « Bi » vs Long « Bī »)</title>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin:0; padding:0; font-family:'Plus Jakarta Sans', sans-serif; }}
body {{ background:#0B0F19; color:#F8FAFC; padding:40px 16px; display:flex; justify-content:center; }}
.container {{ max-width:960px; width:100%; }}
h1 {{ text-align:center; margin-bottom:12px; font-size:26px; color:#38BDF8; }}
p {{ text-align:center; color:#94A3B8; margin-bottom:24px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(270px, 1fr)); gap:16px; margin-top:16px; }}
.ref-box {{ background:rgba(236,72,153,0.15); border:1.5px solid #EC4899; border-radius:16px; padding:20px; text-align:center; margin-bottom:28px; }}
</style>
</head>
<body>
<div class="container">
    <div class="ref-box">
        <div style="font-family:'Amiri',serif; font-size:46px; color:#F472B6;">بِي</div>
        <div style="font-weight:800; color:#FFFFFF; font-size:16px; margin-bottom:10px;">Son LONG (Madd - 2 temps) pour comparaison :</div>
        <button style="background:#EC4899; border:none; color:#FFFFFF; font-weight:800; padding:10px 20px; border-radius:10px; cursor:pointer; font-size:14px;" onclick="new Audio('data:audio/mp3;base64,{b64_long}').play()">▶ Écouter « Bī » LONG (بِي)</button>
    </div>

    <h1>🎯 Leçon 39 — Choix du Son COURT : « Bi » (بِ)</h1>
    <p>Écoutez les versions courtes ci-dessous pour choisir celle qui contraste parfaitement avec le son long :</p>
    
    <div class="grid">
        {''.join(cards)}
    </div>
</div>
</body>
</html>
"""
    with open('test_bi_short.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('Generated test_bi_short.html successfully!')

if __name__ == '__main__':
    asyncio.run(main())
