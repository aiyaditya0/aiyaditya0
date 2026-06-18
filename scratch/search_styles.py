with open("c:/Users/aditya tiwari/Downloads/FUTUREWITHAI WEB/styles.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "cart-item" in line.lower() or "cart-drawer" in line.lower():
        clean_line = line.strip().encode("ascii", "ignore").decode("ascii")
        print(f"styles.css Line {i+1}: {clean_line}")
