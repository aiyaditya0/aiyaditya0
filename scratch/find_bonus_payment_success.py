import os

def main():
    filepath = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\payment-success.html"
    if not os.path.exists(filepath):
        print("payment-success.html not found!")
        return
        
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    lines = content.splitlines()
    for idx, line in enumerate(lines):
        if "bonus" in line.lower() or "free" in line.lower() or "whatsapp" in line.lower():
            if idx > 900:
                clean_line = line.strip().encode("ascii", "ignore").decode("ascii")
                print(f"Line {idx+1}: {clean_line}")
                
if __name__ == "__main__":
    main()
