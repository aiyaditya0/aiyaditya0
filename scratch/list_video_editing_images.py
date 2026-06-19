import os
import re
import urllib.parse

def check_case_sensitive_path(base_dir, relative_path):
    # Split the path into parts
    parts = relative_path.replace('\\', '/').split('/')
    current_dir = base_dir
    
    for part in parts:
        if not part:
            continue
        # List all items in current_dir
        try:
            items = os.listdir(current_dir)
        except Exception:
            return False, f"Could not list directory: {current_dir}"
            
        # Find case-sensitive match
        matched = False
        for item in items:
            if item == part:
                current_dir = os.path.join(current_dir, item)
                matched = True
                break
                
        if not matched:
            # Check if a case-insensitive match exists to identify the discrepancy
            ci_match = None
            for item in items:
                if item.lower() == part.lower():
                    ci_match = item
                    break
            if ci_match:
                return False, f"Case mismatch: '{part}' on disk is '{ci_match}' under '{current_dir}'"
            else:
                return False, f"Not found: '{part}' under '{current_dir}'"
                
    return True, "OK"

def main():
    root_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    filepath = os.path.join(root_dir, "video-editing.html")
    
    if not os.path.exists(filepath):
        print("video-editing.html not found!")
        return
        
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    img_tags = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    print(f"Found {len(img_tags)} images in video-editing.html. Verifying case-sensitivity:")
    
    mismatches = 0
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
            mismatches += 1
            print(f"  #{idx+1}: {src}")
            print(f"    Error: {msg}")
            
    print(f"\nVerification complete. Found {mismatches} case-sensitivity issues.")

if __name__ == "__main__":
    main()
