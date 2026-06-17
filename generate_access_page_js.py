import os
import openpyxl
import re

def make_product_id(name):
    clean = re.sub(r'^\d+\.\s*', '', name)
    clean = clean.lower()
    clean = re.sub(r'[^a-z0-9\s-]', '', clean)
    clean = re.sub(r'[\s-]+', '-', clean).strip('-')
    return clean

def generate_access_page():
    excel_path = "PRODUCT.xlsx"
    wb = openpyxl.load_workbook(excel_path, data_only=True)
    sheet = wb.active
    
    product_links_js = "{\n"
    
    # Mapped core packages
    core_packages = [
        {
            "id": "mega-reels",
            "name": "100,000+ Viral Reels Goldmine Pack",
            "link": "https://drive.google.com/drive/folders/1qBpqgApYwv86vNhsqKhJume2NNo_Qg9V",
            "desc": "Access 100,000+ ready-to-use premium viral reels spanning AI Anime, Cricket, Woodwork, Luxury, and Fitness."
        },
        {
            "id": "n8n-automation-enterprise",
            "name": "14,000+ n8n Workflow Automation (Enterprise)",
            "link": "https://drive.google.com/drive/folders/1HK8GYyfqNK6z64BvEzjBMJuH8xM0-LeD",
            "desc": "Access 14,000+ enterprise node schemas, proxy scrapers, CRM connectors, looping systems, and WhatsApp bots."
        },
        {
            "id": "web-apps",
            "name": "1500+ Manually Tested Web App Pack",
            "link": "https://drive.google.com/file/d/1yNQyxLnLbWppNyzdzQhuYXh6f-Vpjf4n/view?usp=drivesdk",
            "desc": "Access 1500+ complete manually tested SaaS web applications source code packages."
        },
        {
            "id": "video-editing",
            "name": "Video Editing Toolkit (500GB+)",
            "link": "https://drive.google.com/drive/folders/10QKbUY7qRyKM3m1ig6EsVQ3KNSJdDZ8Y?usp=drive_link",
            "desc": "Access 500GB+ premium video editing assets - transitions, LUTs, FX presets, and overlays."
        },
        {
            "id": "digital-marketing-bundle",
            "name": "Full Digital Marketing Resource Bundle",
            "link": "https://drive.google.com/drive/folders/1XyNfF4cxEJTkOJHxAjPLILeAqdAutgdX?usp=drive_link",
            "desc": "Access 700+ premium resources including Canva templates, ChatGPT prompts, and full marketing courses."
        },
        {
            "id": "n8n-pack",
            "name": "n8n Automation Pack (2000+ Workflows)",
            "link": "https://github.com/anshumanenterprises1119/futurewithai",
            "desc": "Access 2,000+ standard ready-to-import n8n automation JSON workflows."
        }
    ]
    
    for p in core_packages:
        product_links_js += f"  '{p['id']}': {{\n"
        product_links_js += f"    name: \"{p['name']}\",\n"
        product_links_js += f"    link: \"{p['link']}\",\n"
        product_links_js += f"    desc: \"{p['desc']}\"\n"
        product_links_js += "  },\n"
        
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
        
        prod_id = make_product_id(name)
        desc = f"Direct access link for {name}. Download or bookmark files for offline usage."
        
        product_links_js += f"  '{prod_id}': {{\n"
        product_links_js += f"    name: \"{name}\",\n"
        product_links_js += f"    link: \"{link}\",\n"
        product_links_js += f"    desc: \"{desc}\"\n"
        product_links_js += "  },\n"
        
    product_links_js += "}"

    # Structure of access.html
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Customer Deliverables Access Portal – FutureWithAi</title>
  <meta name="robots" content="noindex,nofollow">
  
  <!-- Favicon -->
  <link rel="icon" type="image/png" href="favicon.webp">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="styles.css">
  <script src="https://unpkg.com/lucide@latest" defer></script>
  
  <style>
    :root {
      --bg-void: #050505;
      --primary: #ffb77f;
      --primary-container: #ff8a00;
      --text-white: #ffffff;
      --text-primary: #f3dfd1;
      --text-secondary: #ddc1ae;
      --text-muted: #a58c7b;
      --border-color: #232323;
      --glow-primary: 0px 0px 20px rgba(255, 138, 0, 0.25);
    }

    body {
      background-color: var(--bg-void);
      color: var(--text-primary);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      font-family: 'Inter', sans-serif;
    }

    .giant-logo-container {
      max-width: 1000px; width: 100%;
      margin: 40px auto 20px auto; padding: 0 24px;
      text-align: center;
    }
    .giant-logo {
      width: 100%; max-width: 1000px; height: auto;
      object-fit: contain; filter: drop-shadow(0px 0px 30px rgba(255, 138, 0, 0.15));
    }

    .portal-container {
      max-width: 900px; margin: 0 auto 80px auto;
      padding: 0 24px; width: 100%;
    }

    .welcome-card {
      text-align: center; margin-bottom: 48px; padding: 40px;
      background: linear-gradient(135deg, rgba(27, 17, 10, 0.4) 0%, rgba(5, 5, 5, 0.8) 100%);
      border: 1px solid var(--border-color); border-radius: 24px;
      box-shadow: var(--glow-primary);
    }
    .welcome-title {
      font-family: 'Playfair Display', serif; font-size: 32px;
      color: var(--text-white); margin-bottom: 12px;
    }
    .welcome-sub {
      font-size: 15px; color: var(--text-secondary); line-height: 1.6;
    }

    .assets-grid {
      display: grid; grid-template-columns: 1fr 1fr;
      gap: 32px; margin-bottom: 48px;
    }
    @media (max-width: 768px) {
      .assets-grid { grid-template-columns: 1fr; gap: 20px; }
    }

    .asset-card {
      background: rgba(20, 20, 20, 0.5);
      border: 1px solid var(--border-color); border-radius: 20px;
      padding: 32px; display: flex; flex-direction: column;
      transition: all 0.3s ease;
    }
    .asset-card:hover {
      border-color: rgba(255, 138, 0, 0.3);
      box-shadow: var(--glow-primary); transform: translateY(-2px);
    }
    .asset-icon {
      width: 48px; height: 48px;
      background: rgba(255, 138, 0, 0.1); border: 1px solid rgba(255, 138, 0, 0.25);
      border-radius: 12px; display: flex; align-items: center; justify-content: center;
      color: var(--primary-container); margin-bottom: 20px;
    }
    .asset-title {
      font-family: 'Playfair Display', serif; font-size: 22px;
      color: var(--text-white); margin-bottom: 12px;
    }
    .asset-desc {
      font-size: 14px; color: var(--text-muted); line-height: 1.6;
      margin-bottom: 28px; flex-grow: 1;
    }

    .bonus-card {
      background: linear-gradient(135deg, rgba(40, 20, 10, 0.3) 0%, rgba(10, 5, 0, 0.7) 100%);
      border: 1px solid rgba(255, 138, 0, 0.25); border-radius: 24px;
      padding: 40px; margin-bottom: 48px; position: relative; overflow: hidden;
    }
    .bonus-card::after {
      content: 'BONUS'; position: absolute; top: 24px; right: -32px;
      background: var(--primary-container); color: #000;
      font-size: 11px; font-weight: 800; padding: 6px 36px;
      transform: rotate(45deg); letter-spacing: 0.1em;
    }
    .bonus-title {
      font-family: 'Playfair Display', serif; font-size: 26px;
      color: var(--text-white); margin-bottom: 12px;
      display: flex; align-items: center; gap: 10px;
    }
    .bonus-desc {
      font-size: 14.5px; color: var(--text-secondary); line-height: 1.6;
      margin-bottom: 24px;
    }

    .bonus-tasks-list {
      display: grid; gap: 16px; margin-bottom: 32px;
    }
    .task-item {
      display: flex; align-items: center; gap: 16px;
      background: rgba(0, 0, 0, 0.3); border: 1px solid var(--border-color);
      padding: 16px 20px; border-radius: 12px;
    }
    .task-number {
      width: 28px; height: 28px;
      background: rgba(255, 138, 0, 0.15); border: 1px solid rgba(255, 138, 0, 0.3);
      border-radius: 50%; display: flex; align-items: center; justify-content: center;
      font-size: 13px; font-weight: 700; color: var(--primary);
    }
    .task-details { flex-grow: 1; }
    .task-details span {
      font-size: 14px; color: var(--text-white); display: block; font-weight: 500;
    }
    .task-link {
      font-size: 12px; color: var(--primary); text-decoration: none;
      display: inline-flex; align-items: center; gap: 4px; margin-top: 2px;
    }
    .task-link:hover { text-decoration: underline; }

    .actions-footer {
      display: flex; justify-content: center; gap: 20px;
    }
    @media (max-width: 768px) {
      .actions-footer { flex-direction: column; align-items: stretch; }
    }
  </style>
</head>
<body style="display: none;">

  <!-- Large Brand Logo -->
  <div class="giant-logo-container">
    <img src="primary-logo.webp" alt="FutureWithAi Brand Logo" class="giant-logo">
  </div>

  <main class="portal-container">
    
    <!-- Welcome Notice -->
    <div class="welcome-card">
      <h2 class="welcome-title">Congratulations on Your Purchase! 🎉</h2>
      <p class="welcome-sub" id="welcome-message-text">
        Thank you for purchasing our digital resource templates. Below you will find the access links to download your items.
      </p>
    </div>

    <!-- Main Assets Section -->
    <h3 style="font-family: 'Playfair Display', serif; font-size: 22px; color: var(--text-white); margin-bottom: 24px; padding-left: 4px;">Your Purchased Assets</h3>
    
    <div class="assets-grid" id="purchased-assets-container">
      <!-- Mapped Download Cards will load here dynamically -->
    </div>

    <!-- Special Bonus Section (Only shown if n8n purchased) -->
    <div class="bonus-card" id="n8n-bonus-card" style="display: none;">
      <h3 class="bonus-title"><i data-lucide="gift" style="width: 28px; height: 28px; color: var(--primary);"></i> Bonus: Get Free Premium n8n Access Trick 🔑</h3>
      <p class="bonus-desc">
        n8n normally charges a monthly subscription or restricts local cloud instances to 14 days. Complete these 3 quick tasks to get our custom step-by-step trick to get free premium n8n access!
      </p>

      <div class="bonus-tasks-list">
        <div class="task-item">
          <div class="task-number">1</div>
          <div class="task-details">
            <span>Follow Future with AI on Instagram</span>
            <a href="https://www.instagram.com/futurewithai2026/" target="_blank" class="task-link">Open Instagram Profile <i data-lucide="external-link" style="width: 12px; height: 12px;"></i></a>
          </div>
        </div>

        <div class="task-item">
          <div class="task-number">2</div>
          <div class="task-details">
            <span>Follow Aditya Tiwari (Founder) on Instagram</span>
            <a href="https://www.instagram.com/about.aaditya/" target="_blank" class="task-link">Open Founder Profile <i data-lucide="external-link" style="width: 12px; height: 12px;"></i></a>
          </div>
        </div>

        <div class="task-item">
          <div class="task-number">3</div>
          <div class="task-details">
            <span>Give 5-Star Review to Anshuman Enterprises (Parent Company)</span>
            <a href="https://g.page/r/CdZ99l9ezVvlEBE/review" target="_blank" class="task-link">Leave Google Map Review <i data-lucide="external-link" style="width: 12px; height: 12px;"></i></a>
          </div>
        </div>
      </div>

      <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px; line-height: 1.5; font-style: italic;">
        <strong>Instructions:</strong> Complete all three steps above, take a screenshot of each proof (following profiles + submitted review), and click the WhatsApp button below to submit them.
      </p>

      <a href="https://wa.me/917065815743?text=Hi%20Aditya%21%20Maine%20teeno%20tasks%20poore%20kar%20liye%20hain%20%28Instagram%20Follows%20%26%20Google%20Review%29.%20Mera%20screenshots%20verify%20karke%20n8n%20free%20trick%20send%20kar%20dein.%20Dhanyawad%21" target="_blank" class="btn-primary" style="text-decoration: none; width: 100%; justify-content: center; gap: 8px; font-size: 15px; font-weight: 700; background: linear-gradient(135deg, #ff8a00, #ffb77f); color: #000; border: none; box-shadow: 0 4px 15px rgba(255, 138, 0, 0.3);">
        <span>Submit Screenshots on WhatsApp</span> <i data-lucide="message-circle"></i>
      </a>
    </div>

    <!-- Printable/Download Footer Actions -->
    <div class="actions-footer">
      <button onclick="window.print()" class="btn-secondary" style="display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 14px; cursor: pointer; padding: 14px 28px; border-radius: 12px; border: 1px solid var(--border-color); color: var(--text-secondary); background: transparent; transition: all 0.3s ease;">
        <i data-lucide="download" style="width: 16px; height: 16px;"></i> Download Page as PDF
      </button>
      <a href="index.html" class="btn-secondary" style="text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 14px; padding: 14px 28px; border-radius: 12px; border: 1px solid var(--border-color); color: var(--text-secondary); background: transparent;">
        <i data-lucide="home" style="width: 16px; height: 16px;"></i> Return to Homepage
      </a>
    </div>

  </main>

  <footer style="margin-top: auto; border-top: 1px solid var(--border-color); padding: 24px; text-align: center; font-size: 12px; color: var(--text-muted); background: rgba(0,0,0,0.2);">
    &copy; 2026 FutureWithAi. Powered by Anshuman Enterprises. All Rights Reserved.
  </footer>

  <script>
    const PRODUCT_LINKS = REPLACE_WITH_PRODUCT_LINKS;
    const FREE_BONUSES = [
      { name: "Black Word with White Background Images", link: "https://drive.google.com/drive/folders/1GzfLUGZpwOklGZK_UB4_ZsvHM5WUb5cz?usp=drive_link", desc: "🎁 FREE BONUS — Minimalist aesthetic quote backgrounds." },
      { name: "Caravan Life Travel Reels", link: "https://drive.google.com/drive/folders/1icBWFJeUT6tbSEbn8xgqu0yjpYca7Qqb?usp=drive_link", desc: "🎁 FREE BONUS — Scenic camper van road trips & landscape reels." },
      { name: "Dog Reels Bundle", link: "https://drive.google.com/drive/folders/1i6GdFMRzlIWFQYPW3Q26VxmmCtkb6Ewl?usp=drive_link", desc: "🎁 FREE BONUS — Cute and funny dog reels for animal niches." },
      { name: "Funny and Cute Cat Bundle", link: "https://drive.google.com/drive/folders/1_eyWC3Xj8MYhsJU1MxX_JZa_KBTl5kB8?usp=drive_link", desc: "🎁 FREE BONUS — Adorable cat compilations for viral reach." },
      { name: "Health Infographic Post Canva", link: "https://drive.google.com/drive/folders/1eTA836EkIIjF1gmFXVg8hy94VPRPC7KV?usp=drive_link", desc: "🎁 FREE BONUS — Editable health infographic designs in Canva." },
      { name: "Lifestyle Reels Bundle", link: "https://drive.google.com/drive/folders/1nk5llkVEXI-1mU2-W9IevjsWovv2gNr_", desc: "🎁 FREE BONUS — Luxury lifestyle and daily inspiration reels." },
      { name: "Luxury Hotels and Resorts", link: "https://drive.google.com/drive/folders/1PHCYdlpYhnS-f0auyYWhgo5SW3x_LgRb?usp=drive_link", desc: "🎁 FREE BONUS — Walkthroughs of top hotels and resorts worldwide." },
      { name: "Travel Reels Bundle", link: "https://drive.google.com/drive/folders/1Aw0KGaR4pcEQiWaldQhWPbgGLjq9lPsJ?usp=drive_link", desc: "🎁 FREE BONUS — Beautiful global travel landscape clips." },
      { name: "5000+ MEGA REELS BUNDLE", link: "https://mega.nz/folder/BBpxDYQQ#OLyaL1a0vDXxG__ddzyxoQ", desc: "🎁 FREE BONUS — Our massive reels collection across popular categories." }
    ];

    function initIcons() { if (typeof lucide !== 'undefined') lucide.createIcons(); else setTimeout(initIcons, 50); }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initIcons); else initIcons();

    // Verification check
    window.addEventListener('DOMContentLoaded', async () => {
      const APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxUBtaPjMCFBydFtF63ntJhIwBTIWadjGJLcO3K0N5jrgsuzEY4wnhAgkLz3KH1_bA/exec";
      const params = new URLSearchParams(window.location.search);
      const orderId = params.get('orderId') || sessionStorage.getItem('ae_verified_order_id');

      if (!orderId) {
        window.location.replace('index.html');
        return;
      }

      // Check cache first
      let cachedData = null;
      try {
        const cached = sessionStorage.getItem('ae_payment_data');
        if (cached) {
          const parsed = JSON.parse(cached);
          if (parsed.merchantOrderId === orderId) {
            cachedData = parsed;
          }
        }
      } catch (e) {}

      let orderData = cachedData;
      if (!orderData) {
        try {
          const response = await fetch(`${APPS_SCRIPT_URL}?action=check_status&orderId=${encodeURIComponent(orderId)}`);
          const data = await response.json();

          if (response.ok && data.success && data.isPaid) {
            orderData = data;
            sessionStorage.setItem('ae_payment_verified', 'true');
            sessionStorage.setItem('ae_verified_order_id', orderId);
            sessionStorage.setItem('ae_payment_data', JSON.stringify(data));
          } else {
            window.location.replace('index.html');
            return;
          }
        } catch (error) {
          console.error('Payment verification failed:', error);
          window.location.replace('index.html');
          return;
        }
      }

      // Render purchased products
      renderPurchasedAssets(orderData);
      document.body.style.display = 'block';
    });

    function renderPurchasedAssets(orderData) {
      const productsStr = orderData.products || '';
      // Split by comma
      const items = productsStr.split(',').map(i => i.trim().toLowerCase()).filter(i => i.length > 0);
      const container = document.getElementById('purchased-assets-container');
      container.innerHTML = '';

      let showN8nBonus = false;
      let matchedCount = 0;

      items.forEach(idOrName => {
        // Find match in PRODUCT_LINKS
        let matchedKey = null;
        if (PRODUCT_LINKS[idOrName]) {
          matchedKey = idOrName;
        } else {
          // Try search by display name or substring match
          matchedKey = Object.keys(PRODUCT_LINKS).find(key => {
            const prod = PRODUCT_LINKS[key];
            return prod.name.toLowerCase().includes(idOrName) || idOrName.includes(key);
          });
        }

        if (matchedKey) {
          matchedCount++;
          const prod = PRODUCT_LINKS[matchedKey];
          
          if (matchedKey.includes('n8n')) {
            showN8nBonus = true;
          }

          // Create card
          const card = document.createElement('div');
          card.className = 'asset-card';
          card.innerHTML = `
            <div class="asset-icon">
              <i data-lucide="folder-git-2" style="width: 24px; height: 24px;"></i>
            </div>
            <h4 class="asset-title">${prod.name}</h4>
            <p class="asset-desc">${prod.desc}</p>
            <a href="${prod.link}" target="_blank" class="btn-primary" style="text-decoration: none; width: 100%; justify-content: center; gap: 8px; font-size: 14px;">
              <span>Access Digital Folder</span> <i data-lucide="external-link"></i>
            </a>
          `;
          container.appendChild(card);
        }
      });

      // Render bonuses
      if (matchedCount > 0) {
        const bonusHeader = document.createElement('h3');
        bonusHeader.style.cssText = "font-family: 'Playfair Display', serif; font-size: 22px; color: var(--text-white); margin: 40px 0 24px 0; padding-left: 4px; grid-column: span 2;";
        bonusHeader.innerHTML = "🎁 Free Bonuses Included with Your Purchase";
        container.appendChild(bonusHeader);

        FREE_BONUSES.forEach(bonus => {
          const card = document.createElement('div');
          card.className = 'asset-card';
          card.style.borderColor = 'rgba(39, 201, 63, 0.25)';
          card.innerHTML = `
            <div class="asset-icon" style="background: rgba(39, 201, 63, 0.1); border-color: rgba(39, 201, 63, 0.3); color: #27c93f;">
              <i data-lucide="gift" style="width: 24px; height: 24px;"></i>
            </div>
            <h4 class="asset-title">${bonus.name}</h4>
            <p class="asset-desc">${bonus.desc}</p>
            <a href="${bonus.link}" target="_blank" class="btn-primary" style="text-decoration: none; width: 100%; justify-content: center; gap: 8px; font-size: 14px; background: linear-gradient(135deg, #27c93f, #1e9a30); color: #fff; border: none; box-shadow: 0 4px 15px rgba(39, 201, 63, 0.25);">
              <span>Download Bonus Link</span> <i data-lucide="external-link"></i>
            </a>
          `;
          container.appendChild(card);
        });
      }

      // If no matched products, show general lookup
      if (matchedCount === 0) {
        container.innerHTML = `
          <div class="asset-card" style="grid-column: span 2; text-align: center;">
            <div class="asset-icon" style="margin: 0 auto 20px auto;">
              <i data-lucide="alert-triangle" style="width: 24px; height: 24px;"></i>
            </div>
            <h4 class="asset-title">Pending Access Details</h4>
            <p class="asset-desc">
              Your purchased items: "${productsStr}" are being verified. If the folder links do not load within 10 minutes, please contact WhatsApp Support with your Order ID: ${orderData.merchantOrderId}.
            </p>
            <a href="https://wa.me/917065815743?text=Hi%20Support,%20Maine%20Order%20${orderData.merchantOrderId}%20kia%20hai%20par%20links%20show%20nahi%20ho%20rahi." target="_blank" class="btn-primary" style="text-decoration: none; width: fit-content; margin: 0 auto; padding: 12px 24px;">
              Contact Support on WhatsApp
            </a>
          </div>
        `;
      }

      if (showN8nBonus) {
        document.getElementById('n8n-bonus-card').style.display = 'block';
      }

      // Re-run icons
      if (window.lucide) lucide.createIcons();
    }
  </script>
</body>
</html>
""".replace("REPLACE_WITH_PRODUCT_LINKS", product_links_js)

    output_path = "access.html"
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(html_content)
        
    print(f"Dynamic access page compiled successfully at '{output_path}'.")

if __name__ == "__main__":
    generate_access_page()
