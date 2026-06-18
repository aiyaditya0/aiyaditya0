import os
import re

cart_path = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\cart.js"
index_path = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\index.html"
webapps_path = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\web-apps.html"
video_path = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\video-editing.html"

# ══════════════════════════════════════════════════════════════════════════════
# 1. UPDATE CART.JS (Disable automatic openCart on add)
# ══════════════════════════════════════════════════════════════════════════════
print("Updating cart.js...")
with open(cart_path, 'r', encoding='utf-8') as f:
    cart_js = f.read()

# Replace openCart() on item exist with nothing or just console log
cart_js = cart_js.replace(
    "showToast(`\"${name}\" is already in your cart!`, 'info');\n      openCart();\n      return;",
    "showToast(`\"${name}\" is already in your cart!`, 'info');\n      // openCart(); (disabled automatic drawer)\n      return;"
)

# Replace setTimeout(openCart, 500); with comments
cart_js = cart_js.replace(
    "showToast(`Added \"${name}\" to cart!`, 'success');\n    setTimeout(openCart, 500);",
    "showToast(`Added \"${name}\" to cart!`, 'success');\n    // setTimeout(openCart, 500); (disabled automatic drawer)"
)

with open(cart_path, 'w', encoding='utf-8') as f:
    f.write(cart_js)
print("cart.js updated successfully!")


# ══════════════════════════════════════════════════════════════════════════════
# 2. UPDATE INDEX.HTML (Grid, compact card layout, mobile Buy buttons, toast popups)
# ══════════════════════════════════════════════════════════════════════════════
print("Updating index.html...")
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Parse cards and inject new mobile button below title
onclick_pattern = r"addToCartAnimated\(this\s*,\s*'([^']+)'\s*,\s*'([^']+)'\s*,\s*(\d+)\s*,\s*'([^']+)'\s*,\s*'([^']+)'\)"

# Find all cards blocks
cards = re.findall(r'<div class="prod-card".*?</div>\s*</div>\s*</div>', html, re.DOTALL)

for idx, card in enumerate(cards, 1):
    onclick_match = re.search(onclick_pattern, card)
    if onclick_match:
        pid, name, price, img, link = onclick_match.groups()
        
        # Check if mobile button is already present to prevent duplicate insertions
        if 'prod-mobile-buy-btn' in card:
            continue
            
        # Create new button HTML
        btn_html = f'''<button class="prod-mobile-buy-btn" data-product-id="{pid}" onclick="addToCartAnimated(this,'{pid}','{name}',{price},'{img}','{link}')"><i data-lucide="zap" style="width:12px;height:12px;margin-right:4px;"></i>Buy Now — ₹{price}</button>'''
        
        # Find title inside card body
        title_match = re.search(r'(<h3 class="prod-title">.*?</h3>)', card)
        if title_match:
            original_title_line = title_match.group(1)
            new_title_block = original_title_line + "\n          " + btn_html
            
            # Replace card in html
            new_card = card.replace(original_title_line, new_title_block)
            html = html.replace(card, new_card)
            # Update local card representation for consecutive matches
            card = new_card

# Update internal style block inside index.html to support mobile card improvements
css_overrides = """
    /* Mobile-first 2-Column Grid & Bottom Nav styling */
    @media (max-width: 768px) {
      /* Bottom Padding for body to account for sticky nav */
      body {
        padding-bottom: 75px !important;
      }

      /* Hide standard category pills on mobile */
      .cat-nav {
        display: none !important;
      }

      /* Circular Category Scrollbar on Mobile */
      .circular-categories {
        display: flex !important;
        gap: 12px;
        overflow-x: auto;
        padding: 12px 6px;
        margin-bottom: 16px;
        scrollbar-width: none;
        -ms-overflow-style: none;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      }
      .circular-categories::-webkit-scrollbar {
        display: none;
      }
      .circular-cat-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 6px;
        cursor: pointer;
        flex-shrink: 0;
        width: 64px;
        transition: transform 0.2s;
      }
      .circular-cat-item:active {
        transform: scale(0.92);
      }
      .circular-cat-icon {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(255, 138, 0, 0.12) 0%, rgba(255, 138, 0, 0.04) 100%);
        border: 1px solid rgba(255, 138, 0, 0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        transition: all 0.25s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
      }
      .circular-cat-item.active .circular-cat-icon {
        background: linear-gradient(135deg, #ff8a00 0%, #ffb347 100%);
        border-color: #ffb347;
        color: #000;
        box-shadow: 0 0 12px rgba(255, 138, 0, 0.35);
      }
      .circular-cat-name {
        font-size: 10px;
        font-weight: 600;
        color: rgba(255, 255, 255, 0.6);
        text-align: center;
        white-space: nowrap;
      }
      .circular-cat-item.active .circular-cat-name {
        color: #ff8a00;
        font-weight: 700;
      }

      /* 2-Column Product Grid Override */
      .products-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 10px !important;
        margin-bottom: 24px !important;
      }

      /* Card styling adjustments for 2 columns */
      .prod-card {
        border-radius: 12px !important;
        display: flex !important;
        flex-direction: column !important;
        height: 100% !important;
      }
      .prod-img-wrap {
        height: 110px !important; /* Shorter image height on mobile for extremely compact cards */
      }
      .prod-body {
        padding: 8px !important;
        display: flex !important;
        flex-direction: column !important;
        flex: 1 !important;
        justify-content: space-between !important;
      }
      .prod-category {
        display: none !important; /* Hide category to save height */
      }
      .prod-title {
        font-size: 11px !important;
        line-height: 1.25 !important;
        height: 28px !important;
        overflow: hidden !important;
        display: -webkit-box !important;
        -webkit-line-clamp: 2 !important;
        -webkit-box-orient: vertical !important;
        margin-bottom: 6px !important;
        color: #fff !important;
      }
      .prod-desc {
        display: none !important; /* Hide description on mobile to keep card height clean and structured */
      }
      .prod-features {
        display: none !important; /* Hide bullet features on mobile grid list */
      }
      .prod-footer {
        display: none !important; /* Hide original footer containing price blocks & add buttons */
      }
      
      /* Mobile buy button display */
      .prod-mobile-buy-btn {
        display: flex !important;
        width: 100% !important;
        justify-content: center !important;
        align-items: center !important;
        background: linear-gradient(135deg, #ff8a00, #ffb347) !important;
        color: #000 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 8px 6px !important;
        font-size: 11px !important;
        font-weight: 750 !important;
        margin-top: auto !important;
        cursor: pointer !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.2s !important;
      }
      .prod-mobile-buy-btn.added {
        background: #34c759 !important;
        color: #fff !important;
        cursor: default !important;
      }

      /* Mobile Sticky Bottom Nav */
      .mobile-bottom-nav {
        display: flex !important;
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        right: 0 !important;
        height: 58px !important;
        background: rgba(10, 6, 3, 0.96) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border-top: 1px solid rgba(255, 138, 0, 0.25) !important;
        justify-content: space-around !important;
        align-items: center !important;
        z-index: 9999 !important;
        padding-bottom: safe-area-inset-bottom !important;
      }
      .mobile-nav-item {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        text-decoration: none !important;
        color: rgba(255, 255, 255, 0.5) !important;
        font-size: 9px !important;
        font-weight: 500 !important;
        transition: color 0.2s !important;
        position: relative !important;
        flex: 1 !important;
        padding: 4px 0 !important;
      }
      .mobile-nav-item i {
        margin-bottom: 2px !important;
        width: 18px !important;
        height: 18px !important;
        color: inherit !important;
      }
      .mobile-nav-item span {
        font-family: 'Inter', sans-serif !important;
      }
      .mobile-nav-item.active {
        color: #ff8a00 !important;
        font-weight: 700 !important;
      }
      .mobile-nav-item .cart-badge {
        position: absolute !important;
        top: -2px !important;
        right: 18px !important;
        background: #ff8a00 !important;
        color: #000 !important;
        font-size: 8px !important;
        font-weight: 800 !important;
        border-radius: 50% !important;
        width: 14px !important;
        height: 14px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        border: 1px solid #000 !important;
      }

      /* Fix the Black Screen Freeze: transparent overlay without blur */
      .cart-drawer-overlay {
        background: rgba(0, 0, 0, 0.45) !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
      }
    }

    /* Desktop fallback/hiding styling */
    .circular-categories {
      display: none;
    }
    .mobile-bottom-nav {
      display: none;
    }
    .prod-mobile-buy-btn {
      display: none;
    }

    /* Rating Badge Styles */
    .prod-rating-badge {
      position: absolute;
      bottom: 8px;
      left: 8px;
      background: rgba(0, 0, 0, 0.75);
      color: #fff;
      font-size: 9px;
      font-weight: 700;
      padding: 3px 6px;
      border-radius: 4px;
      z-index: 5;
      display: flex;
      align-items: center;
      gap: 3px;
      backdrop-filter: blur(4px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      font-family: 'Inter', sans-serif;
    }
    .prod-rating-badge span {
      color: rgba(255, 255, 255, 0.5);
      font-weight: 400;
      font-size: 8px;
    }

    /* Purchase Toast Styling */
    #purchase-toast {
      position: fixed;
      bottom: 80px; /* Shifted higher on mobile to clear bottom navigation */
      left: 24px;
      z-index: 99999;
      background: rgba(18, 11, 6, 0.95);
      border: 1px solid rgba(255, 138, 0, 0.3);
      border-radius: 16px;
      padding: 14px;
      width: 320px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5), var(--glow-primary);
      display: flex;
      align-items: center;
      gap: 16px;
      transform: translateY(150px);
      opacity: 0;
      transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      pointer-events: none;
    }
    #purchase-toast.show {
      transform: translateY(0);
      opacity: 1;
    }
    .purchase-toast-avatar {
      width: 42px;
      height: 42px;
      border-radius: 50%;
      background: var(--bg-surface-container-highest, #3f3229);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ff8a00;
      border: 1.5px solid rgba(255,138,0,0.2);
      flex-shrink: 0;
      font-weight: 700;
      font-size: 14px;
    }
    .purchase-toast-content {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .purchase-toast-name {
      font-size: 13px;
      font-weight: 700;
      color: #fff;
    }
    .purchase-toast-prod {
      font-size: 11px;
      color: var(--text-secondary, #ddc1ae);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 230px;
    }
    .purchase-toast-meta {
      font-size: 10px;
      color: #27c93f;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    @media (max-width: 768px) {
      #purchase-toast {
        width: calc(100% - 32px);
        left: 16px;
        bottom: 72px; /* Positioned just above bottom nav */
      }
    }
"""

# Check if new overrides are already in styles
if '/* Mobile-first 2-Column Grid & Bottom Nav styling */' not in html:
    # Replace the previous css overrides block we added in first script
    # We find the style block in head and insert the updated CSS there
    html = html.replace('  </style>\n</head>', css_overrides + '  </style>\n</head>')

# Add purchase-toast HTML before bottom nav if not present
toast_html = """
  <!-- Dynamic Purchase Notification Popup -->
  <div id="purchase-toast">
    <div class="purchase-toast-avatar" id="purchase-toast-avatar">RS</div>
    <div class="purchase-toast-content">
      <span class="purchase-toast-name" id="purchase-toast-name">Rohit S. - Mumbai</span>
      <span class="purchase-toast-prod" id="purchase-toast-prod">purchased n8n Automation Pack</span>
      <span class="purchase-toast-meta">
        <i data-lucide="check-circle-2" style="width: 12px; height: 12px; color: #27c93f; fill: none;"></i> Verified Purchase · <span id="purchase-toast-time">Just now</span>
      </span>
    </div>
  </div>
"""
if 'id="purchase-toast"' not in html:
    html = html.replace('<!-- Mobile Sticky Bottom Navigation -->', toast_html + '\n  <!-- Mobile Sticky Bottom Navigation -->')

# Update script block in index.html to add purchase toast script
purchase_js = """
    // Dynamic Purchase Notification Simulation
    const purchaseData = [
      { name: "Sanjay K.", city: "Mumbai" },
      { name: "Pankaj D.", city: "Noida" },
      { name: "Divya J.", city: "Kolkata" },
      { name: "Kartik S.", city: "Indore" },
      { name: "Nitin B.", city: "Bengaluru" },
      { name: "Deepa G.", city: "Chennai" },
      { name: "Rahul S.", city: "Pune" },
      { name: "Anjali P.", city: "Ahmedabad" },
      { name: "Vikas L.", city: "Lucknow" },
      { name: "Priya M.", city: "Delhi" },
      { name: "Kunal G.", city: "Hyderabad" },
      { name: "Rohit R.", city: "Chandigarh" }
    ];

    const purchaseProducts = [
      "n8n Automation Pack (2000+ Workflows)",
      "Ultimate Video Editing Toolkit (500GB)",
      "100,000+ Viral Reels Goldmine Pack",
      "1500+ Manually Tested Web Apps Source Code",
      "Full Digital Marketing Resource Bundle",
      "Enterprise n8n Automation System",
      "2700+ Elementor Pro Templates",
      "1.37tb All Money Making Courses Bundle"
    ];

    function startPurchaseNotifs() {
      const toast = document.getElementById('purchase-toast');
      const avatar = document.getElementById('purchase-toast-avatar');
      const nameEl = document.getElementById('purchase-toast-name');
      const prodEl = document.getElementById('purchase-toast-prod');
      const timeEl = document.getElementById('purchase-toast-time');
      
      if (!toast || !avatar || !nameEl || !prodEl || !timeEl) return;
      
      let index = 0;
      
      function showNext() {
        const item = purchaseData[index];
        const prod = purchaseProducts[Math.floor(Math.random() * purchaseProducts.length)];
        
        // Set values
        const initials = item.name.split(' ').map(n => n[0]).join('');
        avatar.textContent = initials;
        nameEl.textContent = `${item.name} (${item.city})`;
        prodEl.textContent = `purchased ${prod}`;
        timeEl.textContent = ["Just now", "1 min ago", "2 mins ago", "3 mins ago"][Math.floor(Math.random() * 4)];
        
        // Slide in
        toast.classList.add('show');
        if (window.lucide) lucide.createIcons();
        
        // Slide out after 6 seconds (visible state)
        setTimeout(() => {
          toast.classList.remove('show');
          index = (index + 1) % purchaseData.length;
          
          // Wait 20 seconds before showing next
          setTimeout(showNext, 20000);
        }, 6000);
      }
      
      // Delay first notification by 4s
      setTimeout(showNext, 4000);
    }
"""

if 'function startPurchaseNotifs()' not in html:
    # Insert startPurchaseNotifs function
    html = html.replace('    // Sticky Bottom Navigation Actions', purchase_js + '\n\n    // Sticky Bottom Navigation Actions')
    # Trigger startPurchaseNotifs on DOMContentLoaded
    html = html.replace('if (window.lucide) lucide.createIcons();\n      startTimer();', 'if (window.lucide) lucide.createIcons();\n      startTimer();\n      startPurchaseNotifs();')

# Update index.html script block to hook up disabled styling update for new mobile button
btn_update_js = """
    // Refresh all Add buttons based on current cart state
    function refreshAddButtonStates() {
      const cart = JSON.parse(localStorage.getItem('fwai_cart_items') || '[]');
      const cartIds = cart.map(i => i.id);
      document.querySelectorAll('[data-product-id]').forEach(btn => {
        const pid = btn.dataset.productId;
        if (cartIds.includes(pid)) {
          btn.innerHTML = '<i data-lucide="check" style="width:14px;height:14px;"></i> Added';
          btn.classList.add('added');
          btn.setAttribute('disabled', 'true');
          if (window.lucide) lucide.createIcons();
        } else {
          // Reset button state if removed from cart
          btn.classList.remove('added');
          btn.removeAttribute('disabled');
          if (btn.classList.contains('prod-mobile-buy-btn')) {
            const price = btn.onclick.toString().match(/\\d+/); // Get price from onclick string if possible
            const pVal = price ? price[0] : '99';
            btn.innerHTML = `<i data-lucide="zap" style="width:12px;height:12px;margin-right:4px;"></i>Buy Now — ₹${pVal}`;
          } else if (btn.classList.contains('prod-add-btn')) {
            btn.innerHTML = '<i data-lucide="shopping-cart" style="width:14px;height:14px;margin-right:4px;"></i> Add';
          }
        }
      });
    }
"""

html = html.replace('    // Refresh all Add buttons based on current cart state\n    function refreshAddButtonStates() {', btn_update_js + '\n    // Remove old duplicate definition\n    function _unused_refreshAddButtonStates() {')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html updated successfully!")


# ══════════════════════════════════════════════════════════════════════════════
# 3. UPDATE WEB-APPS.HTML AND VIDEO-EDITING.HTML (Dynamic popups, stay 6s, loop 20s)
# ══════════════════════════════════════════════════════════════════════════════

def update_detail_page_popup(file_path):
    print(f"Updating popup in {os.path.basename(file_path)}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the startPurchaseNotifs script block entirely
    # Let's search for function startPurchaseNotifs
    start_notif_pattern = r'function startPurchaseNotifs\(\)\s*\{.*?setTimeout\(showNext,\s*4000\);\s*\}'
    
    new_notif_js = """function startPurchaseNotifs() {
      const toast = document.getElementById('purchase-toast');
      const avatar = document.getElementById('purchase-toast-avatar') || document.getElementById('toast-avatar');
      const nameEl = document.getElementById('purchase-toast-name') || document.getElementById('toast-buyer-name');
      const prodEl = document.getElementById('purchase-toast-prod') || document.getElementById('toast-product-name');
      const timeEl = document.getElementById('purchase-toast-time') || document.getElementById('toast-time');
      
      if (!toast || !avatar || !nameEl || !prodEl || !timeEl) return;
      
      const purchaseProductsList = [
        "n8n Automation Pack (2000+ Workflows)",
        "Ultimate Video Editing Toolkit (500GB)",
        "100,000+ Viral Reels Goldmine Pack",
        "1500+ Manually Tested Web Apps Source Code",
        "Full Digital Marketing Resource Bundle",
        "Enterprise n8n Automation System",
        "2700+ Elementor Pro Templates",
        "1.37tb All Money Making Courses Bundle"
      ];

      let index = 0;
      
      function showNext() {
        const item = purchaseData[index];
        const prod = purchaseProductsList[Math.floor(Math.random() * purchaseProductsList.length)];
        
        // Set values
        const initials = item.name.split(' ').map(n => n[0]).join('');
        avatar.textContent = initials;
        nameEl.textContent = `${item.name} (${item.city})`;
        prodEl.textContent = `purchased ${prod}`;
        timeEl.textContent = ["Just now", "1 min ago", "2 mins ago", "3 mins ago"][Math.floor(Math.random() * 4)];
        
        // Slide in
        toast.classList.add('show');
        if (window.lucide) lucide.createIcons();
        
        // Slide out after 6 seconds
        setTimeout(() => {
          toast.classList.remove('show');
          index = (index + 1) % purchaseData.length;
          
          // Wait 20 seconds before showing next
          setTimeout(showNext, 20000);
        }, 6000);
      }
      
      // Delay first notification by 4s
      setTimeout(showNext, 4000);
    }"""
    
    updated_content = re.sub(start_notif_pattern, new_notif_js, content, flags=re.DOTALL)
    
    # Make sure we also update the overlay css on these pages so they don't look completely black/blurry either
    overlay_css_fix = """
      .cart-drawer-overlay {
        background: rgba(0, 0, 0, 0.45) !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
      }
    """
    
    # Insert it inside style block before </style>
    if 'background: rgba(0, 0, 0, 0.45) !important;' not in updated_content:
        updated_content = updated_content.replace('  </style>', overlay_css_fix + '\n  </style>')
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Updated {os.path.basename(file_path)} successfully!")

update_detail_page_popup(webapps_path)
update_detail_page_popup(video_path)

print("All components restructured and updated successfully!")
