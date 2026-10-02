import asyncio
import os
import sys
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('assets/audio/generated', exist_ok=True)

# Using Hamed classical voice with explicit Tanwin vocalization so that -an, -un, -in are 100% audible
tanwin_items = [
    # Kitab
    ('kitaban.mp3', 'كِتَابَنْ', 'ar-SA-HamedNeural'),
    ('kitabun.mp3', 'كِتَابُنْ', 'ar-SA-HamedNeural'),
    ('kitabin.mp3', 'كِتَابِنْ', 'ar-SA-HamedNeural'),
    # Walad
    ('waladan.mp3', 'وَلَدَنْ', 'ar-SA-HamedNeural'),
    ('waladun.mp3', 'وَلَدُنْ', 'ar-SA-HamedNeural'),
    ('waladin.mp3', 'وَلَدِنْ', 'ar-SA-HamedNeural'),
    # Bayt
    ('baytan.mp3', 'بَيْتَنْ', 'ar-SA-HamedNeural'),
    ('baytun.mp3', 'بَيْتُنْ', 'ar-SA-HamedNeural'),
    ('baytin.mp3', 'بَيْتِنْ', 'ar-SA-HamedNeural'),
    # Kitab alone (for distractor without tanwin)
    ('kitab.mp3', 'كِتَابْ', 'ar-SA-HamedNeural'),
    # Walad alone (for distractor without tanwin)
    ('walad.mp3', 'وَلَدْ', 'ar-SA-HamedNeural'),
    # Bayt alone (for distractor without tanwin)
    ('bayt.mp3', 'بَيْتْ', 'ar-SA-HamedNeural'),
]

async def main():
    for fn, text, voice in tanwin_items:
        path = os.path.join('assets/audio/generated', fn)
        comm = edge_tts.Communicate(text, voice, rate='-15%')
        await comm.save(path)
        print(f'Successfully generated {path} with {voice} ({text})')

if __name__ == '__main__':
    asyncio.run(main())

