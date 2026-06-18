with open("c:/Users/aditya tiwari/Downloads/FUTUREWITHAI WEB/styles.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "flex-direction" in line.lower() or "column" in line.lower():
        # Check if it is near cart-item or in media queries
        context = "".join(lines[max(0, i-4):min(len(lines), i+5)])
        if "cart" in context.lower():
            clean_line = line.strip().encode("ascii", "ignore").decode("ascii")
            print(f"Line {i+1}: {clean_line}")
            print(f"Context:\n{context.encode('ascii', 'ignore').decode('ascii')}\n")
