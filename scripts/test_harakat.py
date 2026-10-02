import asyncio
import os
import sys
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

async def main():
    voice = 'ar-QA-MoazNeural'
    # Test cases
    test_cases = [
        ('verb_kataba', 'كَتَبَـ'),
        ('verb_kataba_std', 'كَتَبَ'),
        ('noun_kitabun', 'كِتَابٌ'),
        ('noun_kitaban', 'كِتَابًا'),
        ('noun_kitabin', 'كِتَابٍ'),
        ('phrase_1', 'قَرَأَ الوَلَدُ الكِتَابَ'),
        ('phrase_2', 'قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا'),
        ('phrase_3', 'ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ'),
        ('phrase_4', 'أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً'),
    ]

    for label, text in test_cases:
        fname = f"test_{label}.mp3"
        comm = edge_tts.Communicate(text, voice, rate='-15%')
        await comm.save(fname)
        print(f"Generated {fname} ({text}) - size: {os.path.getsize(fname)} bytes")

if __name__ == '__main__':
    asyncio.run(main())
