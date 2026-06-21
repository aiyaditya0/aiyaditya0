import os
import re

def patch_page(filepath, filename):
    print(f"Patching: {filename}")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Image maps for each page
    img_map = {
        "video-editing.html": "video-editing-assets/hero-toolkit-zkCHdDKW.webp",
        "mega-reels.html": "reels_hero_mockup.webp",
        "n8n-pack.html": "hero-image.webp",
        "n8n-workflow-automation.html": "n8n_hero_mockup.webp",
        "digital-marketing-bundle.html": "laptop-workspace.webp",
        "web-apps.html": "webapp_hero_mockup.webp"
    }
    img = img_map.get(filename, "hero-image.webp")

    # Product details maps for default pricing button onclick arguments
    prod_map = {
        "video-editing.html": ("video-editing", "Ultimate Video Editing Toolkit", 199),
        "mega-reels.html": ("mega-reels", "100,000+ Viral Reels Goldmine Pack", 99),
        "n8n-pack.html": ("n8n-pack", "n8n Automation Pack (2000+ Workflows)", 99),
        "n8n-workflow-automation.html": ("n8n-automation-enterprise", "14000+ n8n Workflow Automation (Enterprise)", 349),
        "digital-marketing-bundle.html": ("digital-marketing-bundle", "Full Digital Marketing Resource Bundle (700+)", 499),
        "web-apps.html": ("web-apps", "1500+ Manually Tested Web App Pack", 199)
    }
    p_id, p_name, p_price = prod_map.get(filename, ("test-product", "Test Product", 99))

    # 1. Mute local purchase simulation functions to let cart.js handle them globally without duplicate loops
    pattern_sim = r'function startPurchaseNotifs\(\)\s*\{.*?setTimeout\(showNext,\s*\d+\);\s*\}'
    content = re.sub(pattern_sim, 'function startPurchaseNotifs() {\n      // Handled globally by cart.js\n    }', content, flags=re.DOTALL)
    
    # 2. Modify selectTier pricing update script calls
    # Convert hero, banner, and final checkout CTA buttons to use buyNow directly
    content = content.replace("bannerCta.setAttribute('onclick', `addToCart", "bannerCta.setAttribute('onclick', `buyNow")
    content = content.replace("navCta.setAttribute('onclick', `addToCart", "navCta.setAttribute('onclick', `buyNow")
    content = content.replace("navCta.innerHTML = `Add To Cart @ ₹${tier.price}", "navCta.innerHTML = `Buy Now @ ₹${tier.price} <i data-lucide=\"zap\" style=\"width: 14px; height: 14px;\"></i>` //")
    content = content.replace("heroCta.setAttribute('onclick', `addToCart", "heroCta.setAttribute('onclick', `buyNow")
    content = content.replace("heroCta.innerHTML = `ADD TO CART @ ₹${tier.price}", "heroCta.innerHTML = `BUY NOW @ ₹${tier.price} <i data-lucide=\"zap\"></i>` //")
    content = content.replace("finalCta.setAttribute('onclick', `addToCart", "finalCta.setAttribute('onclick', `buyNow")
    content = content.replace("finalCta.innerHTML = `🎬 ADD TO CART NOW @ ₹${tier.price} →`", "finalCta.innerHTML = `⚡ BUY NOW @ ₹${tier.price} →` //")
    content = content.replace("ctaBtn.setAttribute('onclick', `addToCart", "ctaBtn.setAttribute('onclick', `buyNow")
    content = content.replace("calcCta.setAttribute('onclick', `addToCart", "calcCta.setAttribute('onclick', `buyNow")

    # Replace specific pricing card CTA logic in selectTier to update the two buttons:
    old_val_cta_block = """      // Update value comparison CTA button
      const valCta = document.querySelector('.value-pay-today .btn-primary');
      if (valCta) {
        valCta.setAttribute('onclick', `addToCart('${tier.id}', '${tier.name}', ${tier.price}, '""" + img + """', '""" + filename + """'); return false;`);
        valCta.innerHTML = `ADD TO CART @ ₹${tier.price} <i data-lucide="shopping-cart"></i>`;
        if (window.lucide) lucide.createIcons();
      }"""
      
    new_val_cta_block = """      // Update pricing comparison buttons
      const pricingAddBtn = document.querySelector('.btn-add-cart-detail');
      if (pricingAddBtn) {
        pricingAddBtn.setAttribute('onclick', `addToCart('${tier.id}', '${tier.name}', ${tier.price}, '""" + img + """', '""" + filename + """'); return false;`);
      }
      const pricingBuyBtn = document.querySelector('.btn-buy-now-detail');
      if (pricingBuyBtn) {
        pricingBuyBtn.setAttribute('onclick', `buyNow('${tier.id}', '${tier.name}', ${tier.price}, '""" + img + """', '""" + filename + """'); return false;`);
        pricingBuyBtn.innerHTML = `⚡ Buy Now @ ₹${tier.price}`;
      }"""
      
    content = content.replace(old_val_cta_block, new_val_cta_block)
    
    # Also support alternate style updates for other files
    content = content.replace(
        "valCta.setAttribute('onclick', `addToCart('${tier.id}', '${tier.name}', ${tier.price},", 
        "// valCta.setAttribute"
    )

    # 3. Replace Static CTA Buttons in the HTML
    # Hero CTA
    content = content.replace(
        f"onclick=\"addToCart('{p_id}', '{p_name}', {p_price}, '{img}', '{filename}'); return false;\" class=\"btn-primary\" id=\"hero-cta-primary\"",
        f"onclick=\"buyNow('{p_id}', '{p_name}', {p_price}, '{img}', '{filename}'); return false;\" class=\"btn-primary\" id=\"hero-cta-primary\""
    )
    content = content.replace(
        f"ADD TO CART @ ₹{p_price} <i data-lucide=\"shopping-cart\"></i>",
        f"BUY NOW @ ₹{p_price} <i data-lucide=\"zap\"></i>"
    )
    
    # Navbar CTA
    content = content.replace(
        f"onclick=\"addToCart('{p_id}', '{p_name}', {p_price}, '{img}', '{filename}'); return false;\" class=\"nav-cta\" id=\"nav-cta-btn\"",
        f"onclick=\"buyNow('{p_id}', '{p_name}', {p_price}, '{img}', '{filename}'); return false;\" class=\"nav-cta\" id=\"nav-cta-btn\""
    )
    content = content.replace(
        f"Add To Cart <i data-lucide=\"plus\" style=\"width: 14px; height: 14px;\"></i>",
        f"Buy Now <i data-lucide=\"zap\" style=\"width: 14px; height: 14px;\"></i>"
    )
    content = content.replace(
        f"Add To Cart @ ₹{p_price} <i data-lucide=\"plus\" style=\"width: 14px; height: 14px;\"></i>",
        f"Buy Now @ ₹{p_price} <i data-lucide=\"zap\" style=\"width: 14px; height: 14px;\"></i>"
    )

    # Pricing comparison single button to double button
    old_pricing_cta = f"""          <a href="#" onclick="addToCart('{p_id}', '{p_name}', {p_price}, '{img}', '{filename}'); return false;" class="btn-primary" id="pricing-cta-btn" style="text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 8px;">
            🤖 ADD TO CART @ ₹{p_price} →
          </a>"""
    if old_pricing_cta in content:
        new_pricing_cta = f"""          <div class="buy-actions-wrapper" style="display:flex; gap:12px; width:100%; margin-top:8px;">
            <a href="#" class="btn-primary btn-buy-now-detail" style="flex:1.8; justify-content: center; gap: 8px; font-size: 15px; padding: 16px; background: linear-gradient(135deg, #ff8a00, #ffb347); border: none; color: #000; font-weight: 800; text-decoration:none; box-shadow:0 4px 12px rgba(255,138,0,0.2);" onclick="buyNow('{p_id}', '{p_name}', {p_price}, '{img}', '{filename}'); return false;">
              ⚡ Buy Now @ ₹{p_price}
            </a>
            <a href="#" class="btn-primary btn-add-cart-detail" style="flex:1; justify-content: center; gap: 8px; font-size: 15px; padding: 16px; background: rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); color:#fff; text-decoration:none;" onclick="addToCart('{p_id}', '{p_name}', {p_price}, '{img}', '{filename}'); return false;">
              🛒 Add to Cart
            </a>
          </div>"""
        content = content.replace(old_pricing_cta, new_pricing_cta)

    # Handle alternate pricing CTA format (e.g. video-editing.html, web-apps.html, mega-reels.html)
    old_pricing_cta_alt = f"""          <a href="#" onclick="addToCart('{p_id}', '{p_name}', {p_price}, '{img}', '{filename}'); return false;" class="btn-primary" style="width: 100%; justify-content: center; gap: 8px;">
            ADD TO CART @ ₹{p_price} <i data-lucide="shopping-cart"></i>
          </a>"""
    if old_pricing_cta_alt in content:
        new_pricing_cta_alt = f"""          <div class="buy-actions-wrapper" style="display:flex; gap:12px; width:100%; margin-top:8px;">
            <a href="#" class="btn-primary btn-buy-now-detail" style="flex:1.8; justify-content: center; gap: 8px; font-size: 15px; padding: 16px; background: linear-gradient(135deg, #ff8a00, #ffb347); border: none; color: #000; font-weight: 800; text-decoration:none; box-shadow:0 4px 12px rgba(255,138,0,0.2);" onclick="buyNow('{p_id}', '{p_name}', {p_price}, '{img}', '{filename}'); return false;">
              ⚡ Buy Now @ ₹{p_price}
            </a>
            <a href="#" class="btn-primary btn-add-cart-detail" style="flex:1; justify-content: center; gap: 8px; font-size: 15px; padding: 16px; background: rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); color:#fff; text-decoration:none;" onclick="addToCart('{p_id}', '{p_name}', {p_price}, '{img}', '{filename}'); return false;">
              🛒 Add to Cart
            </a>
          </div>"""
        content = content.replace(old_pricing_cta_alt, new_pricing_cta_alt)

    # Specific replace for video-editing.html pricing block
    old_ve_pricing = """        <a href="#" class="btn-primary" style="width: 100%; justify-content: center; gap: 8px; font-size: 16px; padding: 18px;" onclick="addToCart('video-editing', 'Ultimate Video Editing Toolkit', 199, 'video-editing-assets/hero-toolkit-zkCHdDKW.webp', 'video-editing.html'); return false;">
          🎬 ADD TO CART @ ₹199 →
        </a>"""
    new_ve_pricing = """        <div class="buy-actions-wrapper" style="display:flex; gap:12px; width:100%; margin-top:8px;">
          <a href="#" class="btn-primary btn-buy-now-detail" style="flex:1.8; justify-content: center; gap: 8px; font-size: 15px; padding: 16px; background: linear-gradient(135deg, #ff8a00, #ffb347); border: none; color: #000; font-weight: 800; text-decoration:none; box-shadow:0 4px 12px rgba(255,138,0,0.2);" onclick="buyNow('video-editing', 'Ultimate Video Editing Toolkit', 199, 'video-editing-assets/hero-toolkit-zkCHdDKW.webp', 'video-editing.html'); return false;">
            ⚡ Buy Now @ ₹199
          </a>
          <a href="#" class="btn-primary btn-add-cart-detail" style="flex:1; justify-content: center; gap: 8px; font-size: 15px; padding: 16px; background: rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); color:#fff; text-decoration:none;" onclick="addToCart('video-editing', 'Ultimate Video Editing Toolkit', 199, 'video-editing-assets/hero-toolkit-zkCHdDKW.webp', 'video-editing.html'); return false;">
            🛒 Add to Cart
          </a>
        </div>"""
    content = content.replace(old_ve_pricing, new_ve_pricing)

    # Specific replace for digital-marketing-bundle.html pricing block
    old_dm_pricing = """          <a href="#" onclick="addToCart('digital-marketing-bundle','Full Digital Marketing Resource Bundle (700+)',499,'laptop-workspace.webp','digital-marketing-bundle.html'); return false;" class="btn-primary" id="pricing-cta-btn" style="text-decoration:none;display:inline-flex;align-items:center;justify-content:center;gap:8px;width:100%;">
            🛒 ADD TO CART @ ₹499 →
          </a>"""
    new_dm_pricing = """          <div class="buy-actions-wrapper" style="display:flex; gap:12px; width:100%; margin-top:8px;">
            <a href="#" class="btn-primary btn-buy-now-detail" style="flex:1.8; justify-content: center; gap: 8px; font-size: 15px; padding: 16px; background: linear-gradient(135deg, #ff8a00, #ffb347); border: none; color: #000; font-weight: 800; text-decoration:none; box-shadow:0 4px 12px rgba(255,138,0,0.2);" onclick="buyNow('digital-marketing-bundle', 'Full Digital Marketing Resource Bundle (700+)', 499, 'laptop-workspace.webp', 'digital-marketing-bundle.html'); return false;">
              ⚡ Buy Now @ ₹499
            </a>
            <a href="#" class="btn-primary btn-add-cart-detail" style="flex:1; justify-content: center; gap: 8px; font-size: 15px; padding: 16px; background: rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); color:#fff; text-decoration:none;" onclick="addToCart('digital-marketing-bundle', 'Full Digital Marketing Resource Bundle (700+)', 499, 'laptop-workspace.webp', 'digital-marketing-bundle.html'); return false;">
              🛒 Add to Cart
            </a>
          </div>"""
    content = content.replace(old_dm_pricing, new_dm_pricing)

    # General fallback for any other checkout section
    content = content.replace("🎬 ADD TO CART NOW @ ₹99 →", "⚡ BUY NOW @ ₹99 →")
    content = content.replace("🎬 ADD TO CART NOW @ ₹199 →", "⚡ BUY NOW @ ₹199 →")
    content = content.replace("🎬 ADD TO CART NOW @ ₹349 →", "⚡ BUY NOW @ ₹349 →")
    content = content.replace("🎬 ADD TO CART NOW @ ₹499 →", "⚡ BUY NOW @ ₹499 →")
    content = content.replace("ADD TO CART NOW", "BUY NOW")
    
    # Let's add styling rule for .buy-actions-wrapper if not present in styles
    if "buy-actions-wrapper" not in content:
        content = content.replace("</head>", """  <style>
    .buy-actions-wrapper {
      display: flex; gap: 12px; margin-top: 8px; width: 100%;
    }
    @media (max-width: 480px) {
      .buy-actions-wrapper {
        flex-direction: column !important;
      }
    }
  </style>
</head>""")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  -> Patch applied successfully.")

def main():
    root_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    files = [
        "video-editing.html",
        "mega-reels.html",
        "n8n-pack.html",
        "n8n-workflow-automation.html",
        "digital-marketing-bundle.html",
        "web-apps.html"
    ]
    for f in files:
        filepath = os.path.join(root_dir, f)
        if os.path.exists(filepath):
            patch_page(filepath, f)
        else:
            print(f"Warning: File {filepath} not found.")

if __name__ == "__main__":
    main()
