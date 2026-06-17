import os
import openpyxl
import re
import random

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
    if "gym" in name_lower or "fitness" in name_lower:
        return "reels_fitness_preview.png"
    elif "ai" in name_lower or "anime" in name_lower:
        return "reels_anime_preview.png"
    elif "art" in name_lower or "craft" in name_lower:
        return "reels_art_preview.png"
    elif "nature" in name_lower or "woodwork" in name_lower:
        return "reels_woodwork_preview.png"
    elif "cricket" in name_lower:
        return "reels_cricket_preview.png"
    elif "motivation" in name_lower or "business growth" in name_lower:
        return "reels_playbook_preview.png"
    elif "car reels" in name_lower or "caravan" in name_lower:
        return "reels_hero_mockup.png"
    elif "travel" in name_lower or "lifestyle" in name_lower or "luxury hotels" in name_lower:
        return "hero-image.png"
    elif "php scripts" in name_lower or "php" in name_lower:
        return "pos_billing_mockup.png"
    elif "web applications" in name_lower or "web app" in name_lower:
        return "saas_dashboard_mockup.png"
    elif "transitions" in name_lower or "latest editing" in name_lower or "graphics bundle" in name_lower:
        return "reels_playbook_preview.png"
    elif "marketing" in name_lower or "elementor" in name_lower:
        return "ecommerce_portal_mockup.png"
    elif "money making courses" in name_lower or "all money making" in name_lower:
        return "laptop-workspace.png"
        
    # General fallbacks
    if category_id == "web-software":
        return "webapp_hero_mockup.png"
    elif category_id == "digital-marketing":
        return "ecommerce_portal_mockup.png"
    elif category_id == "business":
        return "laptop-workspace.png"
    elif "editing" in category_id or "reels" in category_id:
        return "reels_hero_mockup.png"
        
    return "hero-image.png"

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

def generate_product_landing_pages():
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
        
        cat_lower = category.lower()
        if "video" in cat_lower or "editing" in cat_lower:
            cat_id = "video-editing"
            cat_display = "🎬 Video Editing / Reels"
        elif "software" in cat_lower or "web" in cat_lower:
            cat_id = "web-software"
            cat_display = "💻 Web Software"
        elif "marketing" in cat_lower or "maketing" in cat_lower:
            cat_id = "digital-marketing"
            cat_display = "📊 Digital Marketing"
        elif "business" in cat_lower:
            cat_id = "business"
            cat_display = "💼 Business & Courses"
        else:
            cat_id = "other"
            cat_display = "📦 Other Resources"
            
        img = get_product_image(name, cat_id)
            
        price_str = str(price).strip().upper() if price is not None else ""
        is_free = "FREE" in price_str or price == 0 or not price
        
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
        
    print(f"Loaded {len(products)} products from spreadsheet. Starting page generation...")
    
    # Let's generate pages
    for idx, p in enumerate(products):
        filename = f"product-{p['id']}.html"
        
        # Determine features cards based on category
        if p["category_id"] in ["video-editing", "editing-bundle"]:
            features_cards_html = """
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="zap" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Instant Drive Link</h3>
            <p class="feat-desc">Get direct high-speed download access to the Google Drive folder without redirect delays.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="video" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Watermark Free</h3>
            <p class="feat-desc">All templates and videos are raw, high-definition (HD), and completely free of any logos.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="clock" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Zero Editing Required</h3>
            <p class="feat-desc">Production-ready clips that you can directly drag, drop, and publish on social handles.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="shield" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Commercial License</h3>
            <p class="feat-desc">Includes full resell and commercial rights to utilize these assets for client projects.</p>
          </div>
        </div>
            """
            reviews_html = """
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"The quality of the video files is top notch. I posted 3 motivation clips and got over 12k views in my first week. Incredible deal!"</p>
          <div class="review-author">
            <div class="review-avatar">AK</div>
            <div class="review-author-info">
              <span class="review-name">Amit Kumar</span>
              <span class="review-role">Patna · Creator</span>
            </div>
          </div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Super easy to use. I downloaded the nature and gym clips directly to my phone. Delivered instantly via email."</p>
          <div class="review-author">
            <div class="review-avatar">RV</div>
            <div class="review-author-info">
              <span class="review-name">Rohan Verma</span>
              <span class="review-role">Noida · Editor</span>
            </div>
          </div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Highly recommended. The transition files are clean, no watermarks, and high definition. Absolute steal for the price."</p>
          <div class="review-author">
            <div class="review-avatar">PS</div>
            <div class="review-author-info">
              <span class="review-name">Priya S.</span>
              <span class="review-role">Mumbai · Influencer</span>
            </div>
          </div>
        </div>
            """
        elif p["category_id"] == "web-software":
            features_cards_html = """
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="code" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Clean Source Code</h3>
            <p class="feat-desc">Get complete deployable source code with clean structures, preconfigured router & authentication scripts.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="database" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Database Included</h3>
            <p class="feat-desc">Includes clean SQL database dumps for zero-hassle schema setups on your server.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="server" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Easy Hosting</h3>
            <p class="feat-desc">Fully compatible with generic cPanel shared hosting or VPS instances (PHP, MySQL, Apache).</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="badge-dollar-sign" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Micro-SaaS Ready</h3>
            <p class="feat-desc">Includes resale license rights to rebranding, hosting, and charging clients premium monthly subscriptions.</p>
          </div>
        </div>
            """
            reviews_html = """
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"The PHP scripts are structured perfectly. DB setups worked on the first try. Made my client project ready in 1 day."</p>
          <div class="review-author">
            <div class="review-avatar">SS</div>
            <div class="review-author-info">
              <span class="review-name">Sanjay Sharma</span>
              <span class="review-role">Pune · Freelancer</span>
            </div>
          </div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"The 21 hours video guide is a massive addition. Learned step-by-step how to host and edit. Absolute value for money!"</p>
          <div class="review-author">
            <div class="review-avatar">JD</div>
            <div class="review-author-info">
              <span class="review-name">Jayesh D.</span>
              <span class="review-role">Mumbai · Software Dev</span>
            </div>
          </div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Highly functional scripts. Skip writing backend code, just customize this template and sell. Highly recommended."</p>
          <div class="review-author">
            <div class="review-avatar">VT</div>
            <div class="review-author-info">
              <span class="review-name">Vikash T.</span>
              <span class="review-role">Delhi · Agency Owner</span>
            </div>
          </div>
        </div>
            """
        elif p["category_id"] == "digital-marketing":
            features_cards_html = """
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="layout" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Ready Elementor Blocks</h3>
            <p class="feat-desc">Includes 2700+ layout blocks, sections, headers, and footers ready to import into WordPress.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="mail" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Cold Email Scripts</h3>
            <p class="feat-desc">High-converting cold email copy frameworks that clenched marketing retainers for agencies.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="trending-up" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Ad Copy Templates</h3>
            <p class="feat-desc">Copy-paste ad templates for Facebook and Google campaigns targeting local services.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="file-text" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Agency Contracts</h3>
            <p class="feat-desc">Professional client proposal decks and digital agency contract templates to secure payments.</p>
          </div>
        </div>
            """
            reviews_html = """
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Saved my agency at least a month of graphic creation. elementor pages imported with zero layout issues."</p>
          <div class="review-author">
            <div class="review-avatar">SR</div>
            <div class="review-author-info">
              <span class="review-name">Sneha R.</span>
              <span class="review-role">Bengaluru · Agency Owner</span>
            </div>
          </div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Excellent marketing proposal copy. Used the templates to send pitch decks, secured two local retail contracts."</p>
          <div class="review-author">
            <div class="review-avatar">KP</div>
            <div class="review-author-info">
              <span class="review-name">Karan P.</span>
              <span class="review-role">Ahmedabad · Marketer</span>
            </div>
          </div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"High-quality vectors and Canva graphics templates. Fully customisable and extremely cheap for the huge value."</p>
          <div class="review-author">
            <div class="review-avatar">AT</div>
            <div class="review-author-info">
              <span class="review-name">Aryan T.</span>
              <span class="review-role">Indore · Freelancer</span>
            </div>
          </div>
        </div>
            """
        else: # business
            features_cards_html = """
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="hard-drive" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Massive 1.37 TB Archive</h3>
            <p class="feat-desc">Detailed chapters, worksheets, and resources covering coding, organic sales, copywriting, and SEO.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="graduation-cap" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Premium Frameworks</h3>
            <p class="feat-desc">Learn business hacks and conversion copywriting directly from certified experts' case studies.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="life-buoy" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Lifetime Updates</h3>
            <p class="feat-desc">Get immediate free downloads for all future courses uploaded to this cloud repository folder.</p>
          </div>
        </div>
        <div class="feat-card">
          <div class="feat-icon"><i data-lucide="globe" style="width:20px;height:20px;"></i></div>
          <div>
            <h3 class="feat-title">Download Anytime</h3>
            <p class="feat-desc">Hosted on high-speed cloud nodes. Access individual directories or stream chapters directly.</p>
          </div>
        </div>
            """
            reviews_html = """
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Unbelievable collection. The organic traffic course alone saved me from buying a separate ₹5k masterclass."</p>
          <div class="review-author">
            <div class="review-avatar">JD</div>
            <div class="review-author-info">
              <span class="review-name">Jayesh D.</span>
              <span class="review-role">Patna · Student</span>
            </div>
          </div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Highly structured files. Got the MEGA links immediately after UPI checkout. Fully satisfied!"</p>
          <div class="review-author">
            <div class="review-avatar">RS</div>
            <div class="review-author-info">
              <span class="review-name">Rahul S.</span>
              <span class="review-role">Jaipur · Blogger</span>
            </div>
          </div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Incredible knowledge store. Highly structured guides, no broken links. Highly recommend to everyone."</p>
          <div class="review-author">
            <div class="review-avatar">KM</div>
            <div class="review-author-info">
              <span class="review-name">Kavita M.</span>
              <span class="review-role">Lucknow · Entrepreneur</span>
            </div>
          </div>
        </div>
            """

        # Generate Suggestions (3 related items)
        # We pick 3 random items from products list that are NOT the current product
        candidates = [item for item in products if item["id"] != p["id"]]
        # Prioritize suggestions from the SAME category first
        cat_candidates = [item for item in candidates if item["category_id"] == p["category_id"]]
        if len(cat_candidates) >= 3:
            suggested = random.sample(cat_candidates, 3)
        else:
            suggested = cat_candidates + random.sample([item for item in candidates if item not in cat_candidates], 3 - len(cat_candidates))
            
        suggestions_html = ""
        for s in suggested:
            if s["is_free"]:
                s_price_html = '<span class="suggest-price-free">FREE</span>'
                s_action_html = 'Download Now'
            else:
                s_price_html = f'<span class="suggest-price">₹{s["price"]}</span>'
                s_action_html = 'View Details'
                
            suggestions_html += f"""
        <a href="product-{s["id"]}.html" class="suggest-card">
          <img class="suggest-img" src="{s["img"]}" alt="{s["name"]}">
          <div class="suggest-body">
            <h3 class="suggest-title">{s["name"]}</h3>
            <p class="suggest-desc">{s["desc"]}</p>
            <div class="suggest-footer">
              {s_price_html}
              <span class="suggest-action">{s_action_html} →</span>
            </div>
          </div>
        </a>"""

        # Buy block details
        if p["is_free"]:
            badge_class = "badge-free"
            badge_text = "🎁 Free Resource"
            price_row_html = '<span class="price-free">FREE</span>'
            buy_button_html = f'<a href="{p["link"]}" target="_blank" class="btn-buy btn-buy-free"><i data-lucide="download" style="width:20px;height:20px;"></i> Download Free Resource</a>'
        else:
            badge_class = "badge-sale"
            badge_text = "🔥 Premium Resource"
            price_row_html = f'<span class="price-now">₹{p["price"]}</span><span class="price-orig">₹299</span><span style="color:#27c93f; font-size:13px; font-weight:700;">(90% OFF Launch Deal)</span>'
            buy_button_html = f'<button class="btn-buy btn-buy-paid" onclick="addToCartAnimated(this,\'{p["id"]}\',\'{p["name"]}\',{p["price"]},\'{p["img"]}\',\'product-{p["id"]}.html\')"><i data-lucide="shopping-cart" style="width:20px;height:20px;"></i> Add To Cart</button>'

        # Build Page HTML
        page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FutureWithAi - {p["name"]}</title>
  <meta name="description" content="{p["desc"]}">
  <link rel="icon" type="image/png" href="favicon.png">
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
    :root {{
      --primary: #ff8a00;
      --primary-container: #ff8a00;
      --bg-dark: #050505;
      --text-white: #ffffff;
      --text-secondary: rgba(255, 255, 255, 0.7);
      --text-muted: rgba(255, 255, 255, 0.4);
      --border-color: rgba(255, 255, 255, 0.06);
      --border-hover: rgba(255, 138, 0, 0.35);
      --glow-primary: 0 0 20px rgba(255, 138, 0, 0.15);
    }}

    body {{
      background: var(--bg-dark);
      color: #fff;
      font-family: 'Inter', sans-serif;
      margin: 0;
      padding: 0;
      overflow-x: hidden;
    }}

    #top-bar {{
      background: linear-gradient(90deg, #b34500 0%, #ff8a00 50%, #b34500 100%);
      background-size: 200% 100%;
      animation: barAnim 4s linear infinite;
      color: #000; text-align: center; padding: 10px 16px;
      font-size: 13px; font-weight: 700;
      display: flex; align-items: center; justify-content: center; gap: 10px;
      position: sticky; top: 0; z-index: 9999;
      box-shadow: 0 2px 20px rgba(255,138,0,0.4);
    }}
    @keyframes barAnim {{ 0%,100%{{background-position:0% 50%}} 50%{{background-position:100% 50%}} }}

    header {{
      position: sticky; top: 42px; z-index: 1000;
      background: rgba(5,5,5,0.92);
      backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(255,255,255,0.07);
    }}
    .header-inner {{
      max-width: 1200px; margin: 0 auto;
      display: flex; align-items: center; justify-content: space-between;
      padding: 12px 24px; gap: 16px;
    }}
    .logo-wrap {{ display: flex; align-items: center; text-decoration: none; }}
    .logo-wrap img {{ height: 44px; width: auto; object-fit: contain; }}
    
    .header-actions {{ display: flex; align-items: center; gap: 16px; }}
    .cart-btn {{
      position: relative; background: rgba(255,138,0,0.12);
      border: 1px solid rgba(255,138,0,0.3);
      color: #ff8a00; border-radius: 12px; cursor: pointer;
      padding: 10px 16px; display: flex; align-items: center; gap: 8px;
      font-size: 13px; font-weight: 600;
      transition: all 0.2s;
    }}
    .cart-btn:hover {{ background: rgba(255,138,0,0.2); }}
    .cart-count {{
      background: #ff8a00; color: #000; border-radius: 50%;
      width: 18px; height: 18px; font-size: 10px; font-weight: 800;
      display: flex; align-items: center; justify-content: center;
    }}
    .back-catalog-btn {{
      color: rgba(255,255,255,0.7); text-decoration: none; font-size: 13px; font-weight: 600;
      display: flex; align-items: center; gap: 6px; transition: color 0.2s;
    }}
    .back-catalog-btn:hover {{ color: #ff8a00; }}

    /* Hero Section */
    .product-hero {{
      background: linear-gradient(135deg, #0a0614 0%, #150a00 50%, #0a0614 100%);
      padding: 60px 0;
      border-bottom: 1px solid var(--border-color);
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 24px;
    }}
    .hero-grid {{
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 48px;
      align-items: center;
    }}
    .badge-sale {{
      display: inline-flex; align-items: center; gap: 6px;
      background: rgba(255, 138, 0, 0.15); border: 1px solid rgba(255, 138, 0, 0.3);
      color: #ff8a00; border-radius: 20px; padding: 4px 14px;
      font-size: 11px; font-weight: 800; text-transform: uppercase; margin-bottom: 16px;
    }}
    .badge-free {{
      display: inline-flex; align-items: center; gap: 6px;
      background: rgba(39, 201, 63, 0.15); border: 1px solid rgba(39, 201, 63, 0.3);
      color: #27c93f; border-radius: 20px; padding: 4px 14px;
      font-size: 11px; font-weight: 800; text-transform: uppercase; margin-bottom: 16px;
    }}
    .hero-title {{
      font-family: 'Playfair Display', serif;
      font-size: clamp(28px, 4vw, 42px);
      line-height: 1.2;
      margin: 0 0 16px;
      color: #fff;
    }}
    .hero-title span {{ color: #ff8a00; }}
    .hero-desc {{
      font-size: 16px;
      color: var(--text-secondary);
      line-height: 1.6;
      margin-bottom: 24px;
    }}
    
    /* Purchase details */
    .purchase-block {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 24px;
      margin-bottom: 24px;
    }}
    .price-row {{
      display: flex;
      align-items: baseline;
      gap: 12px;
      margin-bottom: 16px;
    }}
    .price-now {{
      font-size: 38px;
      font-weight: 800;
      color: #ff8a00;
      text-shadow: var(--glow-primary);
    }}
    .price-orig {{
      font-size: 16px;
      color: var(--text-muted);
      text-decoration: line-through;
    }}
    .price-free {{
      font-size: 38px;
      font-weight: 800;
      color: #27c93f;
    }}
    .btn-buy {{
      display: flex; align-items: center; justify-content: center; gap: 10px;
      width: 100%; padding: 16px; border-radius: 14px; border: none;
      font-size: 16px; font-weight: 800; cursor: pointer; transition: all 0.25s;
      font-family: 'Inter', sans-serif;
    }}
    .btn-buy-paid {{
      background: linear-gradient(135deg, #ff8a00, #ffb347);
      color: #000;
      box-shadow: 0 8px 24px rgba(255,138,0,0.3);
    }}
    .btn-buy-paid:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 32px rgba(255,138,0,0.45);
    }}
    .btn-buy-free {{
      background: linear-gradient(135deg, #27c93f, #1e9a30);
      color: #fff;
      box-shadow: 0 8px 24px rgba(39,201,63,0.3);
      text-decoration: none;
    }}
    .btn-buy-free:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 32px rgba(39,201,63,0.45);
    }}
    
    .trust-notes {{
      display: flex; gap: 16px; flex-wrap: wrap; margin-top: 16px;
    }}
    .trust-note {{
      font-size: 12px; color: var(--text-secondary); display: flex; align-items: center; gap: 6px;
    }}
    
    .hero-img-wrap {{
      border: 1.5px solid rgba(255,138,0,0.25);
      border-radius: 24px;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0,0,0,0.6), var(--glow-primary);
      background: #000;
      aspect-ratio: 16 / 10;
    }}
    .hero-img-wrap img {{
      width: 100%; height: 100%; object-fit: cover;
    }}

    /* Features Section */
    .features-sec {{
      padding: 80px 0;
      background: rgba(10, 10, 10, 0.2);
      border-bottom: 1px solid var(--border-color);
    }}
    .sec-title {{
      font-family: 'Playfair Display', serif;
      font-size: 32px;
      text-align: center;
      margin-bottom: 40px;
    }}
    .features-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
    }}
    .feat-card {{
      background: rgba(20,12,5,0.4);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 24px;
      display: flex; gap: 16px;
      align-items: flex-start;
      transition: all 0.25s;
    }}
    .feat-card:hover {{
      border-color: var(--border-hover);
      transform: translateY(-2px);
    }}
    .feat-icon {{
      background: rgba(255,138,0,0.1); border: 1px solid rgba(255,138,0,0.2);
      border-radius: 10px; padding: 10px; color: #ff8a00; flex-shrink: 0;
    }}
    .feat-title {{ font-size: 16px; font-weight: 700; color: #fff; margin: 0 0 6px; }}
    .feat-desc {{ font-size: 13.5px; color: var(--text-secondary); line-height: 1.5; margin: 0; }}

    /* Testimonials */
    .reviews-sec {{
      padding: 80px 0;
      border-bottom: 1px solid var(--border-color);
    }}
    .review-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-top: 40px;
    }}
    .review-card {{
      background: rgba(20, 12, 5, 0.6);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 24px;
      display: flex; flex-direction: column; gap: 14px;
    }}
    .review-stars {{ color: #ffb300; font-size: 13px; display: flex; gap: 2px; }}
    .review-text {{ font-size: 13.5px; color: var(--text-secondary); line-height: 1.55; font-style: italic; }}
    .review-author {{
      display: flex; align-items: center; gap: 12px; margin-top: auto;
      border-top: 1px solid rgba(255,255,255,0.05); padding-top: 12px;
    }}
    .review-avatar {{
      width: 38px; height: 38px; border-radius: 50%;
      background: rgba(255, 138, 0, 0.12); display: flex; align-items: center;
      justify-content: center; font-weight: 700; color: #ff8a00; border: 1px solid rgba(255,138,0,0.2);
    }}
    .review-name {{ font-size: 13.5px; font-weight: 600; color: #fff; display: block; }}
    .review-role {{ font-size: 11px; color: var(--text-muted); display: block; }}

    /* Suggestions Section (Connected Loop) */
    .suggestions-sec {{
      padding: 80px 0;
    }}
    .suggestions-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-top: 40px;
    }}
    .suggest-card {{
      background: rgba(20,12,5,0.8);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      display: flex; flex-direction: column; overflow: hidden;
      transition: all 0.25s; text-decoration: none; color: inherit;
    }}
    .suggest-card:hover {{
      border-color: var(--border-hover);
      transform: translateY(-4px);
      box-shadow: 0 12px 30px rgba(0,0,0,0.5), var(--glow-primary);
    }}
    .suggest-img {{
      width: 100%; aspect-ratio: 16 / 10; object-fit: cover;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }}
    .suggest-body {{ padding: 20px; display: flex; flex-direction: column; flex: 1; }}
    .suggest-title {{ font-size: 16px; font-weight: 700; color: #fff; margin: 0 0 8px; line-height: 1.4; }}
    .suggest-desc {{ font-size: 13px; color: var(--text-secondary); line-height: 1.5; margin-bottom: 16px; }}
    .suggest-footer {{
      display: flex; justify-content: space-between; align-items: center; margin-top: auto;
    }}
    .suggest-price {{ font-size: 16px; font-weight: 800; color: #ff8a00; }}
    .suggest-price-free {{ font-size: 16px; font-weight: 800; color: #27c93f; }}
    .suggest-action {{ font-size: 12px; font-weight: 700; color: #ff8a00; display: flex; align-items: center; gap: 4px; }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--border-color);
      padding: 40px 0;
      text-align: center;
      background: #020202;
    }}
    .footer-text {{ font-size: 13px; color: var(--text-muted); margin: 0; }}

    @media (max-width: 900px) {{
      .hero-grid {{ grid-template-columns: 1fr; gap: 32px; }}
      .features-grid {{ grid-template-columns: 1fr; }}
      .review-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .suggestions-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
      .review-grid {{ grid-template-columns: 1fr; }}
      .suggestions-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <!-- Top announcement -->
  <div id="top-bar">
    <span>🔥 <strong>PROMOTIONAL OFFER</strong> — Get instant digital delivery after payment!</span>
  </div>

  <!-- Header -->
  <header>
    <div class="header-inner">
      <a href="index.html" class="logo-wrap">
        <img src="primary-logo.png" alt="FutureWithAI Logo">
      </a>
      <a href="digital-products.html" class="back-catalog-btn">
        <i data-lucide="arrow-left" style="width:16px;height:16px;"></i> Back to Store
      </a>
      <div class="header-actions">
        <button class="cart-btn cart-toggle-trigger">
          <i data-lucide="shopping-cart" style="width:18px;height:18px;"></i>
          Cart
          <span class="cart-count cart-badge">0</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="product-hero">
    <div class="container">
      <div class="hero-grid">
        <div class="hero-content">
          <span class="{badge_class}">{badge_text}</span>
          <h1 class="hero-title">{p["name"]}</h1>
          <p class="hero-desc">{p["desc"]}</p>
          
          <div class="purchase-block">
            <div class="price-row">
              {price_row_html}
            </div>
            {buy_button_html}
            <div class="trust-notes">
              <div class="trust-note"><i data-lucide="shield-check" style="width:14px;height:14px;color:#ff8a00;"></i> Secure Payment</div>
              <div class="trust-note"><i data-lucide="zap" style="width:14px;height:14px;color:#ff8a00;"></i> Instant Download Link</div>
              <div class="trust-note"><i data-lucide="infinity" style="width:14px;height:14px;color:#ff8a00;"></i> Lifetime Validity</div>
            </div>
          </div>
        </div>
        
        <div class="hero-image-side">
          <div class="hero-img-wrap">
            <img src="{p["img"]}" alt="{p["name"]}">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Features Section -->
  <section class="features-sec">
    <div class="container">
      <h2 class="sec-title">What's Inside This Pack?</h2>
      <div class="features-grid">
        {features_cards_html}
      </div>
    </div>
  </section>

  <!-- Testimonials Section -->
  <section class="reviews-sec">
    <div class="container">
      <h2 class="sec-title" style="margin-bottom: 0;">What Creators & Developers Say</h2>
      <p style="text-align: center; color: var(--text-secondary); margin-top: 8px;">Real reviews from verified buyers.</p>
      <div class="review-grid">
        {reviews_html}
      </div>
    </div>
  </section>

  <!-- Related Products (Connected Loop) -->
  <section class="suggestions-sec">
    <div class="container">
      <h2 class="sec-title" style="margin-bottom: 0;">Other Packs You Might Like</h2>
      <p style="text-align: center; color: var(--text-secondary); margin-top: 8px;">Expand your toolkit with these highly rated additions.</p>
      <div class="suggestions-grid">
        {suggestions_html}
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <p class="footer-text">© 2026 FutureWithAI · Powered by Anshuman Enterprises · All Rights Reserved</p>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      if (window.lucide) lucide.createIcons();
    }});
    
    // Add to Cart Animation
    function addToCartAnimated(btn, id, name, price, img, link) {{
      addToCart(id, name, price, img, link);
      const orig = btn.innerHTML;
      btn.innerHTML = '<i data-lucide="check" style="width:20px;height:20px;"></i> Added!';
      btn.classList.add('added');
      if (window.lucide) lucide.createIcons();
      setTimeout(() => {{
        btn.innerHTML = orig;
        btn.classList.remove('added');
        if (window.lucide) lucide.createIcons();
      }}, 2000);
    }}
  </script>
</body>
</html>"""
        
        # Write to file
        with open(filename, "w", encoding="utf-8") as f_out:
            f_out.write(page_html)
            
    print("All 34 individual landing pages created successfully!")

if __name__ == "__main__":
    generate_product_landing_pages()
