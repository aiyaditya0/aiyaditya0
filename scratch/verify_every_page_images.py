import os
import re
import urllib.parse

def check_case_sensitive_path(base_dir, relative_path):
    parts = relative_path.replace('\\', '/').split('/')
    current_dir = base_dir
    
    for part in parts:
        if not part:
            continue
        try:
            items = os.listdir(current_dir)
        except Exception:
            return False, f"Could not list directory: {current_dir}"
            
        matched = False
        for item in items:
            if item == part:
                current_dir = os.path.join(current_dir, item)
                matched = True
                break
                
        if not matched:
            ci_match = None
            for item in items:
                if item.lower() == part.lower():
                    ci_match = item
                    break
            if ci_match:
                return False, f"Case mismatch: '{part}' vs disk '{ci_match}' under '{current_dir}'"
            else:
                return False, f"Not found: '{part}' under '{current_dir}'"
                
    return True, "OK"

def main():
    root_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]
    
    print(f"Checking images in {len(html_files)} HTML files for case-sensitivity...\n")
    
    total_broken = 0
    for filename in sorted(html_files):
        filepath = os.path.join(root_dir, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        img_tags = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', content, re.IGNORECASE)
        
        page_broken = []
        for idx, src in enumerate(img_tags):
            if src.startswith('http://') or src.startswith('https://') or src.startswith('//'):
                if "futurewithai.anshumanenterprises.online" in src:
                    local_part = src.replace("https://futurewithai.anshumanenterprises.online/", "")
                    if local_part.startswith("http"):
                        continue
                    clean_src = local_part.split('?')[0].split('#')[0]
                else:
                    continue
            else:
                clean_src = src.split('?')[0].split('#')[0]
                
            clean_src = urllib.parse.unquote(clean_src)
            ok, msg = check_case_sensitive_path(root_dir, clean_src)
            if not ok:
                page_broken.append((src, msg))
                
        if page_broken:
            print(f"File: {filename} - {len(page_broken)} BROKEN IMAGES:")
            for src, msg in page_broken:
                print(f"  Src: {src}")
                print(f"    Error: {msg}")
            total_broken += len(page_broken)
            print("-" * 50)
            
    print(f"Completed verification. Total broken references: {total_broken}")

if __name__ == "__main__":
    main()
