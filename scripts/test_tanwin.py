import asyncio
import os
import sys
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

async def test():
    voices = ['ar-QA-MoazNeural', 'ar-SA-HamedNeural', 'ar-SA-ZariyahNeural', 'ar-EG-ShakirNeural']
    words = [
        ('kitabun_std', 'كِتَابٌ'),
        ('kitabun_tatweel', 'كِتَابٌـ'),
        ('kitabun_wasl', 'كِتَابٌ وَ'),
        ('kitaban_std', 'كِتَابًا'),
        ('kitabin_std', 'كِتَابٍ'),
        ('kitabin_tatweel', 'كِتَابٍـ'),
    ]
    for v in voices:
        v_short = v.split('-')[2].replace('Neural','')
        for name, text in words:
            fn = f'test_{v_short}_{name}.mp3'
            comm = edge_tts.Communicate(text, v, rate='-15%')
            await comm.save(fn)
            print(f'Generated {fn}')

asyncio.run(test())

