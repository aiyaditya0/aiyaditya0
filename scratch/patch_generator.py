# Restore original file first to have a clean state before run
import os
import subprocess

# Run git checkout generate_individual_product_pages.py to get a clean slate
subprocess.run(["git", "checkout", "generate_individual_product_pages.py"], check=True)

with open('generate_individual_product_pages.py', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. Insert get_bonuses_html_and_values above generate_product_landing_pages
bonuses_logic = """def get_bonuses_html_and_values(category_id, name):
    # Mapping of categories/keywords to free bundles
    # Available Free Bundles from access.html:
    # 1. "Black Word with White Background Images" - Value: 999
    # 2. "Caravan Life Travel Reels" - Value: 1999
    # 3. "Dog Reels Bundle" - Value: 1999
    # 4. "Funny and Cute Cat Bundle" - Value: 1999
    # 5. "Health Infographic Post Canva" - Value: 1499
    # 6. "Lifestyle Reels Bundle" - Value: 1999
    # 7. "Luxury Hotels and Resorts" - Value: 1999
    # 8. "Travel Reels Bundle" - Value: 1999
    # 9. "5000+ MEGA REELS BUNDLE" - Value: 4999
    
    bonuses = []
    cat_lower = category_id.lower()
    name_lower = name.lower()
    
    if "video-editing" in cat_lower or "editing-bundle" in cat_lower or "editing" in cat_lower:
        bonuses = [
            {"name": "5000+ MEGA REELS BUNDLE", "value": 4999, "desc": "A massive collection of ready-to-use reels across fitness, motivation, luxury, and business niches to explode your social media growth."},
            {"name": "Caravan Life Travel Reels", "value": 1999, "desc": "Stunning cinematic travel reels of camper vans, road trips, and beautiful landscape scenery. 100% royalty-free."},
            {"name": "Dog & Cat Funny Reels", "value": 1999, "desc": "Adorable and funny dog/cat compilation video clips. Tap into the highly viral and profitable pet page page niche."},
            {"name": "Black Word Minimalist Quotes", "value": 999, "desc": "Minimalist text quotes on solid white & black backgrounds, perfect for stories, reels text, and highlighting cover pages."}
        ]
    elif "web-software" in cat_lower or "software" in cat_lower:
        bonuses = [
            {"name": "5000+ MEGA REELS BUNDLE", "value": 4999, "desc": "Use these high-converting viral shorts to promote your web applications and SaaS products on Instagram & TikTok."},
            {"name": "Health Infographic Post Canva", "value": 1499, "desc": "Fully editable infographics for Canva to post informative slide content, build authority, and drive premium traffic."},
            {"name": "Black Word Minimalist Quotes", "value": 999, "desc": "Sleek minimalist quote images on solid black and white background. Excellent for professional branding updates."}
        ]
    elif "digital-marketing" in cat_lower or "marketing" in cat_lower:
        bonuses = [
            {"name": "Health Infographic Post Canva", "value": 1499, "desc": "550+ fully customizable Canva infographic templates. Change fonts, colors, and branding details with a free Canva account."},
            {"name": "5000+ MEGA REELS BUNDLE", "value": 4999, "desc": "A premium archive of 5000+ viral edited reels to create automated theme pages and run high-converting ad campaigns."},
            {"name": "Lifestyle & Travel Reels Bundle", "value": 1999, "desc": "Premium aesthetic travel walkthroughs, luxury hotels, and sports car reels to build high-end personal brands."},
            {"name": "Black Word Minimalist Quotes", "value": 999, "desc": "Clean minimalist text graphics to maintain visual consistency and post professional design content daily."}
        ]
    else: # business / courses / other
        bonuses = [
            {"name": "5000+ MEGA REELS BUNDLE", "value": 4999, "desc": "Build massive organic traffic for your courses or dropshipping store using these ready-to-publish high-retention shorts."},
            {"name": "Health Infographic Post Canva", "value": 1499, "desc": "Fully customizable Canva templates to design and share educational slides and promote your products easily."},
            {"name": "Lifestyle Reels Bundle", "value": 1999, "desc": "Stunning luxury lifestyle, supercar, and hotel walkthrough reels to establish authority and trust on theme pages."}
        ]
        
    num_bonuses = len(bonuses)
    total_val = sum(b["value"] for b in bonuses)
    
    html = f'''
  <!-- {num_bonuses} FREE Bonuses Included Section -->
  <section class="section" id="bonuses">
    <div class="container">
      <div class="section-header" style="text-align: center; margin: 0 auto 48px auto; max-width: 700px;">
        <span class="section-label">{chr(0x1F381)} EXCLUSIVE BONUS INCLUSIONS</span>
        <h2 class="section-title">{num_bonuses} FREE Bonuses Included</h2>
        <p class="section-desc">
          Get \u20b9{total_val:,} worth of premium creator resources for zero extra cost.
        </p>
      </div>

      <div class="bonuses-container">'''
      
    for idx, b in enumerate(bonuses, 1):
        html += f'''
        <!-- Bonus {idx} -->
        <div class="bonus-card" style="border-color: rgba(255, 138, 0, 0.25);">
          <span class="bonus-tag">BONUS #{idx}</span>
          <span class="bonus-value-badge">Worth \u20b9{b["value"]:,} - FREE</span>
          <h3 class="bonus-card-title">{b["name"]}</h3>
          <p class="bonus-card-desc">{b["desc"]}</p>
        </div>'''
        
    html += '''
      </div>
    </div>
  </section>
'''
    return html, bonuses, total_val

"""

if "def get_bonuses_html_and_values" not in content:
    content = content.replace("def generate_product_landing_pages():", bonuses_logic + "\n" + "def generate_product_landing_pages():")
    print("Injected get_bonuses_html_and_values logic successfully!")

# 2. Modify generate_product_landing_pages() to call get_bonuses_html_and_values
target_call = 'stats_ribbon_html, benefits_grid_html, calculator_html, calculator_js, db_inclusions_html, faq_html = get_premium_content_for_category(p["category_id"], p["price"])'
replacement_call = target_call + '\n        bonuses_section_html, bonuses_list, bonuses_total_value = get_bonuses_html_and_values(p["category_id"], p["name"])'

if target_call in content and "bonuses_section_html" not in content:
    content = content.replace(target_call, replacement_call)
    print("Injected get_bonuses_html_and_values call successfully!")

# 3. Add value_items_html generation with exactly 12 spaces indentation
target_val_today = 'val_pay_today_price = f\'<div class="pay-today-price">\u20b9{p["price"]}</div>\''
val_items_logic = "\n" + \
"            # Build Value Items List\n" + \
"            value_items_html = f'''\n" + \
"              <div class=\\\"value-item\\\">\n" + \
"                <span>Premium Asset Pack ({p[\"name\"]})</span>\n" + \
"                <span style=\\\"text-decoration:line-through;color:var(--text-muted);\\\">\u20b92,999</span>\n" + \
"              </div>\n" + \
"              <div class=\\\"value-item\\\">\n" + \
"                <span>Commercial Resell License</span>\n" + \
"                <span style=\\\"text-decoration:line-through;color:var(--text-muted);\\\">\u20b91,499</span>\n" + \
"              </div>\n" + \
"              <div class=\\\"value-item\\\">\n" + \
"                <span>Lifetime Storage Sync Updates</span>\n" + \
"                <span style=\\\"text-decoration:line-through;color:var(--text-muted);\\\">\u20b9999</span>\n" + \
"              </div>'''\n" + \
"            for b in bonuses_list:\n" + \
"                value_items_html += f'''\n" + \
"              <div class=\\\"value-item\\\">\n" + \
"                <span>{b[\"name\"]} (Bonus)</span>\n" + \
"                <span style=\\\"text-decoration:line-through;color:var(--text-muted);\\\">\u20b9{b[\"value\"]:,}</span>\n" + \
"              </div>'''\n" + \
"            grand_total = 2999 + 1499 + 999 + bonuses_total_value\n" + \
"            value_items_html += f'''\n" + \
"              <div class=\\\"value-item total\\\">\n" + \
"                <span>Total Estimated Value:</span>\n" + \
"                <span>\u20b9{grand_total:,}</span>\n" + \
"              </div>'''\n"

if target_val_today in content and "value_items_html" not in content:
    content = content.replace(target_val_today, target_val_today + val_items_logic)
    print("Injected value_items_html logic successfully!")

# 4. Add bonuses CSS styles
css_target = "    .purchase-toast-meta {{ font-size: 10px; color: #27c93f; font-weight: 600; display: flex; align-items: center; gap: 4px; }}\n\n    /* Footer */"

css_replacement = """    .purchase-toast-meta {{ font-size: 10px; color: #27c93f; font-weight: 600; display: flex; align-items: center; gap: 4px; }}

    /* Bonuses Section */
    .bonuses-container {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
      margin-top: 40px;
    }}
    .bonus-card {{
      background: rgba(20, 20, 20, 0.55);
      border: 1.5px solid var(--border-color);
      border-radius: 24px;
      padding: 32px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: relative;
      overflow: hidden;
      transition: var(--transition-smooth);
    }}
    .bonus-card:hover {{
      border-color: var(--border-hover);
      box-shadow: var(--glow-primary);
      transform: translateY(-2px);
    }}
    .bonus-tag {{
      align-self: flex-start;
      background: linear-gradient(90deg, #ff8a00, #ffb347);
      color: #000;
      font-size: 10px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 20px;
      letter-spacing: 0.5px;
    }}
    .bonus-value-badge {{
      position: absolute;
      top: 32px;
      right: 32px;
      font-size: 12px;
      font-weight: 700;
      color: var(--primary);
    }}
    .bonus-card-title {{
      font-family: 'Playfair Display', serif;
      font-size: 20px;
      color: var(--text-white);
      margin-top: 4px;
    }}
    .bonus-card-desc {{
      font-size: 13.5px;
      color: var(--text-secondary);
      line-height: 1.5;
    }}

    /* Footer */"""

if css_target in content and ".bonuses-container" not in content:
    content = content.replace(css_target, css_replacement)
    print("Injected bonuses CSS successfully!")

# 5. Add media query responsive styles
media_target = "      .review-grid {{ grid-template-columns: repeat(2, 1fr); }}\n      #purchase-toast {{ width: calc(100% - 48px); left: 24px; }}"

media_replacement = """      .review-grid {{ grid-template-columns: repeat(2, 1fr); }}
      #purchase-toast {{ width: calc(100% - 48px); left: 24px; }}
      .bonuses-container {{ grid-template-columns: 1fr; }}"""

if media_target in content and "bonuses-container {{ grid-template-columns: 1fr; }}" not in content:
    content = content.replace(media_target, media_replacement)
    print("Injected media query responsive CSS successfully!")

# 6. Inject bonuses section into HTML page template
bonuses_section_placeholder = "  <!-- Value Box Section -->\n  <section class=\"value-sec\">"

bonuses_section_replacement = """  {bonuses_section_html}

  <!-- Value Box Section -->
  <section class="value-sec">"""

if bonuses_section_placeholder in content and "{bonuses_section_html}" not in content:
    content = content.replace(bonuses_section_placeholder, bonuses_section_replacement)
    print("Injected {bonuses_section_html} placeholder successfully!")

# 7. Update Value Box to list value_items_html
value_box_placeholder = """        <div class="value-list">
          <h3 style="font-family:'Playfair Display',serif;font-size:22px;color:#fff;margin-bottom:12px;">What This Deal Saves You:</h3>
          <div class="value-item">
            <span>Premium Asset Archive</span>
            <span style="text-decoration:line-through;color:var(--text-muted);">₹2,999</span>
          </div>
          <div class="value-item">
            <span>Commercial Resell License</span>
            <span style="text-decoration:line-through;color:var(--text-muted);">₹1,499</span>
          </div>
          <div class="value-item">
            <span>Lifetime Storage Sync Updates</span>
            <span style="text-decoration:line-through;color:var(--text-muted);">₹999</span>
          </div>
          <div class="value-item total">
            <span>Total Estimated Value:</span>
            <span>₹5,497</span>
          </div>
        </div>"""

value_box_replacement = """        <div class="value-list">
          <h3 style="font-family:'Playfair Display',serif;font-size:22px;color:#fff;margin-bottom:12px;">What This Deal Saves You:</h3>
          {value_items_html}
        </div>"""

if value_box_placeholder in content:
    content = content.replace(value_box_placeholder, value_box_replacement)
    print("Injected {value_items_html} placeholder successfully!")

with open('generate_individual_product_pages.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patching complete!")
