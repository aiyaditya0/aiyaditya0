import os
import openpyxl
import re

def make_product_id(name):
    # Strip numbers at start like "1. ", "10. ", etc.
    clean = re.sub(r'^\d+\.\s*', '', name)
    # Lowercase, replace non-alphanumeric with hyphen
    clean = clean.lower()
    clean = re.sub(r'[^a-z0-9\s-]', '', clean)
    clean = re.sub(r'[\s-]+', '-', clean).strip('-')
    return clean

def get_product_image(name, category_id):
    name_lower = name.lower()
    
    # Exact mappings for the new WebP images provided by the user
    if "infographic post canva" in name_lower or "550+ fitness health" in name_lower:
        return "0592048c-f88b-41a6-bc23-0eaff4e60064.webp"
    elif "travel reels bundle" in name_lower:
        return "062c4ef6-262f-4d6b-beda-62ba5d7f154a.webp"
    elif "lifestyle reels bundle" in name_lower:
        return "074f8b8c-c197-44d2-b38c-4a4d69698588.webp"
    elif "5000+ mega reels bundle" in name_lower or "5000+ mega reels" in name_lower:
        return "255ad432-0183-46a6-9bad-fcde38327c83.webp"
    elif "space content reels bundle" in name_lower or "space content" in name_lower:
        return "35c0c997-945b-4f67-b5c7-2ea83275c1be.webp"
    elif "glowing motion graphics" in name_lower or "glowing motion" in name_lower:
        return "48e15f8f-547e-4ee6-b3a6-beaa52bbc7ae.webp"
    elif "luxury hotels and resorts" in name_lower or "luxury hotels" in name_lower:
        return "5ab06a38-7ad9-4c1f-93de-c92f6eb0e19f.webp"
    elif "mega car reels bundle" in name_lower or "mega car" in name_lower:
        return "8537458a-8df9-4489-8f8f-6b6a64ddc03e.webp"
    elif "animation explaining" in name_lower or "explaining motivation" in name_lower:
        return "9b80d846-5f05-4d84-8103-c7ed626da19e.webp"
    elif "youtuber kit" in name_lower:
        return "a0c80c0f-3c0a-4930-adb3-e3170b2e9f78.webp"
    elif "english health reels bundle" in name_lower or "english health reels" in name_lower:
        return "b1cea753-66e9-4085-9d6d-84f19973cb47.webp"
    elif "gym" in name_lower or "fitness reels" in name_lower:
        return "b578e47f-4c4a-420c-b59a-3bbc90470abf.webp"
    elif "ai (english) reels" in name_lower or "ai (english)" in name_lower or "700+ ai" in name_lower:
        return "d1afab38-4733-4fbb-b4d8-0710b238de74.webp"
    elif "business growth reels bundle" in name_lower or "business growth" in name_lower:
        return "d3cd854c-b2ff-495e-a47e-b2ead1943696.webp"
    elif "natures reels bundle" in name_lower or "nature reels" in name_lower:
        return "ea545e56-e4a6-4551-ab1f-8aa0e1593fc5.webp"
    elif "ai reels bundle" in name_lower:
        return "fa8550fe-ca58-442a-8906-7d9b4454eb88.webp"
    elif "php scripts" in name_lower or "php" in name_lower:
        return "ChatGPT Image Jun 17, 2026, 08_01_16 PM.webp"
    elif "premium transitions" in name_lower or "transitions" in name_lower:
        return "dcd1eb49-06e0-4670-9b58-34251a1cf975.webp"
    elif "latest editing" in name_lower or "editing 2026" in name_lower:
        return "54beffc5-a747-4142-a5f6-4c32af142c40.webp"
    elif "graphics bundle" in name_lower:
        return "61ac1b38-c5f7-4a17-a64b-59330a93ea76.webp"
    elif "marketing bundle" in name_lower or "digital marketing bundle" in name_lower:
        return "4e4d70ac-e86e-40fe-94b7-168459764baa.webp"
    elif "elementor pro templates" in name_lower or "elementor" in name_lower:
        return "9570321e-3dd1-4d10-b32a-cb3ea8458624.webp"
    elif "ultimate web applications" in name_lower:
        return "e5ede526-2409-4388-9197-cd2b8d7553a3.webp"
    elif "21 hrs content" in name_lower:
        return "3117313c-1dbe-4180-8ec0-838d3223ee52.webp"
    elif "animation visual reels" in name_lower:
        return "bfcbbd14-cbcd-4daa-8278-50bf6240c648.webp"
    elif "luxury reels" in name_lower:
        return "63948cf2-88fa-4cdc-a802-1a91d77f0fd9.webp"
        
    # General fallbacks
    if "art" in name_lower or "craft" in name_lower:
        return "reels_art_preview.webp"
    elif "woodwork" in name_lower:
        return "reels_woodwork_preview.webp"
    elif "cricket" in name_lower:
        return "reels_cricket_preview.webp"
    elif "caravan" in name_lower:
        return "reels_hero_mockup.webp"
    elif "travel" in name_lower or "lifestyle" in name_lower or "luxury hotels" in name_lower:
        return "hero-image.webp"
    elif "web applications" in name_lower or "web app" in name_lower:
        return "saas_dashboard_mockup.webp"
    elif "transitions" in name_lower or "latest editing" in name_lower or "graphics bundle" in name_lower:
        return "reels_playbook_preview.webp"
    elif "marketing" in name_lower or "elementor" in name_lower:
        return "ecommerce_portal_mockup.webp"
    elif "money making courses" in name_lower or "all money making" in name_lower:
        return "laptop-workspace.webp"
        
    if category_id == "webapps":
        return "webapp_hero_mockup.webp"
    elif category_id == "marketing":
        return "ecommerce_portal_mockup.webp"
    elif "editing" in category_id or "reels" in category_id:
        return "reels_hero_mockup.webp"
        
    return "hero-image.webp"


def get_custom_description(name):
    name_lower = name.lower()
    if "animation explaining" in name_lower or "explaining motivation" in name_lower:
        return "500+ premium animated reels/shorts for motivational channels. Stunning visual loops, clean fonts, and high-impact voiceovers."
    elif "text overlay" in name_lower:
        return "500+ ready-to-use motivational reels featuring bold text overlays, trending background score, and high-retention cinematic clips."
    elif "english health reels" in name_lower:
        return "500+ high-definition health, nutrition, and wellness reels in English. Grow your health theme page with zero content creation hassle."
    elif "700+ ai" in name_lower or "ai (english) reels" in name_lower:
        return "700+ futuristic AI-narrated English reels. High-quality visuals, auto-generated subtitles, and viral potential built-in."
    elif "business growth" in name_lower:
        return "1000+ business growth, startup ideas, entrepreneurship, and wealth-building reels. Drive premium B2B traffic to your page."
    elif "mega car reels" in name_lower or "car reels" in name_lower:
        return "200+ cinematic luxury & sports car reels. Experience engine roars, drift clips, and ultra-high-quality luxury aesthetics."
    elif "gym" in name_lower or "fitness reels" in name_lower:
        return "2200+ high-intensity workout routines, gym motivation, and athletic clips. Perfect for building a massive fitness community."
    elif "infographic post canva" in name_lower or "infographic post" in name_lower:
        return "550+ fully editable health & fitness infographics for Canva. Customize colors, fonts, and logos to post viral slide content."
    elif "youtuber kit" in name_lower:
        return "Essential assets for YouTubers: 1000+ sound effects, modern lower thirds, intro/outro screens, glitch FX, and editing transitions."
    elif "natures reels" in name_lower or "nature reels" in name_lower:
        return "1000+ satisfying, peaceful nature reels. Ideal for meditation channels, relaxing background loops, and aesthetic pages."
    elif "space content" in name_lower or "space reels" in name_lower:
        return "1200+ educational space, science, and astronomy shorts. Narrative documentary style that keeps viewers hooked till the end."
    elif "ai reels" in name_lower:
        return "Futuristic AI Avatar reels pack. Ready-to-publish educational and self-help videos featuring high-retention AI speakers."
    elif "animation visual" in name_lower:
        return "Satisfying 3D loops, abstract physics simulations, and colorful animation reels designed for maximum viewer retention."
    elif "art and craft" in name_lower:
        return "Dozens of satisfying DIY craft, sketching, pottery, and miniature art reels. Highly aesthetic and universally loved."
    elif "black word" in name_lower or "white background images" in name_lower:
        return "Elegant minimalist text quotes on white & black backgrounds. Ideal for Instagram story highlight covers and aesthetic grid posts."
    elif "caravan life" in name_lower:
        return "Scenic van life, camping, road trips, and outdoor travel reels. Perfect for wanderlust bloggers and travel creators."
    elif "dog reels" in name_lower:
        return "Adorable and funny dog compilations. Tap into the highly profitable pet niche with cute clips that gather millions of views."
    elif "funny and cute cat" in name_lower or "cat bundle" in name_lower:
        return "Hundreds of viral, cute cat videos and reels. Instant engagement boosters that are heavily favored by the social algorithm."
    elif "health infographic" in name_lower:
        return "Valuable nutrition tips and healthy habit posts. Regularly updated with fresh vector graphics and editable canvas templates."
    elif "lifestyle reels" in name_lower:
        return "Premium luxury lifestyle, mansions, private jets, and travel clips. Show off the dream life to build a luxury brand page."
    elif "luxury hotels" in name_lower or "resorts" in name_lower:
        return "Stunning aesthetic walkthroughs of 5-star hotels, infinity pools, and villas worldwide. Perfect for luxury travel niche."
    elif "travel reels" in name_lower:
        return "Cinematic landscape clips, tropical islands, and mountain views from around the world. Excellent for travel and lifestyle pages."
    elif "glowing motion" in name_lower:
        return "1500+ trending glowing line animations, neon overlays, and motion graphics assets. Level up your editing instantly."
    elif "500+ luxury" in name_lower:
        return "500+ curated premium aesthetic reels of supercars, high-end watches, and luxury travel. Build a top-tier brand page."
    elif "5000+ mega" in name_lower:
        return "Our flagship bundle containing 5000+ high-quality reels covering gym, health, tech, and finance niches. Complete package."
    elif "php scripts" in name_lower:
        return "400+ working PHP source code scripts for building SaaS platforms, utility directories, tools, booking websites, and portals."
    elif "ultimate web applications" in name_lower or "theme & plugins" in name_lower:
        return "200+ premium WordPress themes, elementor templates, security plugins, and SEO tools with lifetime developer licenses."
    elif "21 hrs content" in name_lower:
        return "Step-by-step 21-hour masterclass tutorial on installing, configuring, hosting, and monetizing the 1500+ web application source codes."
    elif "premium transitions" in name_lower:
        return "1500+ drag-and-drop transitions (zooms, wipes, glitch, spins) for Premiere Pro, CapCut, and After Effects."
    elif "latest editing" in name_lower:
        return "The absolute latest 2026 editing package including dynamic overlays, sound effects, LUTs, and typography tools."
    elif "graphics bundle" in name_lower:
        return "Over 100 GB of premium vector shapes, social templates, corporate mockups, PNG icons, and branding presentation files."
    elif "digital marketing" in name_lower or "igital marketing" in name_lower:
        return "Ready-made social media ad copy, cold email frameworks, contract templates, and marketing proposals to scale your agency."
    elif "elementor pro" in name_lower:
        return "2700+ pre-designed Elementor Pro landing pages, complete website structures, widgets, and business blocks."
    elif "money making courses" in name_lower or "all money making" in name_lower:
        return "A massive 1.37 Terabyte catalog of courses on dropshipping, coding, copywriting, organic marketing, and agency scaling."
    else:
        return "Access high-quality direct download folder containing premium digital assets, templates, and files with lifetime access."

def generate_catalog_html():
    excel_path = "PRODUCT.xlsx"
    wb = openpyxl.load_workbook(excel_path, data_only=True)
    sheet = wb.active
    
    products = []
    
    for row_idx, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
        category = row[0]
        name = row[1]
        price = row[2]
        unit = row[3]
        link = row[4]
        
        if not name or not category:
            continue
            
        category = str(category).strip()
        name = str(name).strip()
        link = str(link).strip() if link else ""
        
        # Determine clean category ID matching homepage filters
        cat_lower = category.lower()
        name_lower = name.lower()
        if "software" in cat_lower or "web" in cat_lower:
            cat_id = "webapps"
            cat_display = "💻 Web Apps"
        elif "editing bundle" in cat_lower:
            cat_id = "editing"
            cat_display = "🎬 Video Editing"
        elif "marketing" in cat_lower or "maketing" in cat_lower or "business" in cat_lower:
            cat_id = "marketing"
            cat_display = "📊 Digital Marketing"
        elif "video editing" in cat_lower:
            # Check if it's editing assets or reels
            if any(x in name_lower for x in ["youtuber", "graphics", "motion", "transitions", "editing"]):
                cat_id = "editing"
                cat_display = "🎬 Video Editing"
            else:
                cat_id = "reels"
                cat_display = "📱 Viral Reels"
        else:
            cat_id = "reels"
            cat_display = "📱 Viral Reels"
            
        img = get_product_image(name, cat_id)
            
        # Determine price
        price_str = str(price).strip().upper() if price is not None else ""
        is_free = "FREE" in price_str or price == 0 or not price
        
        # Skip free items in the public catalog since they are delivered as bonuses
        if is_free:
            continue
            
        prod_id = make_product_id(name)
        
        products.append({
            "id": prod_id,
            "name": name,
            "category_id": cat_id,
            "category_display": cat_display,
            "price": 0 if is_free else int(price),
            "is_free": is_free,
            "img": img,
            "link": link,
            "desc": get_custom_description(name)
        })
        
    # Build HTML string
    product_cards_html = ""
    for p in products:
      if p["is_free"]:
        badge_html = '<div class="prod-badge badge-free">🎁 Free</div>'
        price_display = '<span class="prod-price">FREE</span>'
        quick_buy_html = f"""
        <a href="{p["link"]}" target="_blank" class="quick-buy-btn free-btn">
          <i data-lucide="download" style="width:14px;height:14px;"></i> Download Free
        </a>
        <a href="product-{p["id"]}.html" class="quick-view-btn">
          <i data-lucide="eye" style="width:16px;height:16px;"></i>
        </a>
        """
        action_btn = f"""
          <a href="product-{p["id"]}.html" class="prod-add-btn" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); color:#fff; text-align:center; text-decoration:none; flex:1; justify-content:center; font-size:12px; padding:10px;"><i data-lucide="info" style="width:13px;height:13px;margin-right:4px;"></i> Details</a>
          <a href="{p["link"]}" target="_blank" class="prod-add-btn free-btn" style="flex:1.2; padding:10px; justify-content:center; text-decoration:none;"><i data-lucide="download" style="width:14px;height:14px;margin-right:4px;"></i> Download</a>
        """
        features_html = f'<div class="prod-feat-item"><i data-lucide="zap" style="width:12px;height:12px;"></i>Instant direct access</div>'
      else:
        badge_html = '<div class="prod-badge badge-sale">🔥 Paid</div>'
        orig_price = 499 if p["price"] > 50 else 299
        discount = int(round((1.0 - float(p["price"]) / float(orig_price)) * 100))
        price_display = f"""
          <span class="prod-original">₹{orig_price}</span>
          <span class="prod-price">₹{p["price"]}</span>
          <span class="prod-discount">{discount}% OFF</span>
        """
        p_name_escaped = p["name"].replace("'", "\\'")
        quick_buy_html = f"""
        <button class="quick-buy-btn" onclick="buyNow(\'{p["id"]}\',\'{p_name_escaped}\',{p["price"]},\'{p["img"]}\',\'product-{p["id"]}.html\')">
          <i data-lucide="zap" style="width:14px;height:14px;"></i> Buy Now ₹{p["price"]}
        </button>
        <a href="product-{p["id"]}.html" class="quick-view-btn">
          <i data-lucide="eye" style="width:16px;height:16px;"></i>
        </a>
        """
        action_btn = f"""
          <button class="prod-add-btn" onclick="addToCartAnimated(this,\'{p["id"]}\',\'{p_name_escaped}\',{p["price"]},\'{p["img"]}\',\'product-{p["id"]}.html\')" style="flex:1; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); color:#fff; justify-content:center; padding:10px;" title="Add to Cart" data-product-id="{p["id"]}">
            <i data-lucide="shopping-cart" style="width:14px;height:14px;margin-right:4px;"></i> Add
          </button>
          <button class="prod-add-btn" onclick="buyNow(\'{p["id"]}\',\'{p_name_escaped}\',{p["price"]},\'{p["img"]}\',\'product-{p["id"]}.html\')" style="flex:1.8; background:linear-gradient(135deg,#ff8a00,#ffb347); border:none; color:#000; font-weight:800; justify-content:center; padding:10px; box-shadow:0 4px 12px rgba(255,138,0,0.25);">
            <i data-lucide="zap" style="width:14px;height:14px;margin-right:4px;"></i> Buy Now
          </button>
        """
        features_html = f'<div class="prod-feat-item"><i data-lucide="shield-check" style="width:12px;height:12px;"></i>Secure link delivery</div>'

      product_cards_html += f"""
      <div class="prod-card" data-cat="{p["category_id"]}" data-name="{p["name"].lower()}" data-free="{"true" if p["is_free"] else "false"}">
        {badge_html}
        <div class="prod-img-wrap">
          <a href="product-{p["id"]}.html"><img src="{p["img"]}" alt="{p["name"]}" loading="lazy"></a>
          <div class="prod-quick-buy">
            {quick_buy_html}
          </div>
        </div>
        <div class="prod-body">
          <div class="prod-category">{p["category_display"]}</div>
          <h3 class="prod-title"><a href="product-{p["id"]}.html" style="color:inherit; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color=\'#ff8a00\'" onmouseout="this.style.color=\'inherit\'">{p["name"]}</a></h3>
          <p class="prod-desc">{p["desc"]}</p>
          <div class="prod-features">
            {features_html}
            <div class="prod-feat-item"><i data-lucide="infinity" style="width:12px;height:12px;"></i>Lifetime Access</div>
          </div>
          <div class="prod-footer">
            <div class="prod-price-block">
              {price_display}
            </div>
            <div style="display:flex; gap:8px; width:100%; margin-top: 8px;">
              {action_btn}
            </div>
          </div>
        </div>
      </div>"""

    # Read template HTML structure
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FutureWithAI — Digital Product Store</title>
  
  <meta name="description" content="Shop premium individual reels packs, video editing assets, website software templates, courses, and digital marketing tools. Instant post-payment link delivery.">
  <link rel="icon" type="image/png" href="favicon.webp">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="styles.css">
  <script src="https://unpkg.com/lucide@latest" defer></script>
  <script src="pixel-tracker.js" defer></script>
  <script src="cart.js" defer></script>
  
  <noscript>
    <img height="1" width="1" style="display:none"
         src="https://www.facebook.com/tr?id=2550902175328844&ev=PageView&noscript=1"/>
  </noscript>
  
  <style>
    /* Premium Styling additions */
    #top-bar {
      background: linear-gradient(90deg, #b34500 0%, #ff8a00 50%, #b34500 100%);
      background-size: 200% 100%;
      animation: barAnim 4s linear infinite;
      color: #000; text-align: center; padding: 10px 16px;
      font-size: 13px; font-weight: 700; font-family: 'Inter', sans-serif;
      display: flex; align-items: center; justify-content: center; gap: 10px;
      position: sticky; top: 0; z-index: 9999;
      box-shadow: 0 2px 20px rgba(255,138,0,0.4);
    }
    @keyframes barAnim { 0%,100%{background-position:0% 50%} 50%{background-position:100% 50%} }
    
    header {
      position: sticky; top: 42px; z-index: 1000;
      background: rgba(5,5,5,0.92);
      backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(255,255,255,0.07);
    }
    .header-inner {
      max-width: 1300px; margin: 0 auto;
      display: flex; align-items: center; justify-content: space-between;
      padding: 10px 24px; gap: 16px;
    }
    .logo-wrap { display: flex; align-items: center; text-decoration: none; }
    .logo-wrap img { height: 52px; width: auto; object-fit: contain; }
    
    .search-bar {
      flex: 1; max-width: 420px;
      display: flex; align-items: center; gap: 10px;
      background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
      border-radius: 12px; padding: 10px 16px;
    }
    .search-bar input {
      background: none; border: none; outline: none;
      color: #fff; font-size: 14px; width: 100%;
      font-family: 'Inter', sans-serif;
    }
    .search-bar i { color: rgba(255,255,255,0.4); flex-shrink: 0; }
    
    .header-actions { display: flex; align-items: center; gap: 12px; }
    .cart-btn {
      position: relative; background: rgba(255,138,0,0.12);
      border: 1px solid rgba(255,138,0,0.3);
      color: #ff8a00; border-radius: 12px; cursor: pointer;
      padding: 10px 16px; display: flex; align-items: center; gap: 8px;
      font-size: 13px; font-weight: 600; font-family: 'Inter', sans-serif;
      transition: all 0.2s;
    }
    .cart-btn:hover { background: rgba(255,138,0,0.2); }
    .cart-count {
      background: #ff8a00; color: #000; border-radius: 50%;
      width: 18px; height: 18px; font-size: 10px; font-weight: 800;
      display: flex; align-items: center; justify-content: center;
    }
    .whatsapp-btn {
      background: #25D366; color: #fff; border: none; border-radius: 12px;
      padding: 10px 16px; font-size: 13px; font-weight: 600;
      cursor: pointer; text-decoration: none; display: flex; align-items: center; gap: 6px;
      font-family: 'Inter', sans-serif; transition: all 0.2s; white-space: nowrap;
    }
    .whatsapp-btn:hover { background: #20bd5a; transform: translateY(-1px); }
    
    .cat-nav {
      background: rgba(0,0,0,0.6); border-bottom: 1px solid rgba(255,255,255,0.06);
      position: sticky; top: 92px; z-index: 900; overflow-x: auto;
    }
    .cat-nav::-webkit-scrollbar { display: none; }
    .cat-nav-inner {
      display: flex; gap: 0; max-width: 1300px; margin: 0 auto; padding: 0 24px;
    }
    .cat-btn {
      padding: 12px 18px; font-size: 13px; font-weight: 600;
      color: rgba(255,255,255,0.5); background: none; border: none;
      cursor: pointer; white-space: nowrap; transition: all 0.2s;
      border-bottom: 2px solid transparent; font-family: 'Inter', sans-serif;
    }
    .cat-btn:hover { color: #ff8a00; }
    .cat-btn.active { color: #ff8a00; border-bottom-color: #ff8a00; }
    
    .prod-card {
      background: rgba(20,12,5,0.85);
      border: 1px solid rgba(255,255,255,0.06);
      border-radius: 18px; display: flex; flex-direction: column;
      position: relative; transition: all 0.25s; overflow: hidden;
      cursor: pointer;
    }
    .prod-card:hover {
      border-color: rgba(255,138,0,0.35);
      transform: translateY(-4px);
      box-shadow: 0 16px 40px rgba(0,0,0,0.5), 0 0 20px rgba(255,138,0,0.1);
    }
    .badge-free { background: #27c93f; color: #fff; }
    .free-btn {
      background: linear-gradient(135deg, #27c93f, #1e9a30) !important;
      color: #fff !important;
    }
    .free-btn:hover {
      box-shadow: 0 4px 16px rgba(39,201,63,0.4) !important;
    }
    
    .store-hero {
      background: linear-gradient(135deg, #0a0614 0%, #1c0e00 50%, #0a0614 100%);
      padding: 50px 0 40px; text-align: center;
    }
    .hero-title {
      font-family: 'Playfair Display', serif; font-size: clamp(28px, 4vw, 44px);
      color: #fff; line-height: 1.2; margin-bottom: 12px;
    }
    .hero-title span { color: #ff8a00; }
    .hero-sub {
      color: rgba(255,255,255,0.6); font-size: 15px;
      line-height: 1.6; margin: 0 auto 24px; max-width: 600px;
    }
    
    @media(max-width:768px){
      .header-inner { padding: 8px 14px; }
      .logo-wrap img { height: 40px; }
      .search-bar { display: none; }
      .cat-nav { top: 58px; }
      .cat-btn { padding: 10px 12px; font-size: 12px; }
    }
    
    /* ── Review Grid & Testimonials ── */
    .review-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-top: 48px;
    }
    @media(max-width: 900px) {
      .review-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media(max-width: 580px) {
      .review-grid { grid-template-columns: 1fr; }
    }
    .review-card {
      background: rgba(20, 12, 5, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 20px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      transition: all 0.25s;
    }
    .review-card:hover {
      border-color: rgba(255, 138, 0, 0.35);
      box-shadow: 0 12px 30px rgba(0,0,0,0.6), 0 0 15px rgba(255, 138, 0, 0.08);
      transform: translateY(-4px);
    }
    .review-stars {
      color: #ffb300;
      font-size: 13px;
      display: flex;
      align-items: center;
      gap: 2px;
    }
    .review-text {
      font-size: 13.5px;
      color: rgba(255, 255, 255, 0.7);
      line-height: 1.55;
      font-style: italic;
    }
    .review-author {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-top: auto;
      border-top: 1px solid rgba(255,255,255,0.05);
      padding-top: 12px;
    }
    .review-avatar {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(255, 138, 0, 0.12);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      color: #ff8a00;
      border: 1px solid rgba(255, 138, 0, 0.25);
      font-size: 13px;
    }
    .review-name {
      font-size: 13.5px;
      font-weight: 600;
      color: #fff;
      display: block;
    }
    .review-role {
      font-size: 11px;
      color: rgba(255, 255, 255, 0.4);
      display: block;
    }
  </style>
</head>
<body>

  <!-- Top Announcement Bar -->
  <div id="top-bar">
    <span>🎁 <strong>LIMITED TIME OFFER</strong> — Buy any product & get 9+ Premium Bonus Products (Worth ₹19,491) completely FREE!</span>
    <button id="top-bar-close" onclick="this.parentElement.style.display='none'">✕</button>
  </div>

  <!-- Header / Navbar -->
  <header>
    <div class="header-inner">
      <a href="index.html" class="logo-wrap" id="nav-logo">
        <img src="primary-logo.webp" alt="FutureWithAI Logo" class="logo-img">
      </a>
      <div class="search-bar">
        <i data-lucide="search" style="width:16px;height:16px;"></i>
        <input type="text" placeholder="Search product packs... (e.g. Health, PHP, Canva)" id="search-input" onkeyup="filterProducts(this.value)">
      </div>
      <div class="header-actions">
        <button class="cart-btn cart-toggle-trigger" id="cart-nav-btn">
          <i data-lucide="shopping-cart" style="width:18px;height:18px;"></i>
          Cart
          <span class="cart-count cart-badge">0</span>
        </button>
        <a href="https://chat.whatsapp.com/L7M5r6mMdoKEh3cvM5F1xr" target="_blank" class="whatsapp-btn">
          <i data-lucide="message-circle" style="width:16px;height:16px;"></i>
          <span>Join Community</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Category Nav -->
  <nav class="cat-nav">
    <div class="cat-nav-inner">
      <button class="cat-btn active" onclick="filterCat('all', this)">🏪 All Packs</button>
      <button class="cat-btn" onclick="filterCat('video-editing', this)">🎬 Video Editing</button>
      <button class="cat-btn" onclick="filterCat('editing-bundle', this)">🎞️ Editing Bundles</button>
      <button class="cat-btn" onclick="filterCat('web-software', this)">💻 Web Software</button>
      <button class="cat-btn" onclick="filterCat('digital-marketing', this)">📊 Digital Marketing</button>
      <button class="cat-btn" onclick="filterCat('business', this)">💼 Business & Courses</button>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="store-hero">
    <div class="container">
      <h1 class="hero-title">Individual <span>Product Store</span></h1>
      <p class="hero-sub">
        Explore individual, modular content packs compiled from our premium archives. Buy only what you need, with instant post-payment delivery.
      </p>
      
      <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
        <span class="hbadge"><i data-lucide="zap" style="width:12px;height:12px;"></i> Instant Delivery</span>
        <span class="hbadge"><i data-lucide="infinity" style="width:12px;height:12px;"></i> Lifetime Access</span>
        <span class="hbadge"><i data-lucide="shield" style="width:12px;height:12px;"></i> Secure Checkout</span>
      </div>
    </div>
  </section>

  <!-- Main Grid -->
  <div class="store-layout">
    <div class="products-grid" id="products-grid">
      {product_cards_html}
    </div>
  </div>

  <!-- Testimonials Section -->
  <section class="section" id="testimonials" style="background: rgba(10, 10, 10, 0.3); padding: 80px 0; border-top: 1px solid rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.05);">
    <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 24px;">
      <div class="section-header" style="text-align: center; margin: 0 auto 56px auto;">
        <span class="section-label" style="color: #ff8a00; font-size: 13px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase;">⭐ Customer Testimonials</span>
        <h2 class="section-title" style="font-family: 'Playfair Display', serif; font-size: clamp(28px, 4vw, 38px); color: #fff; margin-top: 8px; margin-bottom: 0;">What Creators & Developers Say</h2>
        <p class="section-desc" style="color: rgba(255,255,255,0.6); max-width: 600px; margin: 12px auto 0; font-size: 15px; line-height: 1.6;">Over 25,000+ customers have scaled their content creation and web development with our individual asset packs.</p>
      </div>

      <div class="review-grid">
        <!-- Review 1 -->
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"I bought the 500+ Animation explaining motivation videos. The quality is exceptional! It saved me at least 3 weeks of video rendering time. Delivered instantly after UPI payment."</p>
          <div class="review-author">
            <div class="review-avatar">AK</div>
            <div class="review-author-info">
              <span class="review-name">Amit Kumar</span>
              <span class="review-role">Patna · Content Creator</span>
            </div>
          </div>
        </div>

        <!-- Review 2 -->
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"The 400+ PHP scripts and 2700+ Elementor Pro Templates are a goldmine for web developers. I paid just ₹69 and ₹59. It's incredibly cheap for the huge value inside!"</p>
          <div class="review-author">
            <div class="review-avatar">SS</div>
            <div class="review-author-info">
              <span class="review-name">Sanjay Sharma</span>
              <span class="review-role">Pune · Web Developer</span>
            </div>
          </div>
        </div>

        <!-- Review 3 -->
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Excellent resource store! I downloaded the free Caravan Life and Dog reels bundles first to check, then purchased the space content and Gym reels. Fully satisfied with the quality!"</p>
          <div class="review-author">
            <div class="review-avatar">RV</div>
            <div class="review-author-info">
              <span class="review-name">Rohan Verma</span>
              <span class="review-role">Noida · Theme Page Owner</span>
            </div>
          </div>
        </div>

        <!-- Review 4 -->
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"This individual store is exactly what I wanted. I didn't want to buy the huge complete bundle since I only edit wellness shorts. Got the English Health Reels and Canva Infographics for ₹118 total. Superb!"</p>
          <div class="review-author">
            <div class="review-avatar">MD</div>
            <div class="review-author-info">
              <span class="review-name">Meera Das</span>
              <span class="review-role">Kolkata · Health Coach</span>
            </div>
          </div>
        </div>

        <!-- Review 5 -->
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Best purchase in 2026. The 21 Hrs course on manually testing web apps is very informative, explained step by step. Downloaded immediately via the access page."</p>
          <div class="review-author">
            <div class="review-avatar">JD</div>
            <div class="review-author-info">
              <span class="review-name">Jayesh D.</span>
              <span class="review-role">Mumbai · Software Engineer</span>
            </div>
          </div>
        </div>

        <!-- Review 6 -->
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Highly recommended. The transition packs and Glowing motion reels are top tier. I use them in almost every client video now. 10/10 value for money."</p>
          <div class="review-author">
            <div class="review-avatar">AT</div>
            <div class="review-author-info">
              <span class="review-name">Aryan Tiwari</span>
              <span class="review-role">Indore · Freelance Editor</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-top">
        <div>
          <div class="footer-logo">
            <img src="primary-logo.webp" alt="FutureWithAI Logo">
          </div>
          <p class="footer-desc">India's biggest digital product store — empowering creators, developers & agencies with premium resources.</p>
        </div>
        <div class="footer-col">
          <h4>Products</h4>
          <a href="index.html">Main Bundles</a>
          <a href="n8n-pack.html">n8n Automation Pack</a>
          <a href="video-editing.html">Video Editing Toolkit</a>
          <a href="mega-reels.html">Viral Reels Pack</a>
          <a href="web-apps.html">Web Apps Source Code</a>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <a href="about.html">About Us</a>
          <a href="refund.html">Cancellation & Refund</a>
          <a href="privacy.html">Privacy Policy</a>
          <a href="terms.html">Terms & Conditions</a>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-copy">© 2026 FutureWithAI · Powered by Anshuman Enterprises · All Rights Reserved</p>
        <a href="https://chat.whatsapp.com/L7M5r6mMdoKEh3cvM5F1xr" target="_blank" class="footer-whatsapp">
          💬 Join WhatsApp Community
        </a>
      </div>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      if (window.lucide) lucide.createIcons();
    });

    // Category filter
    function filterCat(cat, btn) {
      document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.prod-card').forEach(card => {
        card.style.display = (cat === 'all' || card.dataset.cat === cat) ? 'flex' : 'none';
      });
    }

    // Search filter
    function filterProducts(query) {
      const q = query.toLowerCase();
      document.querySelectorAll('.prod-card').forEach(card => {
        const name = card.dataset.name || '';
        card.style.display = name.includes(q) ? 'flex' : 'none';
      });
    }

    // Add to Cart Animation
    function addToCartAnimated(btn, id, name, price, img, link) {
      addToCart(id, name, price, img, link);
      const orig = btn.innerHTML;
      btn.innerHTML = '<i data-lucide="check" style="width:14px;height:14px;"></i> Added!';
      btn.classList.add('added');
      if (window.lucide) lucide.createIcons();
      setTimeout(() => {
        btn.innerHTML = orig;
        btn.classList.remove('added');
        if (window.lucide) lucide.createIcons();
      }, 2000);
    }

    // Quick Buy = add to cart + open cart
    function quickBuy(id, name, price, img, link) {
      addToCart(id, name, price, img, link);
      if (window.openCart) window.openCart();
    }
  </script>
</body>
</html>
""".replace("{product_cards_html}", product_cards_html)

    # Update index.html dynamically
    index_path = "index.html"
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            index_content = f.read()
            
        start_tag = "<!-- DYNAMIC_INDIVIDUAL_PRODUCTS_START -->"
        end_tag = "<!-- DYNAMIC_INDIVIDUAL_PRODUCTS_END -->"
        
        start_idx = index_content.find(start_tag)
        end_idx = index_content.find(end_tag)
        
        if start_idx != -1 and end_idx != -1:
            new_index_content = (
                index_content[:start_idx + len(start_tag)] + 
                "\n" + product_cards_html + "\n" + 
                index_content[end_idx:]
            )
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(new_index_content)
            print("index.html updated successfully with individual product cards.")
        else:
            print("Warning: DYNAMIC_INDIVIDUAL_PRODUCTS placeholder tags not found in index.html.")

if __name__ == "__main__":
    generate_catalog_html()
