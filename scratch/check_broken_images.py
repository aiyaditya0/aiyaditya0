import os
import re
import urllib.parse

def main():
    root_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    # Get all html files
    html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]
    
    print(f"Checking images in {len(html_files)} HTML files using regex...\n")
    
    all_referenced_images = {}
    
    # Regex to find src="..." or content="..." inside meta tags
    # Focus on relative links and our site's canonical domain
    img_src_pat = re.compile(r'src=["\']([^"\']+\.(?:webp|png|jpg|jpeg|gif|svg))["\']', re.IGNORECASE)
    meta_img_pat = re.compile(r'<meta\s+[^>]*?(?:property|name)=["\'](?:og:image|twitter:image)["\'][^>]*?content=["\']([^"\']+)["\']', re.IGNORECASE)
    meta_img_pat2 = re.compile(r'<meta\s+[^>]*?content=["\']([^"\']+)["\'][^>]*?(?:property|name)=["\'](?:og:image|twitter:image)["\']', re.IGNORECASE)
    
    for filename in html_files:
        filepath = os.path.join(root_dir, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Find matches for src
        src_matches = img_src_pat.findall(content)
        # Find matches for meta images
        meta_matches = meta_img_pat.findall(content) + meta_img_pat2.findall(content)
        
        all_matches = src_matches + meta_matches
        
        for src in all_matches:
            if src.startswith('http://') or src.startswith('https://') or src.startswith('//'):
                # Check if it's our website domain
                if "futurewithai.anshumanenterprises.online" in src:
                    local_part = src.replace("https://futurewithai.anshumanenterprises.online/", "")
                    if local_part.startswith("http"):
                        continue
                    clean_src = local_part.split('?')[0].split('#')[0]
                else:
                    continue
            else:
                clean_src = src.split('?')[0].split('#')[0]
            
            # URL Decode the path (e.g. %20 -> space)
            clean_src = urllib.parse.unquote(clean_src)
            
            # Normalize path slashes for Windows
            clean_src = clean_src.replace('/', os.sep)
            img_path = os.path.join(root_dir, clean_src)
            exists = os.path.exists(img_path)
            
            if clean_src not in all_referenced_images:
                all_referenced_images[clean_src] = []
            all_referenced_images[clean_src].append((filename, exists))

    # Print results
    print("Image Status Summary:")
    broken_count = 0
    for img_src, refs in all_referenced_images.items():
        exists = refs[0][1]
        status = "OK" if exists else "BROKEN"
        if not exists:
            broken_count += 1
            print(f"Image: {img_src} - {status}")
            for ref_file, _ in refs:
                print(f"  Referenced in: {ref_file}")
    
    if broken_count == 0:
        print("All local images exist on disk!")
    else:
        print(f"\nFound {broken_count} broken image references.")

if __name__ == "__main__":
    main()
