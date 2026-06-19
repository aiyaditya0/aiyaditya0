import os

def main():
    filepath = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\index.html"
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    start_grid = -1
    prod_cards_indices = []
    
    for idx, line in enumerate(lines):
        if 'id="products-grid"' in line:
            start_grid = idx
        elif '<div class="prod-card"' in line:
            prod_cards_indices.append(idx)
            
    print(f"Products Grid starts at line: {start_grid + 1}")
    print(f"Total product cards: {len(prod_cards_indices)}")
    if prod_cards_indices:
        print(f"First product card starts at line: {prod_cards_indices[0] + 1}")
        print(f"6th product card starts at line: {prod_cards_indices[5] + 1}")
        print(f"7th product card starts at line: {prod_cards_indices[6] + 1}")
        print(f"Last product card starts at line: {prod_cards_indices[-1] + 1}")
        
        # Let's find the closing tag for the products-grid div
        # It should be after the last product card.
        # Let's search from the last card downwards to find the closing div of the grid.
        last_card_idx = prod_cards_indices[-1]
        closing_div_idx = -1
        open_divs = 0
        for idx in range(last_card_idx, len(lines)):
            line = lines[idx]
            # Simple check for div close/open
            open_divs += line.count("<div")
            open_divs -= line.count("</div")
            # Since we started inside a card, the card itself will close.
            # Once we balance the card div and then hit the grid's closing div, we find it.
            if "</div>" in line:
                # Let's print the line content to see if it's the grid end
                print(f"Line {idx+1}: {line.strip()}")
                if idx > last_card_idx + 15: # give it some lines to get past the card structure
                    break

if __name__ == "__main__":
    main()
