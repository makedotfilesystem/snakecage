import subprocess
import os
import sys

directory_path = "plugins"

files = [f for f in os.listdir(directory_path) if f.endswith((".py", ".sh"))]

if not files:
    print("No plugins found.")
    exit()

for i, f in enumerate(files, start=1):
    print(f"{i}. {f}")

try:
    choice = int(input("Enter plugin number to execute: ")) - 1
    if choice < 0 or choice >= len(files):
        raise ValueError
except ValueError:
    print("Invalid selection.")
    exit()

selected = os.path.join(directory_path, files[choice])
print(f"Running plugin: {selected}\n")

if selected.endswith(".py"):
    cmd = [sys.executable, "-u", selected]
else:
    cmd = [selected]

with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1) as process:
    for line in process.stdout:
        print(line, end='')

process.wait()
print(f"\nPlugin finished with exit code {process.returncode}")
