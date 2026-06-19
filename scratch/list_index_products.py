import os
import re

def main():
    filepath = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\index.html"
    if not os.path.exists(filepath):
        print("index.html not found")
        return
        
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # We want to find each product card and extract details
    # Product cards look like: <div class="prod-card" ...> ... </div>
    # Let's write a parser to extract cards
    cards = re.findall(r'<div class="prod-card"[^>]*>.*?</div>\s*</div>', content, re.DOTALL)
    print(f"Found {len(cards)} product cards in index.html:\n")
    
    for i, chunk in enumerate(cards):
        title_m = re.search(r'<h3 class="prod-title">([^<]+)</h3>', chunk)
        img_m = re.search(r'<img src="([^"]+)"', chunk)
        quick_buy_m = re.search(r'quickBuy\([^)]*\)', chunk)
        detail_link_m = re.search(r'href="([^"]+\.html)"', chunk)
        
        title = title_m.group(1) if title_m else "N/A"
        img = img_m.group(1) if img_m else "N/A"
        qb = quick_buy_m.group(0) if quick_buy_m else "N/A"
        detail_link = detail_link_m.group(1) if detail_link_m else "N/A"
        
        print(f"Product #{i+1}:")
        print(f"  Title: {title}")
        print(f"  Image: {img}")
        print(f"  Quick Buy: {qb}")
        print(f"  Detail Link: {detail_link}")
        print("-" * 40)

if __name__ == "__main__":
    main()
