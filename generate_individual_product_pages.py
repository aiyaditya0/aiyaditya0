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
    
    # Exact mappings for the new PNG images provided by the user
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
        
    if category_id == "web-software":
        return "webapp_hero_mockup.webp"
    elif category_id == "digital-marketing":
        return "ecommerce_portal_mockup.webp"
    elif category_id == "business":
        return "laptop-workspace.webp"
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

def get_premium_content_for_category(category_id, price):
    # Setup Dynamic Content per category ID
    if category_id in ["video-editing", "editing-bundle"]:
        stats_ribbon_html = """
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="video" style="width:20px;height:20px;color:var(--primary-container);"></i> Raw HD</div>
          <div class="hero-stat-label">Watermark Free</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="zap" style="width:20px;height:20px;color:var(--primary-container);"></i> Instant</div>
          <div class="hero-stat-label">Cloud Download</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="infinity" style="width:20px;height:20px;color:var(--primary-container);"></i> Lifetime</div>
          <div class="hero-stat-label">Access Validity</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="badge-dollar-sign" style="width:20px;height:20px;color:var(--primary-container);"></i> 100%</div>
          <div class="hero-stat-label">Commercial License</div>
        </div>
        """
        benefits_grid_html = """
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="trending-up"></i></div>
          <h3 class="earnings-title">Instagram & TikTok Creators</h3>
          <div class="earnings-salary">₹25,000–₹1,50,000/month</div>
          <p class="earnings-desc">Deploy ready-to-post, watermark-free high retention videos on your pages. Tap into viral social media algorithms to build a massive follower base and secure brand sponsorships.</p>
          <ul class="earnings-bullets">
            <li>Zero filming required</li>
            <li>Post daily consistent shorts</li>
            <li>Attract global audience segments</li>
            <li>Grow niche theme pages rapidly</li>
          </ul>
          <div class="earnings-badge">Grow Passive Income</div>
        </div>
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="video"></i></div>
          <h3 class="earnings-title">Freelance Video Editors</h3>
          <div class="earnings-salary">₹15,000–₹60,000/project</div>
          <p class="earnings-desc">Supercharge client edits. Use premade cinematically corrected clips, LUTs, and animated assets to edit videos in minutes instead of scanning stock footage websites for hours.</p>
          <ul class="earnings-bullets">
            <li>Premium transitions & SFX</li>
            <li>Cut rendering time by 80%</li>
            <li>Increase active project volume</li>
            <li>Charge professional retainer rates</li>
          </ul>
          <div class="earnings-badge">Accelerate Workflows</div>
        </div>
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="briefcase"></i></div>
          <h3 class="earnings-title">Marketing Agencies</h3>
          <div class="earnings-salary">₹50,000–₹3,00,000/month</div>
          <p class="earnings-desc">Secure high-paying local business advertising retainers. Pitch visual advertising campaigns using high-retention video reels and promotional graphic infographics.</p>
          <ul class="earnings-bullets">
            <li>Viral advertisement frameworks</li>
            <li>DFY niche marketing proposals</li>
            <li>High visual content conversion</li>
            <li>Deliver campaigns in hours</li>
          </ul>
          <div class="earnings-badge">Scale Retainer Income</div>
        </div>
        """
        calculator_html = """
        <div class="calculator-container" id="calculator">
          <h2 class="calculator-title"><i data-lucide="calculator" style="color:var(--primary);"></i> Revenue Potential Calculator</h2>
          <p style="color:var(--text-secondary); margin-bottom: 24px;">Slide views & sponsorship metrics to project monthly brand contract earnings</p>
          
          <div class="calc-slider-group">
            <div class="calc-label-row">
              <span>Estimated Monthly Video Views:</span>
              <span class="calc-val-bubble" id="views-val">1,000,000</span>
            </div>
            <input type="range" min="100000" max="10000000" step="100000" value="1000000" class="calc-slider" id="views-slider">
          </div>

          <div class="calc-slider-group">
            <div class="calc-label-row">
              <span>Sponsorship Rate (per 100k views):</span>
              <span class="calc-val-bubble" id="rate-val">₹8,000</span>
            </div>
            <input type="range" min="1000" max="50000" step="500" value="8000" class="calc-slider" id="rate-slider">
          </div>

          <div class="calc-result-box">
            <div class="calc-result-label">Projected Monthly Sponsorship Income:</div>
            <div class="calc-result-value" id="calc-result">₹80,000</div>
            <div class="calc-result-subtitle">Based on regular viral view sponsorship rates</div>
          </div>
        </div>
        """
        calculator_js = """
        const viewsSlider = document.getElementById('views-slider');
        const rateSlider = document.getElementById('rate-slider');
        const viewsVal = document.getElementById('views-val');
        const rateVal = document.getElementById('rate-val');
        const calcResult = document.getElementById('calc-result');

        function updateCalc() {
          const views = parseInt(viewsSlider.value);
          const rate = parseInt(rateSlider.value);
          viewsVal.textContent = views.toLocaleString('en-IN');
          rateVal.textContent = '₹' + rate.toLocaleString('en-IN');
          const income = Math.round((views / 100000) * rate);
          calcResult.textContent = '₹' + income.toLocaleString('en-IN');
        }

        viewsSlider.addEventListener('input', updateCalc);
        rateSlider.addEventListener('input', updateCalc);
        updateCalc();
        """
        db_inclusions_html = """
        <div class="db-category">
          <div class="db-category-title"><i data-lucide="folder-git" style="color:var(--primary);"></i> Files & Library structure</div>
          <div class="db-apps-grid">
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Watermark-free raw MP4/MOV high definition files</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Viral caption ideas & hooks cheat-sheet</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Cinematic sound effects (SFX) & sound loops pack</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Trending video text styles & fonts presets</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Lifetime cloud storage sync access</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Resell rights commercial license sheet</div>
          </div>
        </div>
        """
        faq_html = """
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">How will I download the video files?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">You will get an instant email containing direct links to our premium Google Drive folders. The download bandwidth is extremely fast, and you can download files individually or as a single ZIP.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Are there watermarks or logos on files?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">No! Every file is raw, un-branded, and watermark-free. You can customize them by applying overlays, typography, and logos, or directly upload them to your social pages.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Can I use CapCut or Premiere Pro?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">Yes! All assets are generic MP4/MOV and WAV/MP3 formats, making them fully compatible with all editing software including CapCut, Premiere Pro, After Effects, DaVinci Resolve, and Final Cut.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Is a commercial license included?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">Yes, a full lifetime commercial resell license is included. You can use these elements in client projects, freelance work, and social media platforms without copyright strikes.</div>
          </div>
        </div>
        """
    elif category_id == "web-software":
        stats_ribbon_html = """
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="code" style="width:20px;height:20px;color:var(--primary-container);"></i> Clean</div>
          <div class="hero-stat-label">Source Code files</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="database" style="width:20px;height:20px;color:var(--primary-container);"></i> SQL DB</div>
          <div class="hero-stat-label">Database Dumps</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="shield-check" style="width:20px;height:20px;color:var(--primary-container);"></i> Tested</div>
          <div class="hero-stat-label">Working Boilerplates</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="key" style="width:20px;height:20px;color:var(--primary-container);"></i> Lifetime</div>
          <div class="hero-stat-label">Developer License</div>
        </div>
        """
        benefits_grid_html = """
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="laptop"></i></div>
          <h3 class="earnings-title">Freelance Agency</h3>
          <div class="earnings-salary">₹20,000–₹1,00,000/Project</div>
          <p class="earnings-desc">Deliver advanced SaaS systems, hospital networks, or school administration directories to clients in days instead of coding from scratch for months.</p>
          <ul class="earnings-bullets">
            <li>Cut project turnaround time</li>
            <li>Pre-built database structures</li>
            <li>Tested backend auth scripts</li>
            <li>Retain higher pricing margins</li>
          </ul>
          <div class="earnings-badge">Acquire High-Value Clients</div>
        </div>
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="server"></i></div>
          <h3 class="earnings-title">Micro-SaaS Builders</h3>
          <div class="earnings-salary">₹50,000–₹5,00,000/month</div>
          <p class="earnings-desc">White-label tested code bases, set up Stripe/Razorpay pricing webhooks, host them on VPS networks, and charge premium monthly user subscriptions.</p>
          <ul class="earnings-bullets">
            <li>Tested user management dashboards</li>
            <li>Ready SaaS portal layouts</li>
            <li>Recurring subscription business</li>
            <li>Zero licensing legal fees</li>
          </ul>
          <div class="earnings-badge">Generate Passive Revenue</div>
        </div>
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="globe"></i></div>
          <h3 class="earnings-title">SaaS Reseller & Flipping</h3>
          <div class="earnings-salary">₹1,00,000–₹8,00,000/Flip</div>
          <p class="earnings-desc">Rebrand these applications under premium domain addresses, add basic content features, deploy them, and sell them as running portals on flipping networks.</p>
          <ul class="earnings-bullets">
            <li>Rebrand portals instantly</li>
            <li>Scale SaaS domain portfolios</li>
            <li>Flip micro-services easily</li>
            <li>Full code transfer permissions</li>
          </ul>
          <div class="earnings-badge">Flip Digital Assets</div>
        </div>
        """
        calculator_html = """
        <div class="calculator-container" id="calculator">
          <h2 class="calculator-title"><i data-lucide="calculator" style="color:var(--primary);"></i> Agency Earning Calculator</h2>
          <p style="color:var(--text-secondary); margin-bottom: 24px;">Adjust user client volumes and billing retainers to estimate project income margins</p>
          
          <div class="calc-slider-group">
            <div class="calc-label-row">
              <span>Active Clients / SaaS Installs:</span>
              <span class="calc-val-bubble" id="clients-val">5</span>
            </div>
            <input type="range" min="1" max="50" step="1" value="5" class="calc-slider" id="clients-slider">
          </div>

          <div class="calc-slider-group">
            <div class="calc-label-row">
              <span>Retainer Fee (per Client Project):</span>
              <span class="calc-val-bubble" id="retainer-val">₹25,000</span>
            </div>
            <input type="range" min="5000" max="100000" step="1000" value="25000" class="calc-slider" id="retainer-slider">
          </div>

          <div class="calc-result-box">
            <div class="calc-result-label">Projected Project Earning Potential:</div>
            <div class="calc-result-value" id="calc-result">₹1,25,000</div>
            <div class="calc-result-subtitle">Estimate based on generic freelance agency billing rates</div>
          </div>
        </div>
        """
        calculator_js = """
        const clientsSlider = document.getElementById('clients-slider');
        const retainerSlider = document.getElementById('retainer-slider');
        const clientsVal = document.getElementById('clients-val');
        const retainerVal = document.getElementById('retainer-val');
        const calcResult = document.getElementById('calc-result');

        function updateCalc() {
          const clients = parseInt(clientsSlider.value);
          const retainer = parseInt(retainerSlider.value);
          clientsVal.textContent = clients;
          retainerVal.textContent = '₹' + retainer.toLocaleString('en-IN');
          const revenue = clients * retainer;
          calcResult.textContent = '₹' + revenue.toLocaleString('en-IN');
        }

        clientsSlider.addEventListener('input', updateCalc);
        retainerSlider.addEventListener('input', updateCalc);
        updateCalc();
        """
        db_inclusions_html = """
        <div class="db-category">
          <div class="db-category-title"><i data-lucide="terminal" style="color:var(--primary);"></i> Inclusions & Developer Files</div>
          <div class="db-apps-grid">
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Complete deployable application source code folder</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Configured database SQL schema structure files</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Step-by-step server installation readme documentation</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Configured router, middleware & admin login setups</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Unlimited hosting installations developer license</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Preconfigured stylesheet templates & views folder</div>
          </div>
        </div>
        """
        faq_html = """
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">What programming languages are used?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">Most templates are built using PHP, Laravel, HTML5, Javascript, and MySQL. Some newer SaaS boilerplates use Node.js and React structures. Detailed descriptions are in the root directory.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Is the database schema included?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">Yes! Every codebase includes a clean database SQL dump file to easily import using phpMyAdmin, MySQL Workbench, or VPS terminal interfaces to make setup lightning fast.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Can I customize the code and resell it?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">Absolutely. You receive a commercial developer license. You can white-label the software, rebrand fonts/styles, install it for your local clients, host it as SaaS, or resell it under your name.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Are setup installation guides provided?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">Yes. Detailed readme text files, server configure guidelines, and database connection settings templates are included in each folder for easy reference.</div>
          </div>
        </div>
        """
    elif category_id == "digital-marketing":
        stats_ribbon_html = """
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="palette" style="width:20px;height:20px;color:var(--primary-container);"></i> Canva</div>
          <div class="hero-stat-label">Editable Templates</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="bot" style="width:20px;height:20px;color:var(--primary-container);"></i> ChatGPT</div>
          <div class="hero-stat-label">AI Prompt Books</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="file-check" style="width:20px;height:20px;color:var(--primary-container);"></i> Proposal</div>
          <div class="hero-stat-label">Decks & Contracts</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="refresh-cw" style="width:20px;height:20px;color:var(--primary-container);"></i> Lifetime</div>
          <div class="hero-stat-label">Resource Sync Updates</div>
        </div>
        """
        benefits_grid_html = """
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="layout"></i></div>
          <h3 class="earnings-title">Social Media Marketers</h3>
          <div class="earnings-salary">₹15,000–₹50,000/month</div>
          <p class="earnings-desc">Save hours designing visual posts. Import ready-to-edit Canva templates, add your clients branding, and schedule viral infographic slide decks instantly.</p>
          <ul class="earnings-bullets">
            <li>Fully editable design canvases</li>
            <li>Trending niche infographics</li>
            <li>Supports free Canva accounts</li>
            <li>Manage multiple client accounts</li>
          </ul>
          <div class="earnings-badge">Streamline Graphic Edits</div>
        </div>
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="message-square"></i></div>
          <h3 class="earnings-title">Freelancers & Copywriters</h3>
          <div class="earnings-salary">₹20,000–₹80,000/client</div>
          <p class="earnings-desc">Write high-converting ads, email campaigns, landing page headlines, and SEO articles in seconds. Copy-paste our certified target niche ChatGPT prompt sheets.</p>
          <ul class="earnings-bullets">
            <li>Targeted marketing prompt sequences</li>
            <li>High-converting email copy blocks</li>
            <li>Viral advertisement frameworks</li>
            <li>Scale copywriting speed 10x</li>
          </ul>
          <div class="earnings-badge">Generate Content in Seconds</div>
        </div>
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="check-square"></i></div>
          <h3 class="earnings-title">Marketing Agencies</h3>
          <div class="earnings-salary">₹50,000–₹2,50,000/month</div>
          <p class="earnings-desc">Secure client payments and pitches. Use ready-made contract agreement decks, marketing proposals, service checklists, and cold outreach scripts.</p>
          <ul class="earnings-bullets">
            <li>Agency contract templates</li>
            <li>NDA & client outreach formats</li>
            <li>Proposal decks that seal retainers</li>
            <li>High visual pitch conversions</li>
          </ul>
          <div class="earnings-badge">Scale Retainer Income</div>
        </div>
        """
        calculator_html = """
        <div class="calculator-container" id="calculator">
          <h2 class="calculator-title"><i data-lucide="calculator" style="color:var(--primary);"></i> Marketer Revenue Calculator</h2>
          <p style="color:var(--text-secondary); margin-bottom: 24px;">Adjust client volume and service retainers to estimate your monthly agency revenue</p>
          
          <div class="calc-slider-group">
            <div class="calc-label-row">
              <span>Retained Monthly Clients:</span>
              <span class="calc-val-bubble" id="clients-val">4</span>
            </div>
            <input type="range" min="1" max="20" step="1" value="4" class="calc-slider" id="clients-slider">
          </div>

          <div class="calc-slider-group">
            <div class="calc-label-row">
              <span>Monthly Client Service Fee:</span>
              <span class="calc-val-bubble" id="retainer-val">₹15,000</span>
            </div>
            <input type="range" min="2000" max="50000" step="500" value="15000" class="calc-slider" id="retainer-slider">
          </div>

          <div class="calc-result-box">
            <div class="calc-result-label">Projected Monthly Agency Revenue:</div>
            <div class="calc-result-value" id="calc-result">₹60,000</div>
            <div class="calc-result-subtitle">Projected gross earnings from active service contracts</div>
          </div>
        </div>
        """
        calculator_js = """
        const clientsSlider = document.getElementById('clients-slider');
        const retainerSlider = document.getElementById('retainer-slider');
        const clientsVal = document.getElementById('clients-val');
        const retainerVal = document.getElementById('retainer-val');
        const calcResult = document.getElementById('calc-result');

        function updateCalc() {
          const clients = parseInt(clientsSlider.value);
          const retainer = parseInt(retainerSlider.value);
          clientsVal.textContent = clients;
          retainerVal.textContent = '₹' + retainer.toLocaleString('en-IN');
          const revenue = clients * retainer;
          calcResult.textContent = '₹' + revenue.toLocaleString('en-IN');
        }

        clientsSlider.addEventListener('input', updateCalc);
        retainerSlider.addEventListener('input', updateCalc);
        updateCalc();
        """
        db_inclusions_html = """
        <div class="db-category">
          <div class="db-category-title"><i data-lucide="book-open" style="color:var(--primary);"></i> Marketing Toolkit Contents</div>
          <div class="db-apps-grid">
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Direct editable Canva template URLs</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Sorted high-intent AI ChatGPT copy-paste prompts</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Professional marketing proposal PDF decks</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Cold email outreach scripts and templates</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Standard freelance contract and NDA agreements</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Lifetime cloud storage links validity</div>
          </div>
        </div>
        """
        faq_html = """
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Do I need Canva Pro to edit graphics?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">No! All graphics templates are fully compatible with Canva free accounts. You can customize colors, insert logos, and swap layout images on any device.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">How do I access prompt libraries?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">The prompt databases are sorted as plain text and spreadsheet layouts in the cloud folder. You can open them, copy the prompts, fill in your business parameters, and paste them into ChatGPT.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Can I use proposal sheets for clients?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">Yes, the proposals, contracts, and NDA formats are designed as editable templates. You can add your company branding details and send them directly to clients to lock in deals.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Are updates free for buyers?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">Yes! Any fresh Canva graphic blocks, ChatGPT prompt sheets, or contract checklists added to the cloud directories are automatically synced to your dashboard links for free.</div>
          </div>
        </div>
        """
    else: # business / courses
        stats_ribbon_html = """
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="cloud-lightning" style="width:20px;height:20px;color:var(--primary-container);"></i> 1.37 TB</div>
          <div class="hero-stat-label">Cloud Storage Database</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="graduation-cap" style="width:20px;height:20px;color:var(--primary-container);"></i> Premium</div>
          <div class="hero-stat-label">Learning Modules</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="play-circle" style="width:20px;height:20px;color:var(--primary-container);"></i> Online</div>
          <div class="hero-stat-label">Direct video streaming</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-number"><i data-lucide="file-text" style="width:20px;height:20px;color:var(--primary-container);"></i> Workbooks</div>
          <div class="hero-stat-label">And Strategy Checksheets</div>
        </div>
        """
        benefits_grid_html = """
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="shopping-bag"></i></div>
          <h3 class="earnings-title">E-Commerce & Shopify Sellers</h3>
          <div class="earnings-salary">₹30,000–₹2,00,000/month</div>
          <p class="earnings-desc">Master dropshipping, niche product research, Facebook ads campaigns, and shipping integrations using step-by-step masterclass blueprints.</p>
          <ul class="earnings-bullets">
            <li>Niche product validation methods</li>
            <li>Ad campaign configure setups</li>
            <li>Supplier sourcing worksheets</li>
            <li>High-margin selling formulas</li>
          </ul>
          <div class="earnings-badge">Build Online Stores</div>
        </div>
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="pen-tool"></i></div>
          <h3 class="earnings-title">Freelance Copywriters</h3>
          <div class="earnings-salary">₹20,000–₹1,00,000/client</div>
          <p class="earnings-desc">Write landing pages, sales copies, and high-retention newsletter blocks. Master client prospecting, cold mailing, and contract packaging secrets.</p>
          <ul class="earnings-bullets">
            <li>Sales script copywriting blueprints</li>
            <li>Email sequencing cheat-sheets</li>
            <li>Cold pitch closing frameworks</li>
            <li>Negotiate premium billing fees</li>
          </ul>
          <div class="earnings-badge">Close Marketing Deals</div>
        </div>
        <div class="earnings-card">
          <div class="earnings-icon"><i data-lucide="search"></i></div>
          <h3 class="earnings-title">SEO & Growth Marketers</h3>
          <div class="earnings-salary">₹25,000–₹1,20,000/month</div>
          <p class="earnings-desc">Scale organic traffic channels. Master search keyword research, search console configurations, off-page backlinks creation, and index ranking.</p>
          <ul class="earnings-bullets">
            <li>Keyword target sorting guides</li>
            <li>On-page layout configure cards</li>
            <li>High-quality backlinks blueprint</li>
            <li>Rank on top google indexes</li>
          </ul>
          <div class="earnings-badge">Scale Organic Search Traffic</div>
        </div>
        """
        calculator_html = """
        <div class="calculator-container" id="calculator">
          <h2 class="calculator-title"><i data-lucide="calculator" style="color:var(--primary);"></i> Digital Profit Calculator</h2>
          <p style="color:var(--text-secondary); margin-bottom: 24px;">Adjust daily volume sales and margins to calculate your net projected monthly returns</p>
          
          <div class="calc-slider-group">
            <div class="calc-label-row">
              <span>Daily Sales Volume:</span>
              <span class="calc-val-bubble" id="sales-val">3</span>
            </div>
            <input type="range" min="1" max="100" step="1" value="3" class="calc-slider" id="sales-slider">
          </div>

          <div class="calc-slider-group">
            <div class="calc-label-row">
              <span>Net Profit (per Sale):</span>
              <span class="calc-val-bubble" id="margin-val">₹1,500</span>
            </div>
            <input type="range" min="200" max="5000" step="50" value="1500" class="calc-slider" id="margin-slider">
          </div>

          <div class="calc-result-box">
            <div class="calc-result-label">Net Projected Monthly Profits:</div>
            <div class="calc-result-value" id="calc-result">₹1,35,000</div>
            <div class="calc-result-subtitle">Projected net earnings based on active monthly cycles</div>
          </div>
        </div>
        """
        calculator_js = """
        const salesSlider = document.getElementById('sales-slider');
        const marginSlider = document.getElementById('margin-slider');
        const salesVal = document.getElementById('sales-val');
        const marginVal = document.getElementById('margin-margin'); // Wait, let's fix ID matching
        const marginValActual = document.getElementById('margin-val');
        const calcResult = document.getElementById('calc-result');

        function updateCalc() {
          const sales = parseInt(salesSlider.value);
          const margin = parseInt(marginSlider.value);
          salesVal.textContent = sales;
          if(marginValActual) marginValActual.textContent = '₹' + margin.toLocaleString('en-IN');
          const revenue = sales * margin * 30;
          calcResult.textContent = '₹' + revenue.toLocaleString('en-IN');
        }

        salesSlider.addEventListener('input', updateCalc);
        marginSlider.addEventListener('input', updateCalc);
        updateCalc();
        """
        db_inclusions_html = """
        <div class="db-category">
          <div class="db-category-title"><i data-lucide="database" style="color:var(--primary);"></i> Cloud Vault Database structure</div>
          <div class="db-apps-grid">
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Instant access to 1.37 TB high speed cloud folders</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Direct video lessons online streaming player</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Sorted chapters, text guide guides & templates</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Ad copy templates, worksheets & spreadsheets</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Lifetime free updates for future uploads</div>
            <div class="db-app-item"><i data-lucide="check" style="color:#27c93f;width:14px;height:14px;"></i>Offline downloads support for all lessons</div>
          </div>
        </div>
        """
        faq_html = """
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">How do I access 1.37 TB of directories?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">All files are hosted on secure, high-speed cloud nodes (MEGA and Google Drive). The links never expire, and you can download chapters locally or stream videos directly.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Are there templates or worksheets inside?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">Yes! Along with video guides, you get comprehensive excel sheets, ad copy templates, email sequences, and checklists to practice concepts.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Is there a time limit to download?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">No, your access link is valid forever. You can access the database folder from your desktop, mobile, or tablet anytime at zero extra charges.</div>
          </div>
        </div>
        <div class="faq-item">
          <div class="faq-header">
            <span class="faq-question">Do I get new courses added to the vault?</span>
            <i data-lucide="plus" class="faq-icon"></i>
          </div>
          <div class="faq-body">
            <div class="faq-content">Yes! All future marketing courses, dropshipping masterclass chapters, and resources uploaded to the cloud repository are completely free for all previous buyers.</div>
          </div>
        </div>
        """
    return stats_ribbon_html, benefits_grid_html, calculator_html, calculator_js, db_inclusions_html, faq_html

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
            if "bundle" in cat_lower:
                cat_id = "editing-bundle"
                cat_display = "🎬 Editing Bundle"
            else:
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
    
    # Generate pages
    for idx, p in enumerate(products):
        filename = f"product-{p['id']}.html"
        
        # Delete individual page if product is free (given as a bonus)
        if p["is_free"]:
            if os.path.exists(filename):
                try:
                    os.remove(filename)
                    print(f"Deleted free product page: {filename}")
                except Exception as e:
                    print(f"Error deleting {filename}: {e}")
            continue
        
        # Category specific layouts
        stats_ribbon_html, benefits_grid_html, calculator_html, calculator_js, db_inclusions_html, faq_html = get_premium_content_for_category(p["category_id"], p["price"])
        
        # Testimonial reviews
        reviews_html = """
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Outstanding resource pack. I was skeptical first due to the low price, but the cloud link has everything as described. Clean layouts, zero issues."</p>
          <div class="review-author">
            <div class="review-avatar">AK</div>
            <div class="review-author-info">
              <span class="review-name">Amit Kumar</span>
              <span class="review-role">Patna · Verified Customer</span>
            </div>
          </div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★ <span style="font-size: 11px; color: #27c93f; margin-left: auto;">✔ Verified Buyer</span></div>
          <p class="review-text">"Absolute lifesaver for my freelance projects. Saved me days of scanning code files and stock footage. Delivered instantly via confirmation email."</p>
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
          <p class="review-text">"Really solid quality. I checked the dog and caravan reels folders, and they are high definition. Then I bought this paid pack. Incredible value."</p>
          <div class="review-author">
            <div class="review-avatar">RV</div>
            <div class="review-author-info">
              <span class="review-name">Rohan Verma</span>
              <span class="review-role">Noida · Creator</span>
            </div>
          </div>
        </div>
        """
        
        # Generate Related Suggestions (3 candidates from same category first, excluding free products)
        candidates = [item for item in products if item["id"] != p["id"] and not item["is_free"]]
        cat_candidates = [item for item in candidates if item["category_id"] == p["category_id"]]
        if len(cat_candidates) >= 3:
            suggested = random.sample(cat_candidates, 3)
        else:
            suggested = cat_candidates + random.sample([item for item in candidates if item not in cat_candidates], 3 - len(cat_candidates))
            
        suggestions_html = ""
        for s in suggested:
            if s["is_free"]:
                s_badge_html = '<span class="suggest-price-free">FREE</span>'
                quick_buy_btn_html = f"""
                <a href="{s["link"]}" target="_blank" class="quick-buy-btn free-btn">
                  <i data-lucide="download" style="width:14px;height:14px;"></i> Download Free
                </a>
                """
            else:
                s_badge_html = f'<span class="suggest-price">₹{s["price"]}</span>'
                s_name_escaped = s["name"].replace("'", "\\'")
                quick_buy_btn_html = f"""
                <button class="quick-buy-btn" onclick="quickBuy(\'{s["id"]}\',\'{s_name_escaped}\',{s["price"]},\'{s["img"]}\',\'product-{s["id"]}.html\')">
                  <i data-lucide="zap" style="width:14px;height:14px;"></i> Buy Now ₹{s["price"]}
                </button>
                """
            suggestions_html += f"""
        <div class="suggest-card">
          <div class="prod-img-wrap">
            <img class="suggest-img" src="{s["img"]}" alt="{s["name"]}" loading="lazy">
            <div class="prod-quick-buy">
              {quick_buy_btn_html}
              <a href="product-{s["id"]}.html" class="quick-view-btn">
                <i data-lucide="eye" style="width:16px;height:16px;"></i>
              </a>
            </div>
          </div>
          <div class="suggest-body">
            <h3 class="suggest-title"><a href="product-{s["id"]}.html" style="color:inherit; text-decoration:none; transition:color 0.2s;" onmouseover="this.style.color=\'#ff8a00\'" onmouseout="this.style.color=\'inherit\'">{s["name"]}</a></h3>
            <p class="suggest-desc">{s["desc"]}</p>
            <div class="suggest-footer">
              {s_badge_html}
              <a href="product-{s["id"]}.html" class="suggest-action">Details →</a>
            </div>
          </div>
        </div>"""

        # Dynamic buy layout
        p_name_escaped = p["name"].replace("'", "\\'")
        if p["is_free"]:
            badge_class = "badge-free"
            badge_text = "🎁 Free Resource"
            price_row_html = '<span class="price-free">FREE</span>'
            buy_button_html = f'<a href="{p["link"]}" target="_blank" class="btn-buy btn-buy-free"><i data-lucide="download" style="width:20px;height:20px;"></i> Download Free Resource</a>'
            val_pay_today_badge = '<div class="pay-today-badge">100% Free Access</div>'
            val_pay_today_price = '<div class="pay-today-price">FREE</div>'
            value_block_actions = f'<a href="{p["link"]}" target="_blank" class="btn-primary" style="width:100%; justify-content:center; text-decoration:none;"><i data-lucide="download"></i> Download Free</a>'
            discount = 100
        else:
            badge_class = "badge-sale"
            badge_text = "🔥 Premium Resource"
            orig_price = 499 if p["price"] > 50 else 299
            discount = int(round((1.0 - float(p["price"]) / float(orig_price)) * 100))
            price_row_html = f'<span class="price-now">₹{p["price"]}</span><span class="price-orig">₹{orig_price}</span><span style="color:#27c93f; font-size:13px; font-weight:700;">({discount}% OFF Launch Deal)</span>'
            buy_button_html = f'<button class="btn-buy btn-buy-paid" onclick="addToCartAnimated(this,\'{p["id"]}\',\'{p_name_escaped}\',{p["price"]},\'{p["img"]}\',\'product-{p["id"]}.html\')"><i data-lucide="shopping-cart" style="width:20px;height:20px;"></i> Add To Cart</button>'
            val_pay_today_badge = f'<div class="pay-today-badge">{discount}% Discount Applied</div>'
            val_pay_today_price = f'<div class="pay-today-price">₹{p["price"]}</div>'
            value_block_actions = f'<button class="btn-primary" style="width: 100%; justify-content: center; gap: 8px;" onclick="addToCartAnimated(this,\'{p["id"]}\',\'{p_name_escaped}\',{p["price"]},\'{p["img"]}\',\'product-{p["id"]}.html\')"><i data-lucide="shopping-cart"></i> Add To Cart</button>'

        # Build Page HTML
        page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FutureWithAi - {p["name"]}</title>
  
  <meta name="description" content="{p["desc"]}">
  <meta property="og:title" content="FutureWithAi - {p["name"]}">
  <meta property="og:description" content="{p["desc"]}">
  <meta property="og:image" content="{p["img"]}">
  
  <link rel="icon" type="image/png" href="favicon.webp">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
  
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
      --transition-smooth: all 0.3s ease;
    }}

    body {{
      background: var(--bg-dark);
      color: #fff;
      font-family: 'Inter', sans-serif;
      margin: 0;
      padding: 0;
      overflow-x: hidden;
    }}

    #limited-offer-banner {{
      position: sticky; top: 0; z-index: 9999;
      background: linear-gradient(90deg, #b34500 0%, #ff8a00 40%, #ffb347 60%, #ff8a00 80%, #b34500 100%);
      background-size: 200% 100%;
      animation: bannerSlide 4s linear infinite;
      color: #000; text-align: center; padding: 10px 16px;
      font-size: 13.5px; font-weight: 700;
      display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap;
      box-shadow: 0 2px 20px rgba(255,138,0,0.5);
    }}
    @keyframes bannerSlide {{ 0%{{background-position:0% 50%}} 50%{{background-position:100% 50%}} 100%{{background-position:0% 50%}} }}
    
    #offer-countdown {{
      display: inline-flex; align-items: center; gap: 4px;
      background: rgba(0,0,0,0.18); border-radius: 8px;
      padding: 3px 12px; font-size: 14px; font-weight: 800; color: #fff;
    }}
    .offer-cta-link {{
      background: #000; color: #ff8a00; padding: 4px 14px;
      border-radius: 20px; font-size: 12.5px; font-weight: 800;
      text-decoration: none; transition: background 0.2s; white-space: nowrap;
    }}
    .offer-cta-link:hover {{ background: #1a1a1a; }}
    #offer-close-btn {{
      position: absolute; right: 14px; top: 50%; transform: translateY(-50%);
      background: none; border: none; color: rgba(0,0,0,0.5); cursor: pointer; font-size: 18px;
    }}
    #offer-close-btn:hover {{ color: #000; }}

    header {{
      position: sticky; top: 42px; z-index: 1000;
      background: rgba(5,5,5,0.92); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
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
      font-size: 13px; font-weight: 600; transition: all 0.2s;
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

    /* Product Hero */
    .product-hero {{
      background: linear-gradient(135deg, #0a0614 0%, #150a00 50%, #0a0614 100%);
      padding: 60px 0; border-bottom: 1px solid var(--border-color);
    }}
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; }}
    .hero-grid {{ display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 48px; align-items: center; }}
    
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
      font-family: 'Playfair Display', serif; font-size: clamp(30px, 4.5vw, 46px);
      line-height: 1.15; margin: 0 0 16px; color: #fff;
    }}
    .hero-desc {{ font-size: 16px; color: var(--text-secondary); line-height: 1.6; margin-bottom: 24px; }}
    
    .purchase-block {{
      background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-color);
      border-radius: 20px; padding: 24px; margin-bottom: 24px;
    }}
    .price-row {{ display: flex; align-items: baseline; gap: 12px; margin-bottom: 16px; flex-wrap: wrap; }}
    .price-now {{ font-size: 38px; font-weight: 800; color: #ff8a00; text-shadow: var(--glow-primary); }}
    .price-orig {{ font-size: 16px; color: var(--text-muted); text-decoration: line-through; }}
    .price-free {{ font-size: 38px; font-weight: 800; color: #27c93f; }}
    
    .btn-buy {{
      display: flex; align-items: center; justify-content: center; gap: 10px;
      width: 100%; padding: 16px; border-radius: 14px; border: none;
      font-size: 16px; font-weight: 800; cursor: pointer; transition: all 0.25s;
      font-family: 'Inter', sans-serif;
    }}
    .btn-buy-paid {{
      background: linear-gradient(135deg, #ff8a00, #ffb347); color: #000;
      box-shadow: 0 8px 24px rgba(255,138,0,0.3);
    }}
    .btn-buy-paid:hover {{ transform: translateY(-2px); box-shadow: 0 12px 32px rgba(255,138,0,0.45); }}
    .btn-buy-free {{
      background: linear-gradient(135deg, #27c93f, #1e9a30); color: #fff;
      box-shadow: 0 8px 24px rgba(39,201,63,0.3); text-decoration: none;
    }}
    .btn-buy-free:hover {{ transform: translateY(-2px); box-shadow: 0 12px 32px rgba(39,201,63,0.45); }}
    
    .trust-notes {{ display: flex; gap: 16px; flex-wrap: wrap; margin-top: 16px; }}
    .trust-note {{ font-size: 12px; color: var(--text-secondary); display: flex; align-items: center; gap: 6px; }}
    
    .hero-img-wrap {{
      border: 1.5px solid rgba(255,138,0,0.25); border-radius: 24px;
      overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.6), var(--glow-primary);
      background: #080503; aspect-ratio: 1 / 1;
      display: flex; align-items: center; justify-content: center;
    }}
    .hero-img-wrap img {{ width: 100%; height: 100%; object-fit: contain; padding: 12px; }}

    /* Trust Statistics Ribbon */
    .trustbar {{ padding: 24px 0; background: rgba(255,138,0,0.02); border-bottom: 1px solid var(--border-color); }}
    .trustbar-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }}
    .hero-stat-card {{
      background: rgba(27, 17, 10, 0.4); border: 1px solid var(--border-color);
      border-radius: 16px; padding: 20px; text-align: center; transition: var(--transition-smooth);
    }}
    .hero-stat-card:hover {{ border-color: var(--border-hover); box-shadow: var(--glow-primary); transform: translateY(-2px); }}
    .hero-stat-number {{
      font-size: 22px; font-weight: 800; color: #ff8a00; margin-bottom: 4px;
      display: flex; align-items: center; justify-content: center; gap: 8px;
    }}
    .hero-stat-label {{ font-size: 12px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-secondary); }}

    /* Revenue Potential / Benefits Grid */
    .earnings-sec {{ padding: 80px 0; border-bottom: 1px solid var(--border-color); }}
    .section-header {{ text-align: center; margin: 0 auto 56px auto; max-width: 700px; }}
    .section-label {{ color: #ff8a00; font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; display: block; margin-bottom: 8px; }}
    .section-title {{ font-family: 'Playfair Display', serif; font-size: clamp(26px, 4vw, 36px); color: #fff; margin: 0 0 12px; }}
    .section-desc {{ color: var(--text-secondary); font-size: 15px; line-height: 1.6; margin: 0; }}
    
    .earnings-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }}
    .earnings-card {{
      background: linear-gradient(135deg, rgba(20, 15, 10, 0.45) 0%, rgba(5, 5, 5, 0.8) 100%);
      border: 1px solid var(--border-color); border-radius: 24px; padding: 36px 28px;
      display: flex; flex-direction: column; gap: 20px; transition: var(--transition-smooth);
    }}
    .earnings-card:hover {{ border-color: var(--primary-container); box-shadow: var(--glow-primary); transform: translateY(-4px); }}
    .earnings-icon {{
      width: 48px; height: 48px; border-radius: 12px; background: rgba(255, 138, 0, 0.15);
      border: 1px solid rgba(255, 138, 0, 0.25); color: #ff8a00;
      display: flex; align-items: center; justify-content: center;
    }}
    .earnings-title {{ font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; color: #fff; margin: 0; }}
    .earnings-salary {{ font-size: 22px; font-weight: 800; color: #ff8a00; text-shadow: var(--glow-primary); }}
    .earnings-desc {{ font-size: 13.5px; color: var(--text-secondary); line-height: 1.55; margin: 0; }}
    .earnings-bullets {{ list-style: none; display: flex; flex-direction: column; gap: 10px; padding: 0; margin: 0; }}
    .earnings-bullets li {{ font-size: 13.5px; color: var(--text-muted); display: flex; gap: 10px; }}
    .earnings-bullets li::before {{ content: "•"; color: #ff8a00; font-weight: bold; }}
    .earnings-badge {{ align-self: flex-start; background: rgba(255, 138, 0, 0.15); color: #ff8a00; font-size: 11px; font-weight: 700; padding: 4px 12px; border-radius: 20px; margin-top: auto; }}

    /* Calculator Section */
    .calc-sec {{ padding: 80px 0; background: rgba(10, 10, 10, 0.3); border-bottom: 1px solid var(--border-color); }}
    .calculator-container {{
      background: linear-gradient(135deg, rgba(27, 17, 10, 0.95) 0%, rgba(5, 5, 5, 0.98) 100%);
      border: 1px solid rgba(255, 138, 0, 0.2); border-radius: 28px; padding: 40px;
      max-width: 760px; margin: 0 auto; box-shadow: 0 12px 40px rgba(0,0,0,0.6), var(--glow-primary);
    }}
    .calculator-title {{ font-family: 'Playfair Display', serif; font-size: 26px; color: #fff; margin: 0 0 12px; display: flex; align-items: center; justify-content: center; gap: 10px; }}
    .calc-slider-group {{ margin-bottom: 30px; text-align: left; }}
    .calc-label-row {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; font-size: 14.5px; color: #fff; }}
    .calc-val-bubble {{ background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border-color); border-radius: 8px; padding: 4px 12px; font-weight: 700; color: #ff8a00; }}
    .calc-slider {{ width: 100%; height: 6px; border-radius: 4px; outline: none; -webkit-appearance: none; accent-color: #ff8a00; background: rgba(255,255,255,0.08); }}
    .calc-result-box {{ background: rgba(0,0,0,0.3); border: 1px solid var(--border-color); border-radius: 16px; padding: 24px; margin-top: 32px; text-align: center; }}
    .calc-result-label {{ font-size: 13px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 6px; }}
    .calc-result-value {{ font-size: 48px; font-weight: 800; color: #ff8a00; text-shadow: var(--glow-primary); margin-bottom: 4px; }}
    .calc-result-subtitle {{ font-size: 12.5px; color: var(--text-muted); }}

    /* Database Inclusions */
    .db-sec {{ padding: 80px 0; border-bottom: 1px solid var(--border-color); }}
    .db-container {{ max-width: 900px; margin: 0 auto; }}
    .db-category {{ background: rgba(20, 15, 10, 0.4); border: 1px solid var(--border-color); border-radius: 20px; padding: 32px; }}
    .db-category-title {{ font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #ff8a00; margin-bottom: 24px; border-bottom: 1px solid rgba(255,138,0,0.15); padding-bottom: 10px; display: flex; align-items: center; gap: 10px; }}
    .db-apps-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; }}
    .db-app-item {{ font-size: 14px; color: var(--text-secondary); background: rgba(0,0,0,0.25); border: 1px solid rgba(255,255,255,0.02); padding: 12px 16px; border-radius: 8px; display: flex; align-items: center; gap: 10px; }}

    /* Value Box */
    .value-sec {{ padding: 80px 0; background: rgba(10,10,10,0.3); border-bottom: 1px solid var(--border-color); }}
    .value-box {{
      background: linear-gradient(135deg, rgba(30, 18, 10, 0.98) 0%, rgba(5, 5, 5, 0.99) 100%);
      border: 1.5px solid rgba(255, 138, 0, 0.3); border-radius: 24px; padding: 40px;
      max-width: 900px; margin: 0 auto; box-shadow: var(--glow-primary);
      display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 48px; align-items: center;
    }}
    .value-list {{ display: flex; flex-direction: column; gap: 12px; }}
    .value-item {{ display: flex; justify-content: space-between; font-size: 14.5px; color: var(--text-secondary); border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px; }}
    .value-item.total {{ font-size: 18px; font-weight: 700; color: #fff; border-bottom: none; margin-top: 8px; }}
    .value-pay-today {{ text-align: center; border-left: 1px solid rgba(255,255,255,0.08); padding-left: 48px; }}
    .pay-today-label {{ font-size: 12px; text-transform: uppercase; letter-spacing: 0.15em; color: var(--text-muted); margin-bottom: 4px; }}
    .pay-today-price {{ font-size: 58px; font-weight: 800; color: #ff8a00; text-shadow: var(--glow-primary); line-height: 1; margin-bottom: 8px; }}
    .pay-today-badge {{ display: inline-block; background: rgba(39, 201, 63, 0.15); color: #27c93f; border: 1px solid rgba(39, 201, 63, 0.3); padding: 3px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 24px; }}

    /* Testimonials */
    .reviews-sec {{ padding: 80px 0; border-bottom: 1px solid var(--border-color); }}
    .review-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
    .review-card {{ background: rgba(20, 12, 5, 0.6); border: 1px solid var(--border-color); border-radius: 20px; padding: 24px; display: flex; flex-direction: column; gap: 14px; transition: var(--transition-smooth); }}
    .review-card:hover {{ border-color: var(--border-hover); transform: translateY(-2px); }}
    .review-stars {{ color: #ffb300; font-size: 13px; display: flex; gap: 2px; }}
    .review-text {{ font-size: 13.5px; color: var(--text-secondary); line-height: 1.55; font-style: italic; }}
    .review-author {{ display: flex; align-items: center; gap: 12px; margin-top: auto; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 12px; }}
    .review-avatar {{ width: 38px; height: 38px; border-radius: 50%; background: rgba(255, 138, 0, 0.12); display: flex; align-items: center; justify-content: center; font-weight: 700; color: #ff8a00; border: 1px solid rgba(255,138,0,0.2); }}
    .review-name {{ font-size: 13.5px; font-weight: 600; color: #fff; display: block; }}
    .review-role {{ font-size: 11px; color: var(--text-muted); display: block; }}

    /* FAQ Section */
    .faq-sec {{ padding: 80px 0; border-bottom: 1px solid var(--border-color); }}
    .faq-container {{ max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; }}
    .faq-item {{ background: rgba(20, 20, 20, 0.4); border: 1px solid var(--border-color); border-radius: 16px; overflow: hidden; transition: var(--transition-smooth); }}
    .faq-item:hover {{ border-color: var(--border-hover); }}
    .faq-header {{ padding: 24px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; user-select: none; }}
    .faq-question {{ font-size: 15px; font-weight: 600; color: #fff; padding-right: 20px; }}
    .faq-icon {{ color: #ff8a00; transition: transform 0.3s ease; flex-shrink: 0; }}
    .faq-body {{ max-height: 0; overflow: hidden; transition: max-height 0.4s ease; }}
    .faq-content {{ padding: 0 24px 24px 24px; font-size: 13.5px; color: var(--text-secondary); line-height: 1.6; border-top: 1px solid rgba(255,255,255,0.02); padding-top: 16px; }}
    .faq-item.active .faq-body {{ max-height: 300px; }}
    .faq-item.active .faq-icon {{ transform: rotate(45deg); }}

    /* Suggestions Section */
    .suggestions-sec {{ padding: 80px 0; }}
    .suggestions-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }}
    .suggest-card {{
      background: rgba(20,12,5,0.8); border: 1px solid var(--border-color);
      border-radius: 18px; display: flex; flex-direction: column; overflow: hidden;
      transition: var(--transition-smooth);
    }}
    .suggest-card:hover {{ border-color: var(--border-hover); transform: translateY(-4px); box-shadow: 0 12px 30px rgba(0,0,0,0.5), var(--glow-primary); }}
    .suggest-img {{ width: 100%; aspect-ratio: 16 / 10; object-fit: cover; border-bottom: 1px solid rgba(255,255,255,0.05); }}
    .suggest-body {{ padding: 20px; display: flex; flex-direction: column; flex: 1; }}
    .suggest-title {{ font-size: 15.5px; font-weight: 700; color: #fff; margin: 0 0 8px; line-height: 1.4; }}
    .suggest-desc {{ font-size: 13px; color: var(--text-secondary); line-height: 1.5; margin-bottom: 16px; flex: 1; }}
    .suggest-footer {{ display: flex; justify-content: space-between; align-items: center; margin-top: auto; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 12px; }}
    .suggest-action {{ font-size: 12px; font-weight: 700; color: #ff8a00; display: flex; align-items: center; gap: 4px; text-decoration: none; }}

    /* Purchase Toast Notifications */
    #purchase-toast {{
      position: fixed; bottom: 24px; left: 24px; z-index: 99999;
      background: rgba(18, 11, 6, 0.95); border: 1px solid rgba(255, 138, 0, 0.3);
      border-radius: 16px; padding: 16px; width: 320px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5), var(--glow-primary);
      display: flex; align-items: center; gap: 16px;
      transform: translateY(120px); opacity: 0;
      transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      pointer-events: none;
    }}
    #purchase-toast.show {{ transform: translateY(0); opacity: 1; }}
    .purchase-toast-avatar {{
      width: 42px; height: 42px; border-radius: 50%;
      background: rgba(255,138,0,0.1); display: flex; align-items: center;
      justify-content: center; color: #ff8a00; border: 1px solid rgba(255,138,0,0.2);
      flex-shrink: 0; font-weight: 700; font-size: 14px;
    }}
    .purchase-toast-content {{ display: flex; flex-direction: column; gap: 2px; }}
    .purchase-toast-name {{ font-size: 13px; font-weight: 700; color: #fff; }}
    .purchase-toast-prod {{ font-size: 11px; color: var(--text-secondary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 230px; }}
    .purchase-toast-meta {{ font-size: 10px; color: #27c93f; font-weight: 600; display: flex; align-items: center; gap: 4px; }}

    /* Footer */
    footer {{ border-top: 1px solid var(--border-color); padding: 40px 0; text-align: center; background: #020202; }}
    .footer-text {{ font-size: 13px; color: var(--text-muted); margin: 0; }}

    /* Responsive */
    @media (max-width: 991px) {{
      .hero-grid {{ grid-template-columns: 1fr; gap: 32px; }}
      .trustbar-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .earnings-grid {{ grid-template-columns: 1fr; gap: 24px; }}
      .db-apps-grid {{ grid-template-columns: 1fr; }}
      .value-box {{ grid-template-columns: 1fr; gap: 32px; }}
      .value-pay-today {{ border-left: none; border-top: 1px solid rgba(255,255,255,0.08); padding-left: 0; padding-top: 32px; }}
      .suggestions-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .review-grid {{ grid-template-columns: repeat(2, 1fr); }}
      #purchase-toast {{ width: calc(100% - 48px); left: 24px; }}
    }}
    @media (max-width: 768px) {{
      header {{ top: 58px; }}
      #limited-offer-banner {{ font-size: 11px; padding: 8px 36px 8px 12px; }}
      #offer-countdown {{ font-size: 12px; }}
      .suggestions-grid {{ grid-template-columns: 1fr; }}
      .review-grid {{ grid-template-columns: 1fr; }}
    }}
    @media (max-width: 480px) {{
      .pay-today-price {{ font-size: 48px; }}
      .calc-result-value {{ font-size: 38px; }}
    }}
  </style>
</head>
<body>
  <!-- Countdown Announcement Banner -->
  <div id="limited-offer-banner">
    <span>🔥 <strong>LAUNCH OFFER</strong> — Get this pack today at {discount}% off before the price increases!</span>
    <span id="offer-countdown">⏳ Loading...</span>
    <a href="#" onclick="quickBuy('{p["id"]}', '{p_name_escaped}', {p["price"]}, '{p["img"]}', 'product-{p["id"]}.html'); return false;" class="offer-cta-link">Grab Deal →</a>
    <button id="offer-close-btn" onclick="document.getElementById('limited-offer-banner').style.display='none'">✕</button>
  </div>

  <!-- Header -->
  <header>
    <div class="header-inner">
      <a href="index.html" class="logo-wrap">
        <img src="primary-logo.webp" alt="FutureWithAI Logo">
      </a>
      <a href="index.html" class="back-catalog-btn">
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
              <div class="trust-note"><i data-lucide="shield-check" style="width:14px;height:14px;color:#ff8a00;"></i> Secure Payments</div>
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

  <!-- Statistics Ribbon -->
  <section class="trustbar">
    <div class="container">
      <div class="trustbar-grid">
        {stats_ribbon_html}
      </div>
    </div>
  </section>

  <!-- Earning Potential / Benefits Section -->
  <section class="earnings-sec" id="benefits">
    <div class="container">
      <div class="section-header">
        <span class="section-label">⚡ Growth & Earning potential</span>
        <h2 class="section-title">Scale Your Freelancing, Business & Creator Journey</h2>
        <p class="section-desc">Here is exactly how you can leverage these digital assets to build recurring income streams and scale branding.</p>
      </div>
      <div class="earnings-grid">
        {benefits_grid_html}
      </div>
    </div>
  </section>

  <!-- Calculator Section -->
  <section class="calc-sec">
    <div class="container">
      {calculator_html}
    </div>
  </section>

  <!-- Database Inclusions Section -->
  <section class="db-sec" id="inclusions">
    <div class="container">
      <div class="db-container">
        {db_inclusions_html}
      </div>
    </div>
  </section>

  <!-- Value Box Section -->
  <section class="value-sec">
    <div class="container">
      <div class="value-box">
        <div class="value-list">
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
        </div>
        
        <div class="value-pay-today">
          <div class="pay-today-label">You Pay Today:</div>
          {val_pay_today_price}
          {val_pay_today_badge}
          {value_block_actions}
        </div>
      </div>
    </div>
  </section>

  <!-- Testimonials Section -->
  <section class="reviews-sec">
    <div class="container">
      <div class="section-header" style="margin-bottom: 40px;">
        <span class="section-label">⭐ Customer Reviews</span>
        <h2 class="section-title">What Creators & Developers Say</h2>
        <p class="section-desc">Real reviews from verified digital asset buyers.</p>
      </div>
      <div class="review-grid">
        {reviews_html}
      </div>
    </div>
  </section>

  <!-- FAQ Accordion Section -->
  <section class="faq-sec" id="faq">
    <div class="container">
      <div class="section-header" style="margin-bottom: 40px;">
        <span class="section-label">❔ FAQ</span>
        <h2 class="section-title">Frequently Asked Questions</h2>
        <p class="section-desc">Everything you need to know about access, delivery, and licenses.</p>
      </div>
      
      <div class="faq-container">
        {faq_html}
      </div>
    </div>
  </section>

  <!-- Related Products (Connected Loop) -->
  <section class="suggestions-sec">
    <div class="container">
      <div class="section-header" style="margin-bottom: 40px;">
        <span class="section-label">🎁 Toolkit expansions</span>
        <h2 class="section-title">Other Packs You Might Like</h2>
        <p class="section-desc">Expand your resource toolkit with these highly rated bundles.</p>
      </div>
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

  <!-- Floating simulated purchases toast -->
  <div id="purchase-toast">
    <div class="purchase-toast-avatar" id="toast-avatar">R</div>
    <div class="purchase-toast-content">
      <div class="purchase-toast-name" id="toast-buyer-name">Rahul S.</div>
      <div class="purchase-toast-prod" id="toast-prod-name">Gym Reels Pack</div>
      <div class="purchase-toast-meta">
        <i data-lucide="check-circle" style="width:10px;height:10px;"></i> Verified Purchase
      </div>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      if (window.lucide) lucide.createIcons();
      startTimer();
      setupFAQs();
      startPurchaseSimulation();
    }});

    // Countdown Timer
    function startTimer() {{
      const end = Date.now() + (18 * 3600000);
      function tick() {{
        const rem = end - Date.now();
        if (rem <= 0) return;
        const h = Math.floor(rem / 3600000);
        const m = Math.floor((rem % 3600000) / 60000);
        const s = Math.floor((rem % 60000) / 1000);
        const pad = n => String(n).padStart(2, '0');
        const el = document.getElementById('offer-countdown');
        if (el) el.textContent = `⏳ ${{pad(h)}}:${{pad(m)}}:${{pad(s)}}`;
      }}
      tick(); setInterval(tick, 1000);
    }}

    // FAQ Accordion listener
    function setupFAQs() {{
      document.querySelectorAll('.faq-header').forEach(header => {{
        header.addEventListener('click', () => {{
          const item = header.parentElement;
          const isActive = item.classList.contains('active');
          document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));
          if (!isActive) {{
            item.classList.add('active');
          }}
        }});
      }});
    }}

    // Simulated Purchases
    function startPurchaseSimulation() {{
      const buyers = [
        {{ name: 'Rahul Sharma', city: 'Delhi' }},
        {{ name: 'Aniket Patel', city: 'Ahmedabad' }},
        {{ name: 'Vikram Rao', city: 'Bengaluru' }},
        {{ name: 'Priya Sen', city: 'Kolkata' }},
        {{ name: 'Sanjay Deshmukh', city: 'Mumbai' }},
        {{ name: 'Amit Tiwari', city: 'Indore' }},
        {{ name: 'Jayesh Dave', city: 'Pune' }},
        {{ name: 'Sneha Reddy', city: 'Hyderabad' }},
        {{ name: 'Kunal Kapoor', city: 'Chandigarh' }},
        {{ name: 'Meera Nair', city: 'Kochi' }}
      ];
      
      const toast = document.getElementById('purchase-toast');
      const avatar = document.getElementById('toast-avatar');
      const buyerName = document.getElementById('toast-buyer-name');
      const prodName = document.getElementById('toast-prod-name');
      
      function showNextToast() {{
        const b = buyers[Math.floor(Math.random() * buyers.length)];
        buyerName.textContent = `${{b.name}} (${{b.city}})`;
        prodName.textContent = "{p["name"]}";
        avatar.textContent = b.name.charAt(0);
        
        toast.classList.add('show');
        setTimeout(() => {{
          toast.classList.remove('show');
        }}, 4000);
      }}

      // Start after random 8-15 seconds, repeat every 20-30 seconds
      setTimeout(() => {{
        showNextToast();
        setInterval(showNextToast, 25000);
      }}, 8000 + Math.random() * 7000);
    }}

    // Quick Buy helper
    function quickBuy(id, name, price, img, link) {{
      addToCart(id, name, price, img, link);
      if (window.openCart) window.openCart();
    }}

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
    
    // Category Slider JS
    {calculator_js}
  </script>
</body>
</html>"""
        
        # Write to file
        with open(filename, "w", encoding="utf-8") as f_out:
            f_out.write(page_html)
            
    print("All 34 individual landing pages created successfully!")

if __name__ == "__main__":
    generate_product_landing_pages()
