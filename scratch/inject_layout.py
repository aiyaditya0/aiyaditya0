import re

index_path = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB\index.html"

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the internal style block to inject our styles before </style>
new_css = """
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
        gap: 12px !important;
        margin-bottom: 24px !important;
      }

      /* Card styling adjustments for 2 columns */
      .prod-card {
        border-radius: 12px !important;
      }
      .prod-img-wrap {
        height: 120px !important; /* Shorter image height on mobile to fit the grid aspect ratio */
      }
      .prod-body {
        padding: 10px !important;
      }
      .prod-category {
        font-size: 8px !important;
        margin-bottom: 3px !important;
      }
      .prod-title {
        font-size: 11px !important;
        line-height: 1.25 !important;
        height: 28px !important;
        overflow: hidden !important;
        display: -webkit-box !important;
        -webkit-line-clamp: 2 !important;
        -webkit-box-orient: vertical !important;
        margin-bottom: 4px !important;
      }
      .prod-desc {
        display: none !important; /* Hide description on mobile to keep card height clean and structured */
      }
      .prod-features {
        display: none !important; /* Hide bullet features on mobile grid list */
      }
      .prod-footer {
        padding-top: 8px !important;
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 6px !important;
      }
      .prod-price-block {
        display: flex !important;
        align-items: center !important;
        gap: 4px !important;
        flex-wrap: wrap !important;
      }
      .prod-original {
        font-size: 9px !important;
      }
      .prod-price {
        font-size: 15px !important;
      }
      .prod-discount {
        font-size: 8px !important;
        padding: 1px 4px !important;
      }
      .prod-add-btn {
        width: 100% !important;
        justify-content: center !important;
        font-size: 11px !important;
        padding: 8px 10px !important;
        border-radius: 8px !important;
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
    }

    /* Desktop fallback/hiding styling */
    .circular-categories {
      display: none;
    }
    .mobile-bottom-nav {
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
"""

# Find internal style close tag and insert before it
html = html.replace('  </style>\n</head>', new_css + '  </style>\n</head>')

# 2. Add data-cat-id attribute to all existing cat-btn tags in the header
html = html.replace("filterCat('all', this)\">🏪 All Products", "filterCat('all', this)\" data-cat-id=\"all\">🏪 All Products")
html = html.replace("filterCat('automation', this)\">🤖 Automation", "filterCat('automation', this)\" data-cat-id=\"automation\">🤖 Automation")
html = html.replace("filterCat('editing', this)\">🎬 Video Editing", "filterCat('editing', this)\" data-cat-id=\"editing\">🎬 Video Editing")
html = html.replace("filterCat('reels', this)\">📱 Viral Reels", "filterCat('reels', this)\" data-cat-id=\"reels\">📱 Viral Reels")
html = html.replace("filterCat('webapps', this)\">💻 Web Apps", "filterCat('webapps', this)\" data-cat-id=\"webapps\">💻 Web Apps")
html = html.replace("filterCat('marketing', this)\">📊 Digital Marketing", "filterCat('marketing', this)\" data-cat-id=\"marketing\">📊 Digital Marketing")

# 3. Inject circular categories navigation inside products container
circular_nav_html = """
    <!-- Mobile Categories Navigation (Horizontal Circular Scroll) -->
    <div class="circular-categories" id="circular-categories">
      <div class="circular-cat-item active" data-cat-id="all" onclick="filterCat('all', this)">
        <div class="circular-cat-icon">🏪</div>
        <div class="circular-cat-name">All</div>
      </div>
      <div class="circular-cat-item" data-cat-id="automation" onclick="filterCat('automation', this)">
        <div class="circular-cat-icon">🤖</div>
        <div class="circular-cat-name">Automation</div>
      </div>
      <div class="circular-cat-item" data-cat-id="editing" onclick="filterCat('editing', this)">
        <div class="circular-cat-icon">🎬</div>
        <div class="circular-cat-name">Editing</div>
      </div>
      <div class="circular-cat-item" data-cat-id="reels" onclick="filterCat('reels', this)">
        <div class="circular-cat-icon">📱</div>
        <div class="circular-cat-name">Reels</div>
      </div>
      <div class="circular-cat-item" data-cat-id="webapps" onclick="filterCat('webapps', this)">
        <div class="circular-cat-icon">💻</div>
        <div class="circular-cat-name">Web Apps</div>
      </div>
      <div class="circular-cat-item" data-cat-id="marketing" onclick="filterCat('marketing', this)">
        <div class="circular-cat-icon">📊</div>
        <div class="circular-cat-name">Marketing</div>
      </div>
    </div>
"""

# Place it right after <div class="store-layout" id="products">
html = html.replace('<div class="store-layout" id="products">', '<div class="store-layout" id="products">\n' + circular_nav_html)

# 4. Inject sticky bottom navigation before </body>
bottom_nav_html = """
  <!-- Mobile Sticky Bottom Navigation -->
  <div class="mobile-bottom-nav" id="mobile-bottom-nav">
    <a href="index.html" class="mobile-nav-item active" onclick="handleBottomNavClick(event, 'home')">
      <i data-lucide="home"></i>
      <span>Home</span>
    </a>
    <a href="#products" class="mobile-nav-item" onclick="handleBottomNavClick(event, 'categories')">
      <i data-lucide="grid"></i>
      <span>Categories</span>
    </a>
    <a href="#" class="mobile-nav-item cart-toggle-trigger" onclick="handleBottomNavClick(event, 'cart')">
      <div style="position: relative; display: inline-flex;">
        <i data-lucide="shopping-cart"></i>
        <span class="cart-count cart-badge">0</span>
      </div>
      <span>Cart</span>
    </a>
    <a href="https://chat.whatsapp.com/L7M5r6mMdoKEh3cvM5F1xr" target="_blank" class="mobile-nav-item" onclick="handleBottomNavClick(event, 'community')">
      <i data-lucide="message-square"></i>
      <span>Community</span>
    </a>
    <a href="https://wa.me/917065815743?text=Hi%2C%20I%20need%20support%20regarding%20FutureWithAI%20Store" target="_blank" class="mobile-nav-item" onclick="handleBottomNavClick(event, 'support')">
      <i data-lucide="phone"></i>
      <span>Support</span>
    </a>
  </div>
"""

html = html.replace('</body>', bottom_nav_html + '\n</body>')

# 5. Inject JavaScript functions before </script>
js_updates = """
    // Sync Category Filter Active States and Category Nav Scroll
    const originalFilterCat = filterCat;
    filterCat = function(cat, btn) {
      // Clear active classes from both standard buttons and circular items
      document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.circular-cat-item').forEach(b => b.classList.remove('active'));
      
      // Activate clicked item
      btn.classList.add('active');
      
      // Sync active state in the other nav bar
      if (btn.classList.contains('cat-btn')) {
        const circBtn = document.querySelector(`.circular-cat-item[data-cat-id="${cat}"]`);
        if (circBtn) circBtn.classList.add('active');
      } else {
        const pillBtn = document.querySelector(`.cat-btn[data-cat-id="${cat}"]`);
        if (pillBtn) pillBtn.classList.add('active');
      }

      // Sync active state in sticky bottom nav
      const bottomNavItems = document.querySelectorAll('.mobile-nav-item');
      bottomNavItems.forEach(i => i.classList.remove('active'));
      const catNavItem = document.querySelector('.mobile-nav-item[onclick*="categories"]');
      if (catNavItem) catNavItem.classList.add('active');

      // Call original filtering logic
      originalFilterCat(cat, btn);
    };

    // Sticky Bottom Navigation Actions
    function handleBottomNavClick(event, action) {
      const items = document.querySelectorAll('.mobile-nav-item');
      items.forEach(item => item.classList.remove('active'));

      if (action === 'home') {
        event.preventDefault();
        window.scrollTo({top: 0, behavior: 'smooth'});
        event.currentTarget.classList.add('active');
      } else if (action === 'categories') {
        event.preventDefault();
        const target = document.getElementById('products');
        if (target) {
          target.scrollIntoView({behavior: 'smooth'});
        }
        event.currentTarget.classList.add('active');
      } else if (action === 'cart') {
        event.preventDefault();
        openCart();
        // Keep active highlighted temporarily or permanently
        event.currentTarget.classList.add('active');
      }
      // Community and Support will naturally open their href in target="_blank"
    }

    // Sync active mobile nav on scroll
    window.addEventListener('scroll', () => {
      const productsSection = document.getElementById('products');
      if (!productsSection) return;
      
      const bottomNavItems = document.querySelectorAll('.mobile-nav-item');
      const rect = productsSection.getBoundingClientRect();
      const inProducts = rect.top <= window.innerHeight / 2 && rect.bottom >= window.innerHeight / 2;
      
      if (window.scrollY < 200) {
        bottomNavItems.forEach(i => i.classList.remove('active'));
        const homeNavItem = document.querySelector('.mobile-nav-item[onclick*="home"]');
        if (homeNavItem) homeNavItem.classList.add('active');
      } else if (inProducts) {
        bottomNavItems.forEach(i => i.classList.remove('active'));
        const catNavItem = document.querySelector('.mobile-nav-item[onclick*="categories"]');
        if (catNavItem) catNavItem.classList.add('active');
      }
    });
"""

html = html.replace('  </script>\n</body>', js_updates + '  </script>\n</body>')

# 6. Inject rating badges in each product card's image wrap
# Let's find all prod-cards and their image wraps
# We'll use a deterministic function to add the badge

def get_rating_info(name):
    name_lower = name.lower()
    if 'n8n automation' in name_lower or '2000 workflows' in name_lower:
        return '4.9', '2.4K'
    elif '14000 n8n' in name_lower or 'enterprise' in name_lower:
        return '4.9', '1.2K'
    elif 'video editing toolkit' in name_lower or '500gb' in name_lower:
        return '4.8', '1.8K'
    elif '100000' in name_lower or 'reels goldmine' in name_lower:
        return '4.8', '3.1K'
    elif '1500 manually' in name_lower or 'web apps' in name_lower:
        return '4.7', '940'
    elif 'digital marketing resource' in name_lower:
        return '4.9', '2.4K'
    h = sum(ord(c) for c in name)
    rating = ['4.7', '4.8', '4.9'][h % 3]
    reviews = [120, 240, 310, 480, 560, 780, 850][h % 7]
    return rating, f"{reviews}"

# Parse and match prod-card pattern
pattern = r'(<div class="prod-card" data-cat="([^"]+)" data-name="([^"]+)"[^>]*>.*?<div class="prod-img-wrap">.*?<img [^>]+>)'

def replace_img_wrap(match):
    full_img_match = match.group(1)
    name = match.group(3)
    rating, reviews = get_rating_info(name)
    badge_html = f'\\n          <div class="prod-rating-badge">⭐ {rating} <span>| {reviews}</span></div>'
    # Check if badge already exists in this block (for idempotency)
    if 'class="prod-rating-badge"' in full_img_match:
        return full_img_match
    return full_img_match + badge_html

updated_html = re.sub(pattern, replace_img_wrap, html, flags=re.DOTALL)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(updated_html)

print("Restructured index.html layout & ratings injected successfully!")
