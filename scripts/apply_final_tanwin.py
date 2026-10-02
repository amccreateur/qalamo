import asyncio
import os
import sys
import subprocess
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('assets/audio/generated', exist_ok=True)

# Using the exact proven formula:
# -an: standard Alif Tanwin ('كِتَابًا')
# -oun: 'كِتَابُ نْ' (Hamed)
# -in: 'كِتَابِ نْ' (Hamed)
tanwin_list = [
    # Kitab
    ('kitaban.mp3', 'كِتَابًا', 'ar-SA-HamedNeural'),
    ('kitabun.mp3', 'كِتَابُ نْ', 'ar-SA-HamedNeural'),
    ('kitabin.mp3', 'كِتَابِ نْ', 'ar-SA-HamedNeural'),
    # Walad
    ('waladan.mp3', 'وَلَدًا', 'ar-SA-HamedNeural'),
    ('waladun.mp3', 'وَلَدُ نْ', 'ar-SA-HamedNeural'),
    ('waladin.mp3', 'وَلَدِ نْ', 'ar-SA-HamedNeural'),
    # Bayt
    ('baytan.mp3', 'بَيْتًا', 'ar-SA-HamedNeural'),
    ('baytun.mp3', 'بَيْتُ نْ', 'ar-SA-HamedNeural'),
    ('baytin.mp3', 'بَيْتِ نْ', 'ar-SA-HamedNeural'),
    # Base Sukun words
    ('kitab.mp3', 'كِتَابْ', 'ar-SA-HamedNeural'),
    ('walad.mp3', 'وَلَدْ', 'ar-SA-HamedNeural'),
    ('bayt.mp3', 'بَيْتْ', 'ar-SA-HamedNeural'),
]

async def main():
    for fn, text, voice in tanwin_list:
        raw_path = f'raw_tw_{fn}'
        final_path = os.path.join('assets/audio/generated', fn)

        comm = edge_tts.Communicate(text, voice, rate='-10%')
        await comm.save(raw_path)

        # Trim leading silence for 0ms instant playback
        cmd = [
            'ffmpeg', '-y', '-i', raw_path,
            '-af', 'silenceremove=start_periods=1:start_duration=0.01:start_threshold=-35dB',
            final_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        if os.path.exists(raw_path):
            os.remove(raw_path)

        print(f'Generated: {final_path} from "{text}" ({voice})')

if __name__ == '__main__':
    asyncio.run(main())

