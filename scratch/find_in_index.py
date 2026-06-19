import os

def main():
    index_path = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\index.html"
    if not os.path.exists(index_path):
        print("index.html not found!")
        return
        
    with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        
    print(f"Total lines in index.html: {len(lines)}")
    matches = 0
    for idx, line in enumerate(lines):
        if "product-" in line:
            matches += 1
            print(f"Line {idx+1}: {line.strip()[:120]}")
            if matches >= 15:
                print("... truncated ...")
                break
                
    if matches == 0:
        print("No occurrences of 'product-' found.")

if __name__ == "__main__":
    main()
