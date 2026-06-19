import os
import re

def get_bonuses_from_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    # Find bonuses section in HTML body
    pattern = re.compile(r'(?:<!--\s*.*Bonus.*Section\s*-->|<section[^>]*id=["\']bonuses["\'][^>]*>)(.*?)</section>', re.IGNORECASE | re.DOTALL)
    match = pattern.search(content)
    if match:
        body = match.group(1)
        # Find all bonus cards
        bonus_cards = re.findall(r'<div class="bonus-card"[^>]*>.*?</div>\s*</div>', body, re.DOTALL)
        return bonus_cards
    return None

def main():
    root_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    pages = [
        "video-editing.html",
        "mega-reels.html",
        "n8n-pack.html",
        "n8n-workflow-automation.html",
        "web-apps.html",
        "digital-marketing-bundle.html"
    ]
    
    for filename in pages:
        filepath = os.path.join(root_dir, filename)
        cards = get_bonuses_from_file(filepath)
        if cards:
            print(f"File: {filename} - Found {len(cards)} bonuses:")
            for idx, card in enumerate(cards):
                # Extract title and description
                title_m = re.search(r'<h3 class="bonus-card-title">([^<]+)</h3>', card)
                desc_m = re.search(r'<p class="bonus-card-desc">([^<]+)</p>', card)
                title = title_m.group(1).strip() if title_m else "N/A"
                desc = desc_m.group(1).strip() if desc_m else "N/A"
                print(f"  Bonus #{idx+1}: {title}")
                print(f"    Desc: {desc[:80]}...")
        else:
            print(f"File: {filename} - No bonuses section found.")
        print("-" * 50)

if __name__ == "__main__":
    main()
