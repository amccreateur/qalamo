import asyncio
import os
import sys
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

variations = [
    # 1. Phonetic elongation
    ('kitaboon_hamed', 'كِتَابُونْ', 'ar-SA-HamedNeural'),
    ('kitabeen_hamed', 'كِتَابِينْ', 'ar-SA-HamedNeural'),
    ('kitaboon_zariyah', 'كِتَابُونْ', 'ar-SA-ZariyahNeural'),
    ('kitabeen_zariyah', 'كِتَابِينْ', 'ar-SA-ZariyahNeural'),
    ('kitaboon_moaz', 'كِتَابُونْ', 'ar-QA-MoazNeural'),
    ('kitabeen_moaz', 'كِتَابِينْ', 'ar-QA-MoazNeural'),

    # 2. Syllabic concatenation
    ('kitabun_phonetic_hamed', 'كِتَابُنْ', 'ar-SA-HamedNeural'),
    ('kitabin_phonetic_hamed', 'كِتَابِنْ', 'ar-SA-HamedNeural'),
    ('kitabu_nun_hamed', 'كِتَابُ نْ', 'ar-SA-HamedNeural'),
    ('kitabi_nun_hamed', 'كِتَابِ نْ', 'ar-SA-HamedNeural'),

    # 3. Tanwin with soft carrier
    ('kitabun_ha_hamed', 'كِتَابٌ هْ', 'ar-SA-HamedNeural'),
    ('kitabin_ha_hamed', 'كِتَابٍ هْ', 'ar-SA-HamedNeural'),
]

async def main():
    os.makedirs('test_phonetic_variations', exist_ok=True)
    for name, text, voice in variations:
        fn = f'test_phonetic_variations/{name}.mp3'
        comm = edge_tts.Communicate(text, voice, rate='-10%')
        await comm.save(fn)
        print(f'Generated: {fn} for {text}')

if __name__ == '__main__':
    asyncio.run(main())
