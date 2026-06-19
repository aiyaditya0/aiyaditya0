import os

def main():
    filepath = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\video-editing.html"
    if not os.path.exists(filepath):
        print("video-editing.html not found!")
        return
        
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    lines = content.splitlines()
    found = -1
    for idx, line in enumerate(lines):
        if 'class="bonuses-container"' in line and idx > 600:
            found = idx
            break
            
    if found != -1:
        print(f"Found bonuses-container at line {found+1}:")
        for i in range(found - 2, min(len(lines), found + 60)):
            clean_line = lines[i].strip().encode("ascii", "ignore").decode("ascii")
            print(f"{i+1}: {clean_line}")
    else:
        print("bonuses-container not found in HTML body")

if __name__ == "__main__":
    main()
