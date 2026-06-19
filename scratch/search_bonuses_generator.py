import os

def main():
    filepath = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\generate_individual_product_pages.py"
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    lines = content.splitlines()
    matches = 0
    for idx, line in enumerate(lines):
        if "bonus" in line.lower():
            matches += 1
            print(f"Line {idx+1}: {line.strip()[:100]}")
            if matches >= 30:
                print("... truncated ...")
                break
                
    if matches == 0:
        print("No matches for 'bonus' found in generate_individual_product_pages.py")

if __name__ == "__main__":
    main()
