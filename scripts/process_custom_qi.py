import subprocess
import os
import shutil

src_path = r"C:\Users\madan\Desktop\Qi.mpeg"
dst_path = r"assets\audio\generated\qaf_kasra.mp3"
temp_clean = r"scripts\temp_audio\custom_qi_clean.mp3"

os.makedirs("scripts/temp_audio", exist_ok=True)

# Process audio: trim head and tail silence, normalize volume
cmd = [
    "ffmpeg", "-y", "-i", src_path,
    "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,areverse,volume=2dB",
    temp_clean
]

subprocess.run(cmd, check=True)
shutil.copy2(temp_clean, dst_path)

print(f"Custom Qi processed and saved to {dst_path} successfully!")
