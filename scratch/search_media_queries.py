with open("c:/Users/aditya tiwari/Downloads/FUTUREWITHAI WEB/styles.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(2200, len(lines)):
    line = lines[i]
    if "cart" in line.lower() or "img" in line.lower() or "flex" in line.lower():
        clean_line = line.strip().encode("ascii", "ignore").decode("ascii")
        print(f"Line {i+1}: {clean_line}")
