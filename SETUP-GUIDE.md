# FutureWithAI — Google Apps Script Setup Guide
## Complete Automated Delivery System

---

## 📋 System Overview

Ye system automatically karta hai:
1. ✅ **Payment ke baad** — Token generate hota hai (e.g., `FWA-A3B9C7EC`)
2. ✅ **Email delivery** — Customer ko email jaata hai with:
   - Direct Google Drive download links (sabhi products ke)
   - PDF attachments (agar available hain)
   - Access token for lifetime access
   - Free bonus links
3. ✅ **Thank You page** — Payment success pe:
   - Product download links directly dikhte hain
   - Access token prominently display hota hai (copy button ke saath)
   - Post-purchase upsell banner (30% off pe dusre products)
4. ✅ **Access Portal** — `access.html?token=FWA-XXXXXXXX`
   - Customer kabhi bhi token se apne products access kar sakta hai
   - Bookmarkable URL
5. ✅ **Google Sheet** — Har order log hota hai with:
   - Date, OrderId, Name, Email, Phone, Products, Amount, Status, Delivery, DeliveryDate, EmailBody, AccessToken

---

## 🔧 Step-by-Step Setup

### Step 1: Google Sheet Banao

1. [Google Sheets](https://sheets.google.com) pe jaao
2. New spreadsheet banao: **"FutureWithAI Orders"**
3. First sheet ka naam set karo: **"Orders"**
4. Row 1 mein ye headers dalo:

| A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Date | OrderId | Name | Email | Phone | Products | Amount | Status | Delivery | DeliveryDate | EmailBody | AccessToken |

5. Sheet ka URL note karo — uska Spreadsheet ID chahiye hoga

---

### Step 2: Google Drive Folder Setup

1. Google Drive mein ek folder banao: **"FutureWithAI PDFs"**
2. Is folder mein sabhi product PDFs upload karo (filenames PRODUCT_CATALOG mein match hone chahiye):
   - `mega-reels.pdf`
   - `n8n-automation-enterprise.pdf`
   - `web-apps.pdf`
   - `video-editing.pdf`
   - `digital-marketing-bundle.pdf`
   - etc.
3. Folder ka ID note karo (URL se: `https://drive.google.com/drive/folders/FOLDER_ID`)

---

### Step 3: Google Apps Script Deploy Karo

1. **Apps Script editor kholo:**
   - Google Sheet mein jaao → Extensions → Apps Script
   - Ya directly: [script.google.com](https://script.google.com)

2. **Code paste karo:**
   - `google-apps-script.gs` file ka poora code copy karo
   - Apps Script editor mein paste karo (default `Code.gs` file mein)

3. **Script Properties set karo:**
   - Apps Script editor mein → ⚙️ Project Settings → Script Properties
   - Add these properties:
   
   | Property | Value |
   |----------|-------|
   | `DRIVE_FOLDER_ID` | Google Drive folder ID (Step 2 se) |
   | `GEMINI_API_KEY` | Gemini API key ([Get here](https://aistudio.google.com/app/apikey)) |

4. **Spreadsheet link karo:**
   - Apps Script ko apne Google Sheet se link karo
   - File → Properties → Script Properties mein Spreadsheet ID add karo
   - Ya container-bound script use karo (Sheet se Extensions → Apps Script)

---

### Step 4: Web App Deploy Karo

1. Apps Script editor mein → **Deploy** → **New deployment**
2. Settings:
   - **Type:** Web app
   - **Execute as:** Me
   - **Who has access:** Anyone
3. **Deploy** click karo
4. **Web App URL** copy karo (ye URL website mein use hoga)

> ⚠️ **IMPORTANT:** Har baar code update karne ke baad → Deploy → Manage deployments → Edit → New version → Deploy

---

### Step 5: Website mein URL Update Karo

Agar aapka Web App URL change hota hai, to ye files update karo:

1. **`payment-success.html`** — Line ~390:
   ```js
   const APPS_SCRIPT_URL = "YOUR_NEW_WEB_APP_URL";
   ```

2. **`access.html`** — Line ~459:
   ```js
   const APPS_SCRIPT_URL = "YOUR_NEW_WEB_APP_URL";
   ```

---

### Step 6: Time-based Trigger Set Karo (Backup)

Ye trigger har 5 minute mein check karega ki koi undelivered order to nahi:

1. Apps Script editor mein → **Triggers** (⏰ icon)
2. **Add Trigger:**
   - Function: `processNewSheetRows`
   - Event source: Time-driven
   - Type: Minutes timer
   - Interval: Every 5 minutes
3. Save karo

---

### Step 7: Test Karo

1. Apps Script editor mein `testDelivery()` function run karo
2. Check karo:
   - ✅ Email aaya with product links + token
   - ✅ PDF attachment attached hai
   - ✅ Google Sheet mein row add hua with token

---

## 🔄 Complete Flow Diagram

```
Customer adds to cart → Checkout page (with upsell)
    ↓
Payment gateway (PhonePe/UPI)
    ↓
payment-success.html polls Apps Script (?action=check_status)
    ↓
Apps Script returns: status + accessToken + productLinks
    ↓
Thank You page shows:
  ├─ ✅ Payment confirmation
  ├─ 🔑 Access Token (copyable)
  ├─ 📥 Product download links (clickable)
  ├─ 🚀 Access Portal link (bookmarkable)
  └─ ⚡ Upsell banner (30% off other products)
    ↓
Simultaneously, Apps Script:
  ├─ 📧 Sends email with links + token + PDFs
  ├─ 📊 Logs to Google Sheet
  └─ 🔑 Stores token for lifetime access
    ↓
Customer can revisit: access.html?token=FWA-XXXXXXXX
```

---

## 📱 Product Links Reference

All product Google Drive/MEGA links are stored in:
- **`google-apps-script.gs`** → `PRODUCT_LINKS` object (server-side)
- **`access.html`** → `PRODUCT_LINKS` object (client-side fallback)

> 📌 **MEGA products links are mapped:**
> - 400+ PHP Scripts
> - 200+ Ultimate Web Apps Theme & Plugins  
> - Digital Marketing Bundle
> - 2700+ Elementor Pro Templates
> - 1.37TB Courses Bundle
>
> All of these now point directly to the main MEGA folder link containing the files.

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| Email nahi aa raha | Check DRIVE_FOLDER_ID and GEMINI_API_KEY in Script Properties |
| Token show nahi ho raha | Make sure Apps Script deployed as "New version" after code update |
| Product links nahi dikh rahe | Check PRODUCT_LINKS in google-apps-script.gs for correct keys |
| Access page redirect ho raha | Token/orderId invalid ya payment not completed |
| Sheet update nahi ho raha | Check trigger is active and function has permission |
