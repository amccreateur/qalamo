import asyncio
import os
import sys
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

async def main():
    voices = {
        'hamed': 'ar-SA-HamedNeural',
        'fahed': 'ar-KW-FahedNeural',
        'shakir': 'ar-EG-ShakirNeural',
        'moaz': 'ar-QA-MoazNeural',
    }

    texts = [
        ('najm_std', 'نَجْمٌ'),
        ('najm_anchor', 'نَجْمٌـ'),
        ('najm_wasl', 'نَجْمٌ كَبِيرٌ'),
        ('an_najm_std', 'النَّجْمُ'),
        ('an_najm_anchor', 'النَّجْمُـ'),
    ]

    for vname, vcode in voices.items():
        for tname, text in texts:
            fname = f"test_najm_{vname}_{tname}.mp3"
            try:
                comm = edge_tts.Communicate(text, vcode, rate='-15%')
                await comm.save(fname)
                print(f"Generated {fname} ({text}) - voice: {vname}")
            except Exception as e:
                print(f"Error {fname}: {e}")

if __name__ == '__main__':
    asyncio.run(main())

