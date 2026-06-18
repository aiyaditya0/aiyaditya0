import os
import json
from html.parser import HTMLParser

class SEOHTMLParser(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.in_json_ld = False
        self.json_ld_contents = []
        self.errors = []
        self.canonical_hrefs = []
        self.robots_contents = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'script' and attrs_dict.get('type') == 'application/ld+json':
            self.in_json_ld = True
            self.json_ld_contents.append("")
        elif tag == 'link' and attrs_dict.get('rel') == 'canonical':
            href = attrs_dict.get('href')
            if href:
                self.canonical_hrefs.append(href)
        elif tag == 'meta' and attrs_dict.get('name') == 'robots':
            content = attrs_dict.get('content')
            if content:
                self.robots_contents.append(content)

    def handle_data(self, data):
        if self.in_json_ld:
            self.json_ld_contents[-1] += data

    def handle_endtag(self, tag):
        if tag == 'script' and self.in_json_ld:
            self.in_json_ld = False

    def handle_error(self, message):
        self.errors.append(f"Parser error: {message}")

def verify_file(filepath):
    filename = os.path.basename(filepath)
    print(f"Verifying {filename}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parser = SEOHTMLParser(filename)
    try:
        parser.feed(content)
        parser.close()
    except Exception as e:
        print(f"  [ERROR] Parsing failed: {e}")
        return False

    success = True
    
    # 1. Check Parser Errors
    if parser.errors:
        for err in parser.errors:
            print(f"  [ERROR] {err}")
        success = False

    # 2. Check JSON-LD validation
    for i, j_content in enumerate(parser.json_ld_contents):
        try:
            json.loads(j_content.strip())
            print(f"  [OK] JSON-LD schema #{i+1} is valid.")
        except json.JSONDecodeError as jde:
            print(f"  [ERROR] JSON-LD schema #{i+1} is invalid JSON: {jde}")
            print("  --- Invalid content starts ---")
            print(j_content.strip())
            print("  --- Invalid content ends ---")
            success = False

    # 3. Check Canonical and Robots depending on expected status
    is_utility = filename in [
        'checkout.html', 'payment-success.html', 'payment-failure.html',
        'access.html', 'emergent-prompt.html', '404.html'
    ]

    if is_utility:
        # Expected: robots content noindex
        if not parser.robots_contents:
            print(f"  [ERROR] No meta robots tag found in utility page {filename}")
            success = False
        else:
            for robots_val in parser.robots_contents:
                norm_robots = robots_val.replace(" ", "").lower()
                if "noindex" in norm_robots:
                    print(f"  [OK] robots tag is set to noindex: '{robots_val}'")
                else:
                    print(f"  [ERROR] robots tag '{robots_val}' does not contain 'noindex'")
                    success = False
    else:
        # Indexable pages
        # Expected: canonical link tag
        if not parser.canonical_hrefs:
            print(f"  [ERROR] No canonical link tag found in indexable page {filename}")
            success = False
        else:
            for canonical in parser.canonical_hrefs:
                if canonical.startswith("https://futurewithai.anshumanenterprises.online/"):
                    print(f"  [OK] Canonical tag found: {canonical}")
                else:
                    print(f"  [ERROR] Canonical tag has incorrect domain/protocol: {canonical}")
                    success = False

    return success

def main():
    html_files = [
        'index.html', 'n8n-pack.html', 'n8n-workflow-automation.html',
        'video-editing.html', 'mega-reels.html', 'web-apps.html',
        'digital-marketing-bundle.html', 'about.html', 'privacy.html',
        'terms.html', 'refund.html', 'checkout.html', 'payment-success.html',
        'payment-failure.html', 'access.html', 'emergent-prompt.html', '404.html'
    ]

    base_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    all_ok = True

    for filename in html_files:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"[WARNING] File not found: {filepath}")
            continue
        
        ok = verify_file(filepath)
        if not ok:
            all_ok = False
        print("-" * 50)

    if all_ok:
        print("\nSUCCESS: ALL HTML AND SCHEMA VERIFICATIONS COMPLETED SUCCESSFULLY!")
    else:
        print("\nFAILURE: SOME VERIFICATIONS FAILED. PLEASE CORRECT ERRORS.")

if __name__ == "__main__":
    main()
