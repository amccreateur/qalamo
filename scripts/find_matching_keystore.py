import subprocess
import glob
import os

target_sha1 = "08:73:AB:7F:63:84:22:BE:D5:82:4C:94:39:3C:A5:F8:45:13:8C:EE".replace(":", "").lower()
print(f"Target SHA1: {target_sha1}")

keystores = []
for root, dirs, files in os.walk("D:\\Dialectal"):
    if "node_modules" in root or ".gradle" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith(".jks") or f.endswith(".keystore"):
            keystores.append(os.path.join(root, f))

for root, dirs, files in os.walk("C:\\Users\\madan"):
    if "node_modules" in root or ".gradle" in root or ".git" in root or "AppData" in root:
        continue
    for f in files:
        if f.endswith(".jks") or f.endswith(".keystore"):
            keystores.append(os.path.join(root, f))

print(f"Found {len(keystores)} keystores to test.")

passwords = ["android", "123456", "password", "dialectal", "qalamo", "amccreateur"]

for ks in keystores:
    print(f"\nChecking: {ks}")
    found = False
    for pwd in passwords:
        try:
            res = subprocess.run(["keytool", "-list", "-v", "-keystore", ks, "-storepass", pwd], capture_output=True, text=True)
            if res.returncode == 0:
                out = res.stdout
                for line in out.splitlines():
                    if "SHA1:" in line:
                        sha = line.split("SHA1:")[1].strip().replace(":", "").lower()
                        print(f"  PWD '{pwd}' -> SHA1: {sha}")
                        if sha == target_sha1:
                            print(f"  🔥🔥🔥 MATCH FOUND! KeyStore: {ks}, Password: {pwd}")
                            found = True
                if found:
                    break
        except Exception as e:
            pass
