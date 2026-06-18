import re

with open("c:/Users/aditya tiwari/Downloads/FUTUREWITHAI WEB/google-apps-script.gs", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "deliver" in line.lower() or "action" in line.lower() or "dopost" in line.lower():
        print(f"Line {i+1}: {line.strip()}")
