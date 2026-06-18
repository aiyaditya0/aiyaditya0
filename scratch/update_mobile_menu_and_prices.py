import re

styles_path = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\styles.css"
index_path = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\index.html"

# ══════════════════════════════════════════════════════════════════════════════
# 1. UPDATE STYLES.CSS (Make cart drawer 80% wide and remove backdrop blur on mobile)
# ══════════════════════════════════════════════════════════════════════════════
print("Updating styles.css...")
with open(styles_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace full width mobile cart drawer style with slide-out sidebar style
css_content = css_content.replace(
    ".cart-drawer { width: 100% !important; right: -100% !important; }",
    ".cart-drawer { width: 80% !important; max-width: 340px !important; right: -100% !important; }"
)

# Replace the other mobile rules
css_content = css_content.replace(
    "  .cart-drawer {\n    width: 100%;\n    right: -100%;\n  }",
    "  .cart-drawer {\n    width: 80%;\n    max-width: 340px;\n    right: -100%;\n  }"
)

# Ensure overlay has no blur and light dim on mobile globally
overlay_css = """
  .cart-drawer-overlay {
    background: rgba(0, 0, 0, 0.45) !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
  }
"""
if '.cart-drawer-overlay {' not in css_content:
    # Append to the @media (max-width: 768px) section in styles.css
    # We find the end of @media (max-width: 768px) and insert it
    css_content = css_content.replace(
        "  .cart-drawer {\n    width: 80%;\n    max-width: 340px;\n    right: -100%;\n  }\n}",
        "  .cart-drawer {\n    width: 80%;\n    max-width: 340px;\n    right: -100%;\n  }\n" + overlay_css + "}"
    )

with open(styles_path, 'w', encoding='utf-8') as f:
    f.write(css_content)
print("styles.css updated successfully!")


# ══════════════════════════════════════════════════════════════════════════════
# 2. UPDATE INDEX.HTML (Apply data-price attribute and fix the price label bug)
# ══════════════════════════════════════════════════════════════════════════════
print("Updating index.html...")
with open(index_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace any existing mobile cart drawer styles in internal stylesheet to match styles.css
html_content = html_content.replace(
    ".cart-drawer { width: 100% !important; right: -100% !important; }",
    ".cart-drawer { width: 80% !important; max-width: 340px !important; right: -100% !important; }"
)

# Regex to find the mobile button we generated earlier and replace it with data-price version
# We support matching with or without spaces and icons
button_regex = r'<button class="prod-mobile-buy-btn" data-product-id="([^"]+)" onclick="addToCartAnimated\(this,\'([^\']+)\',\'([^\']+)\',(\d+),\'([^\']+)\',\'([^\']+)\'\)">(.*?)</button>'

def replace_button(match):
    pid = match.group(1)
    name = match.group(3)
    price = match.group(4)
    img = match.group(5)
    link = match.group(6)
    return f'<button class="prod-mobile-buy-btn" data-product-id="{pid}" data-price="{price}" onclick="addToCartAnimated(this,\'{pid}\',\'{name}\',{price},\'{img}\',\'{link}\')"><i data-lucide="zap" style="width:12px;height:12px;margin-right:4px;"></i>Buy Now — ₹{price}</button>'

html_content = re.sub(button_regex, replace_button, html_content)

# Update Javascript button update script to extract price from dataset.price
new_js_update = """
          if (btn.classList.contains('prod-mobile-buy-btn')) {
            const pVal = btn.dataset.price || '99';
            btn.innerHTML = `<i data-lucide="zap" style="width:12px;height:12px;margin-right:4px;"></i>Buy Now — ₹${pVal}`;
          }"""

# Replace the previous matching logic
old_js_update_pattern = r'if\s*\(btn\.classList\.contains\(\'prod-mobile-buy-btn\'\)\)\s*\{\s*const\s*price\s*=\s*btn\.onclick\.toString\(\)\.match\(/\\d\+/\);\s*const\s*pVal\s*=\s*price\s*\?\s*price\[0\]\s*:\s*\'99\';\s*btn\.innerHTML\s*=\s*`[^`]+`;\s*\}'
html_content = re.sub(old_js_update_pattern, new_js_update, html_content)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print("index.html updated successfully!")
