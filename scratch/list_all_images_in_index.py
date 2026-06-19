import os
import re
import urllib.parse

def main():
    filepath = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\index.html"
    if not os.path.exists(filepath):
        print("index.html not found!")
        return
        
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    # Find all img tags using a very permissive regex
    img_tags = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    
    print(f"Found {len(img_tags)} img tags in index.html:")
    broken_count = 0
    for idx, src in enumerate(img_tags):
        # Resolve path
        if src.startswith('http://') or src.startswith('https://') or src.startswith('//'):
            # Check if it's our website domain
            if "futurewithai.anshumanenterprises.online" in src:
                local_part = src.replace("https://futurewithai.anshumanenterprises.online/", "")
                if local_part.startswith("http"):
                    print(f"  #{idx+1}: {src} [External Link]")
                    continue
                clean_src = local_part.split('?')[0].split('#')[0]
            else:
                print(f"  #{idx+1}: {src} [External Link]")
                continue
        else:
            clean_src = src.split('?')[0].split('#')[0]
            
        clean_src = urllib.parse.unquote(clean_src)
        clean_src = clean_src.replace('/', os.sep)
        
        img_path = os.path.join(r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB", clean_src)
        exists = os.path.exists(img_path)
        status = "OK" if exists else "BROKEN"
        print(f"  #{idx+1}: {src} -> Resolves to: {clean_src} [{status}]")
        if not exists:
            broken_count += 1
            
    print(f"\nFound {broken_count} broken images in index.html.")

if __name__ == "__main__":
    main()
