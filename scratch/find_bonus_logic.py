import os

def main():
    root_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    files_to_search = [
        "generate_individual_product_pages.py",
        "generate_catalog_page.py",
        "cart.js",
        "payment-success.html",
        "access.html"
    ]
    
    for filename in files_to_search:
        filepath = os.path.join(root_dir, filename)
        if not os.path.exists(filepath):
            continue
        print(f"File: {filename}")
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Search for occurrences of bonus
        lines = content.splitlines()
        count = 0
        for idx, line in enumerate(lines):
            if "bonus" in line.lower() or "free" in line.lower():
                # Print a few lines around it
                print(f"  Line {idx+1}: {line.strip()[:100]}")
                count += 1
                if count >= 15:
                    print("  ... too many occurrences ...")
                    break
        print("-" * 50)

if __name__ == "__main__":
    main()
