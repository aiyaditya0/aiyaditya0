with open("c:/Users/aditya tiwari/Downloads/FUTUREWITHAI WEB/cart.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "img" in line.lower() or "cart" in line.lower() or "your cart" in line.lower():
        clean_line = line.strip().encode("ascii", "ignore").decode("ascii")
        print(f"Line {i+1}: {clean_line}")
