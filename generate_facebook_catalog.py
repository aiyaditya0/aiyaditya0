import os
import openpyxl
import csv
import re

def make_product_id(name):
    clean = re.sub(r'^\d+\.\s*', '', name)
    clean = clean.lower()
    clean = re.sub(r'[^a-z0-9\s-]', '', clean)
    clean = re.sub(r'[\s-]+', '-', clean).strip('-')
    return clean

def get_product_image(name, category_id):
    name_lower = name.lower()
    
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

def main():
    root_dir = r"c:\Users\aditya tiwari\Downloads\FUTUREWITHAI WEB"
    excel_path = os.path.join(root_dir, "PRODUCT.xlsx")
    
    if not os.path.exists(excel_path):
        print(f"Error: {excel_path} not found!")
        return
        
    wb = openpyxl.load_workbook(excel_path, data_only=True)
    sheet = wb.active
    
    facebook_catalog_path = os.path.join(root_dir, "facebook_catalog.csv")
    
    domain = "https://futurewithai.anshumanenterprises.online"
    
    # Custom pages mapping
    custom_pages = {
        "video-editing": "video-editing.html",
        "n8n-pack": "n8n-pack.html",
        "n8n-workflow-automation": "n8n-workflow-automation.html",
        "mega-reels": "mega-reels.html",
        "web-apps": "web-apps.html",
        "digital-marketing-bundle": "digital-marketing-bundle.html"
    }

    with open(facebook_catalog_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Standard Meta catalog headers
        writer.writerow(['id', 'title', 'description', 'availability', 'condition', 'price', 'link', 'image_link', 'brand'])
        
        count = 0
        for row_idx, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
            category = row[0]
            name = row[1]
            price = row[2]
            unit = row[3]
            link_col = row[4]
            
            if not name or not category:
                continue
                
            category = str(category).strip()
            name = str(name).strip()
            
            cat_lower = category.lower()
            name_lower = name.lower()
            
            # Determine clean category ID
            if "software" in cat_lower or "web" in cat_lower:
                cat_id = "webapps"
            elif "editing bundle" in cat_lower:
                cat_id = "editing"
            elif "marketing" in cat_lower or "maketing" in cat_lower or "business" in cat_lower:
                cat_id = "marketing"
            elif "video editing" in cat_lower:
                if any(x in name_lower for x in ["youtuber", "graphics", "motion", "transitions", "editing"]):
                    cat_id = "editing"
                else:
                    cat_id = "reels"
            else:
                cat_id = "reels"
                
            p_id = make_product_id(name)
            
            # Skip items that are free (often delivered as bonuses)
            price_str = str(price).strip().upper() if price is not None else ""
            if "FREE" in price_str or price == 0 or not price:
                continue
                
            # Determine price string e.g. "199.00 INR"
            try:
                price_val = float(price)
            except ValueError:
                price_val = 199.0  # default fallback
            price_formatted = f"{price_val:.2f} INR"
            
            # Link mapping
            # Check if this product corresponds to one of our main custom landing pages
            page_name = f"product-{p_id}.html"
            for key, val in custom_pages.items():
                if key in p_id or p_id in key:
                    page_name = val
                    break
                    
            product_url = f"{domain}/{page_name}"
            
            # Image Link
            img_file = get_product_image(name, cat_id)
            if img_file.startswith("video-editing-assets/"):
                img_url = f"{domain}/{img_file}"
            else:
                img_url = f"{domain}/{img_file}"
                
            desc = get_custom_description(name)
            # Append Bumper Offer to the description
            desc += "\n\n🎁 BUMPER LAUNCH OFFER: Buy this pack today and get 9 Premium Bonus Rewards Bundles (Worth ₹19,491) completely FREE:\n1. 5000+ MEGA REELS BUNDLE (Worth ₹4,999)\n2. Caravan Life Travel Reels (Worth ₹1,999)\n3. Dog Reels Bundle (Worth ₹1,999)\n4. Funny & Cute Cat Bundle (Worth ₹1,999)\n5. Health Infographic Post Canva (Worth ₹1,499)\n6. Lifestyle Reels Bundle (Worth ₹1,999)\n7. Luxury Hotels & Resorts (Worth ₹1,999)\n8. Travel Reels Bundle (Worth ₹1,999)\n9. Black Word Quotes (Worth ₹999)"
            
            writer.writerow([
                p_id,
                name,
                desc,
                'in stock',
                'new',
                price_formatted,
                product_url,
                img_url,
                'FutureWithAI'
            ])
            count += 1
            
    print(f"Generated Facebook Catalog with {count} products at: {facebook_catalog_path}")

if __name__ == "__main__":
    main()
