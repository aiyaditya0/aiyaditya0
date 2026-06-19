import os

def main():
    index_path = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\index.html"
    if not os.path.exists(index_path):
        print("index.html not found!")
        return
        
    with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    print("Checking placeholder comments in index.html:")
    for tag in ["DYNAMIC", "PRODUCTS", "INDIVIDUAL", "START", "END"]:
        count = content.count(tag)
        print(f"  Word '{tag}' occurs {count} times")
        
    # Print lines around "products-grid"
    lines = content.splitlines()
    grid_idx = -1
    for idx, line in enumerate(lines):
        if 'id="products-grid"' in line:
            grid_idx = idx
            break
            
    if grid_idx != -1:
        print(f"\nLines {grid_idx-5} to {grid_idx+15} in index.html:")
        for idx in range(max(0, grid_idx-5), min(len(lines), grid_idx+15)):
            print(f"{idx+1}: {lines[idx]}")
    else:
        print("Could not find id=\"products-grid\" in index.html")

if __name__ == "__main__":
    main()
