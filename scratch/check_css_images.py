import os
import re
import urllib.parse

def main():
    root_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    css_path = os.path.join(root_dir, "styles.css")
    
    if not os.path.exists(css_path):
        print("styles.css not found!")
        return
        
    with open(css_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    # Find all url(...) patterns in css
    url_pat = re.compile(r'url\s*\(\s*["\']?([^"\'\)]+)["\']?\s*\)', re.IGNORECASE)
    matches = url_pat.findall(content)
    
    print(f"Found {len(matches)} URL references in styles.css:")
    broken_count = 0
    for match in matches:
        if match.startswith('http://') or match.startswith('https://') or match.startswith('//') or match.startswith('data:'):
            continue
            
        clean_src = match.split('?')[0].split('#')[0]
        clean_src = urllib.parse.unquote(clean_src)
        clean_src = clean_src.replace('/', os.sep)
        
        img_path = os.path.join(root_dir, clean_src)
        exists = os.path.exists(img_path)
        status = "OK" if exists else "BROKEN"
        print(f"  Url: {match} -> Resolves to: {clean_src} [{status}]")
        if not exists:
            broken_count += 1
            
    print(f"\nFound {broken_count} broken references in CSS.")

if __name__ == "__main__":
    main()
