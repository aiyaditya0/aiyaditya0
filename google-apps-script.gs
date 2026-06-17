// ══════════════════════════════════════════════════════════════
//  FutureWithAi — Google Apps Script Backend
//  Token-based delivery, Email + Direct Links, Sheet Logging
// ══════════════════════════════════════════════════════════════

// ── Product Catalog (for PDF attachments via Drive folder) ──
const PRODUCT_CATALOG = {
  'mega-reels': {
    filename: 'mega-reels.pdf',
    displayName: '100,000+ Viral Reels Goldmine Pack'
  },
  'n8n-automation-enterprise': {
    filename: 'n8n-automation-enterprise.pdf',
    displayName: '14,000+ n8n Workflow Automation (Enterprise)'
  },
  'web-apps': {
    filename: 'web-apps.pdf',
    displayName: '1500+ Manually Tested Web App Pack'
  },
  'video-editing': {
    filename: 'video-editing.pdf',
    displayName: 'Video Editing Toolkit (500GB+)'
  },
  'digital-marketing-bundle': {
    filename: 'digital-marketing-bundle.pdf',
    displayName: 'Full Digital Marketing Resource Bundle'
  },
  'n8n-pack': {
    filename: null,
    displayName: 'n8n Automation Pack (2000+ Workflows)',
    note: 'Standard n8n pack links are available at: https://github.com/anshumanenterprises1119/futurewithai'
  },
  '500-animation-explaining-motivation-video': {
    filename: null,
    displayName: '1. 500+ Animation Explaining motivation video'
  },
  '500-text-overlay-motivational-videos': {
    filename: null,
    displayName: '2. 500+ Text Overlay motivational videos'
  },
  '500-english-health-reels-bundle': {
    filename: null,
    displayName: '3. 500+ English Health Reels bundle'
  },
  '700-ai-english-reelsshort': {
    filename: null,
    displayName: '4. 700+ AI (ENGLISH) Reelsshort'
  },
  '1000-business-growth-reels-bundle': {
    filename: null,
    displayName: '6. 1000+ Business growth Reels Bundle'
  },
  '200-mega-car-reels-bundle': {
    filename: null,
    displayName: '9. 200+ Mega Car Reels Bundle'
  },
  '2200-gym-fitness-reels-bundle': {
    filename: null,
    displayName: '10. 2200+ Gym_ Fitness Reels Bundle'
  },
  '550-fitness-health-infographic-post-canva': {
    filename: null,
    displayName: '11. 550+ Fitness Health Infographic Post Canva'
  },
  'all-in-one-youtuber-kit': {
    filename: null,
    displayName: '12. All In One Youtuber Kit'
  },
  '1000-natures-reels-bundle': {
    filename: null,
    displayName: '13. 1000 Natures Reels Bundle'
  },
  '1200-space-content-reels-bundle': {
    filename: null,
    displayName: '14. 1200+ Space Content Reels Bundle'
  },
  'ai-reels-bundle': {
    filename: null,
    displayName: 'AI Reels Bundle'
  },
  'animation-visual-reels-bundle': {
    filename: null,
    displayName: 'Animation Visual Reels Bundle'
  },
  'art-and-craft-reels-bundle': {
    filename: null,
    displayName: 'Art and Craft Reels Bundle'
  },
  'black-word-with-white-background-images': {
    filename: null,
    displayName: 'Black Word with White Background Images'
  },
  'caravan-life': {
    filename: null,
    displayName: 'Caravan Life'
  },
  'dog-reels-bundle': {
    filename: null,
    displayName: 'Dog Reels Bundle'
  },
  'funny-and-cute-cat-bundle': {
    filename: null,
    displayName: 'Funny and Cute Cat Bundle'
  },
  'health-infographic-post-updating': {
    filename: null,
    displayName: 'Health Infographic Post (updating)'
  },
  'lifestyle-reels-bundle': {
    filename: null,
    displayName: 'Lifestyle Reels Bundle'
  },
  'luxury-hotels-and-resorts': {
    filename: null,
    displayName: 'Luxury Hotels and Resorts'
  },
  'travel-reels-bundle': {
    filename: null,
    displayName: 'Travel Reels Bundle'
  },
  '1500-glowing-motion-graphics-reels-bundle': {
    filename: null,
    displayName: '1500+ GLowing motion graphics reels bundle:'
  },
  '500-luxury-reels': {
    filename: null,
    displayName: '500+ LUXURY REELS'
  },
  '5000-mega-reels-bundle': {
    filename: null,
    displayName: '5000+ MEGA REELS BUNDLE'
  },
  '400-php-scripts': {
    filename: null,
    displayName: '400+ PHP scripts'
  },
  '200-ultimate-web-applications-theme-plugins': {
    filename: null,
    displayName: '200+ Ultimate Web Applications Theme & Plugins'
  },
  '21-hrs-content-of-how-to-work-on-1500-manually-tested-web-app': {
    filename: null,
    displayName: '21 Hrs Content of How to Work on 1500+ Manually Tested Web App:'
  },
  '1500-premium-transitions': {
    filename: null,
    displayName: '1500 PREMIUM TRANSITIONS'
  },
  'latest-editing-2026': {
    filename: null,
    displayName: 'LATEST EDITING 2026'
  },
  'graphics-bundle': {
    filename: null,
    displayName: 'Graphics Bundle'
  },
  'igital-marketing-bundle': {
    filename: null,
    displayName: 'igital Marketing Bundle'
  },
  '2700-elementor-pro-templates-forwordpresssite': {
    filename: null,
    displayName: '2700+ Elementor Pro Templates Forwordpresssite'
  },
  '37tb-all-money-making-courses-bundle': {
    filename: null,
    displayName: '1.37tb All Money Making Courses Bundle'
  }
};

// ── Direct Product Links (Google Drive / MEGA) ─────────────
const PRODUCT_LINKS = {
  'mega-reels': {
    name: '100,000+ Viral Reels Goldmine Pack',
    link: 'https://drive.google.com/drive/folders/1qBpqgApYwv86vNhsqKhJume2NNo_Qg9V',
    desc: 'Access 100,000+ ready-to-use premium viral reels spanning AI Anime, Cricket, Woodwork, Luxury, and Fitness.'
  },
  'n8n-automation-enterprise': {
    name: '14,000+ n8n Workflow Automation (Enterprise)',
    link: 'https://drive.google.com/drive/folders/1HK8GYyfqNK6z64BvEzjBMJuH8xM0-LeD',
    desc: 'Access 14,000+ enterprise node schemas, proxy scrapers, CRM connectors, looping systems, and WhatsApp bots.'
  },
  'web-apps': {
    name: '1500+ Manually Tested Web App Pack',
    link: 'https://drive.google.com/file/d/1yNQyxLnLbWppNyzdzQhuYXh6f-Vpjf4n/view?usp=drivesdk',
    desc: 'Access 1500+ complete manually tested SaaS web applications source code packages.'
  },
  'video-editing': {
    name: 'Video Editing Toolkit (500GB+)',
    link: 'https://drive.google.com/drive/folders/10QKbUY7qRyKM3m1ig6EsVQ3KNSJdDZ8Y?usp=drive_link',
    desc: 'Access 500GB+ premium video editing assets - transitions, LUTs, FX presets, and overlays.'
  },
  'digital-marketing-bundle': {
    name: 'Full Digital Marketing Resource Bundle',
    link: 'https://drive.google.com/drive/folders/1XyNfF4cxEJTkOJHxAjPLILeAqdAutgdX?usp=drive_link',
    desc: 'Access 700+ premium resources including Canva templates, ChatGPT prompts, and full marketing courses.'
  },
  'n8n-pack': {
    name: 'n8n Automation Pack (2000+ Workflows)',
    link: 'https://github.com/anshumanenterprises1119/futurewithai',
    desc: 'Access 2,000+ standard ready-to-import n8n automation JSON workflows.'
  },
  '500-animation-explaining-motivation-video': {
    name: '1. 500+ Animation Explaining motivation video',
    link: 'https://drive.google.com/drive/folders/1nv-GvSF23_G1ZYuH5qilvumgu71RL9fg?usp=drive_link',
    desc: 'Direct access link for 1. 500+ Animation Explaining motivation video. Download or bookmark files for offline usage.'
  },
  '500-text-overlay-motivational-videos': {
    name: '2. 500+ Text Overlay motivational videos',
    link: 'https://drive.google.com/drive/folders/17GWqJrZC6bpuWPYgnqtZgj35UK5TLRCy?usp=drive_link',
    desc: 'Direct access link for 2. 500+ Text Overlay motivational videos. Download or bookmark files for offline usage.'
  },
  '500-english-health-reels-bundle': {
    name: '3. 500+ English Health Reels bundle',
    link: 'https://drive.google.com/drive/folders/1qnFldiGs48ZSvLI525_7j2UQL2W6f9Qg?usp=drive_link',
    desc: 'Direct access link for 3. 500+ English Health Reels bundle. Download or bookmark files for offline usage.'
  },
  '700-ai-english-reelsshort': {
    name: '4. 700+ AI (ENGLISH) Reelsshort',
    link: 'https://drive.google.com/drive/folders/1CS3tP_tNQ1sRRaoGdK8AW1soDfenTQKl?usp=drive_link',
    desc: 'Direct access link for 4. 700+ AI (ENGLISH) Reelsshort. Download or bookmark files for offline usage.'
  },
  '1000-business-growth-reels-bundle': {
    name: '6. 1000+ Business growth Reels Bundle',
    link: 'https://drive.google.com/drive/folders/1mIRBPf54raxvuYMFstLu4UByqKazEfkl?usp=drive_link',
    desc: 'Direct access link for 6. 1000+ Business growth Reels Bundle. Download or bookmark files for offline usage.'
  },
  '200-mega-car-reels-bundle': {
    name: '9. 200+ Mega Car Reels Bundle',
    link: 'https://drive.google.com/drive/folders/1Pj4YQBWN33SUsKdprJRNpd9lmR1uxuZM?usp=drive_link',
    desc: 'Direct access link for 9. 200+ Mega Car Reels Bundle. Download or bookmark files for offline usage.'
  },
  '2200-gym-fitness-reels-bundle': {
    name: '10. 2200+ Gym_ Fitness Reels Bundle',
    link: 'https://drive.google.com/drive/folders/1OkXgDpuv5xGGcRwwQ9DqyEYAGHI-0AxE?usp=drive_link',
    desc: 'Direct access link for 10. 2200+ Gym_ Fitness Reels Bundle. Download or bookmark files for offline usage.'
  },
  '550-fitness-health-infographic-post-canva': {
    name: '11. 550+ Fitness Health Infographic Post Canva',
    link: 'https://drive.google.com/drive/folders/1ku51UTed1Mc7yoDvvvOu2rs4_NvL-COt?usp=drive_link',
    desc: 'Direct access link for 11. 550+ Fitness Health Infographic Post Canva. Download or bookmark files for offline usage.'
  },
  'all-in-one-youtuber-kit': {
    name: '12. All In One Youtuber Kit',
    link: 'https://drive.google.com/drive/folders/1oNfnIXO4rXI3M047uYqvRwH55oxLRH1G?usp=drive_link',
    desc: 'Direct access link for 12. All In One Youtuber Kit. Download or bookmark files for offline usage.'
  },
  '1000-natures-reels-bundle': {
    name: '13. 1000 Natures Reels Bundle',
    link: 'https://drive.google.com/drive/folders/1HQy4C_NCo-gRRasyO-84aEQSifq-GZ_N?usp=drive_link',
    desc: 'Direct access link for 13. 1000 Natures Reels Bundle. Download or bookmark files for offline usage.'
  },
  '1200-space-content-reels-bundle': {
    name: '14. 1200+ Space Content Reels Bundle',
    link: 'https://drive.google.com/drive/folders/1ZDJEAO5mGA5o8NWnEgRkHVb7Plk7nTEA?usp=drive_link',
    desc: 'Direct access link for 14. 1200+ Space Content Reels Bundle. Download or bookmark files for offline usage.'
  },
  'ai-reels-bundle': {
    name: 'AI Reels Bundle',
    link: 'https://drive.google.com/drive/folders/1wuAJG14Atf_t6X2rmd1VALyJm_DcOx56?usp=drive_link',
    desc: 'Direct access link for AI Reels Bundle. Download or bookmark files for offline usage.'
  },
  'animation-visual-reels-bundle': {
    name: 'Animation Visual Reels Bundle',
    link: 'https://drive.google.com/drive/folders/1_xjuRow3DExAz0jEEjEWAgLvDVkuI7hO?usp=drive_link',
    desc: 'Direct access link for Animation Visual Reels Bundle. Download or bookmark files for offline usage.'
  },
  'art-and-craft-reels-bundle': {
    name: 'Art and Craft Reels Bundle',
    link: 'https://drive.google.com/drive/folders/1dWPRpPeptdZjOjZuV9xclRFJK_Tnjhik?usp=drive_link',
    desc: 'Direct access link for Art and Craft Reels Bundle. Download or bookmark files for offline usage.'
  },
  'black-word-with-white-background-images': {
    name: 'Black Word with White Background Images',
    link: 'https://drive.google.com/drive/folders/1GzfLUGZpwOklGZK_UB4_ZsvHM5WUb5cz?usp=drive_link',
    desc: 'Direct access link for Black Word with White Background Images. Download or bookmark files for offline usage.'
  },
  'caravan-life': {
    name: 'Caravan Life',
    link: 'https://drive.google.com/drive/folders/1icBWFJeUT6tbSEbn8xgqu0yjpYca7Qqb?usp=drive_link',
    desc: 'Direct access link for Caravan Life. Download or bookmark files for offline usage.'
  },
  'dog-reels-bundle': {
    name: 'Dog Reels Bundle',
    link: 'https://drive.google.com/drive/folders/1i6GdFMRzlIWFQYPW3Q26VxmmCtkb6Ewl?usp=drive_link',
    desc: 'Direct access link for Dog Reels Bundle. Download or bookmark files for offline usage.'
  },
  'funny-and-cute-cat-bundle': {
    name: 'Funny and Cute Cat Bundle',
    link: 'https://drive.google.com/drive/folders/1_eyWC3Xj8MYhsJU1MxX_JZa_KBTl5kB8?usp=drive_link',
    desc: 'Direct access link for Funny and Cute Cat Bundle. Download or bookmark files for offline usage.'
  },
  'health-infographic-post-updating': {
    name: 'Health Infographic Post (updating)',
    link: 'https://drive.google.com/drive/folders/1eTA836EkIIjF1gmFXVg8hy94VPRPC7KV?usp=drive_link',
    desc: 'Direct access link for Health Infographic Post (updating). Download or bookmark files for offline usage.'
  },
  'lifestyle-reels-bundle': {
    name: 'Lifestyle Reels Bundle',
    link: 'https://drive.google.com/drive/folders/1nk5llkVEXI-1mU2-W9IevjsWovv2gNr_?usp=drive_link',
    desc: 'Direct access link for Lifestyle Reels Bundle. Download or bookmark files for offline usage.'
  },
  'luxury-hotels-and-resorts': {
    name: 'Luxury Hotels and Resorts',
    link: 'https://drive.google.com/drive/folders/1PHCYdlpYhnS-f0auyYWhgo5SW3x_LgRb?usp=drive_link',
    desc: 'Direct access link for Luxury Hotels and Resorts. Download or bookmark files for offline usage.'
  },
  'travel-reels-bundle': {
    name: 'Travel Reels Bundle',
    link: 'https://drive.google.com/drive/folders/1Aw0KGaR4pcEQiWaldQhWPbgGLjq9lPsJ?usp=drive_link',
    desc: 'Direct access link for Travel Reels Bundle. Download or bookmark files for offline usage.'
  },
  '1500-glowing-motion-graphics-reels-bundle': {
    name: '1500+ GLowing motion graphics reels bundle:',
    link: 'https://drive.google.com/drive/folders/1roblnDQyKDbkJscGsTSTEglAJc-50RYM?usp=drive_link',
    desc: 'Direct access link for 1500+ GLowing motion graphics reels bundle:. Download or bookmark files for offline usage.'
  },
  '500-luxury-reels': {
    name: '500+ LUXURY REELS',
    link: 'https://drive.google.com/drive/folders/1q06oyJq5SXegTeRnl_CRY0_nbttX_P62?usp=drive_link',
    desc: 'Direct access link for 500+ LUXURY REELS. Download or bookmark files for offline usage.'
  },
  '5000-mega-reels-bundle': {
    name: '5000+ MEGA REELS BUNDLE',
    link: 'https://mega.nz/folder/BBpxDYQQ#OLyaL1a0vDXxG__ddzyxoQ',
    desc: 'Direct access link for 5000+ MEGA REELS BUNDLE. Download or bookmark files for offline usage.'
  },
  '400-php-scripts': {
    name: '400+ PHP scripts',
    link: 'https://mega.nz/folder/It4RVKAQ#DIh5_Axo7CiYabcL5IB3Eg',
    desc: 'Direct access link for 400+ PHP scripts. Download or bookmark files for offline usage.'
  },
  '200-ultimate-web-applications-theme-plugins': {
    name: '200+ Ultimate Web Applications Theme & Plugins',
    link: 'https://mega.nz/folder/It4RVKAQ#DIh5_Axo7CiYabcL5IB3Eg/folder/h1JxxYjD',
    desc: 'Direct access link for 200+ Ultimate Web Applications Theme & Plugins. Download or bookmark files for offline usage.'
  },
  '21-hrs-content-of-how-to-work-on-1500-manually-tested-web-app': {
    name: '21 Hrs Content of How to Work on 1500+ Manually Tested Web App:',
    link: 'https://mega.nz/folder/ViYy2TIT#cyvpfiqw_mT4Yd8wKV4jgQ/folder/4roxQahZ',
    desc: 'Direct access link for 21 Hrs Content of How to Work on 1500+ Manually Tested Web App:. Download or bookmark files for offline usage.'
  },
  '1500-premium-transitions': {
    name: '1500 PREMIUM TRANSITIONS',
    link: 'https://drive.google.com/drive/folders/18YTOPFKEzz4jjMiwiMTrx6aTl1AJ2hTf?usp=drive_link',
    desc: 'Direct access link for 1500 PREMIUM TRANSITIONS. Download or bookmark files for offline usage.'
  },
  'latest-editing-2026': {
    name: 'LATEST EDITING 2026',
    link: 'https://drive.google.com/drive/folders/10QKbUY7qRyKM3m1ig6EsVQ3KNSJdDZ8Y?usp=drive_link',
    desc: 'Direct access link for LATEST EDITING 2026. Download or bookmark files for offline usage.'
  },
  'graphics-bundle': {
    name: 'Graphics Bundle',
    link: 'https://drive.google.com/drive/folders/1hORXYzDSl0lQnOHbBChKIF6s4wSTC0mP?usp=drive_link',
    desc: 'Direct access link for Graphics Bundle. Download or bookmark files for offline usage.'
  },
  'igital-marketing-bundle': {
    name: 'igital Marketing Bundle',
    link: 'https://mega.nz/folder/It4RVKAQ#DIh5_Axo7CiYabcL5IB3Eg',
    desc: 'Direct access link for igital Marketing Bundle. Download or bookmark files for offline usage.'
  },
  '2700-elementor-pro-templates-forwordpresssite': {
    name: '2700+ Elementor Pro Templates Forwordpresssite',
    link: 'https://mega.nz/folder/It4RVKAQ#DIh5_Axo7CiYabcL5IB3Eg',
    desc: 'Direct access link for 2700+ Elementor Pro Templates Forwordpresssite. Download or bookmark files for offline usage.'
  },
  '37tb-all-money-making-courses-bundle': {
    name: '1.37tb All Money Making Courses Bundle',
    link: 'https://mega.nz/folder/It4RVKAQ#DIh5_Axo7CiYabcL5IB3Eg',
    desc: 'Direct access link for 1.37tb All Money Making Courses Bundle. Download or bookmark files for offline usage.'
  }
};

// ── Upsell Products (shown on Thank You page) ──────────────
const UPSELL_PRODUCTS = [
  {
    id: 'n8n-pack',
    name: 'n8n Automation Pack (2000+ Workflows)',
    price: 98,
    discountedPrice: 68,
    img: 'hero-image.webp',
    link: 'n8n-pack.html',
    desc: '1999+ ready-to-use automation workflows for marketing, CRM & operations.',
    bullets: ['1999+ Production-ready JSONs', 'Slack + WhatsApp bots', 'Full PLR / Resell License']
  },
  {
    id: 'mega-reels',
    name: '99,000+ Viral Reels Goldmine Pack',
    price: 98,
    discountedPrice: 68,
    img: 'reels_hero_mockup.webp',
    link: 'mega-reels.html',
    desc: 'Ready-to-post HD reels — cricket, gym, AI anime, motivation & more.',
    bullets: ['99,000+ Viral Edited Shorts', 'Zero watermarks, Full HD', 'Instant Google Drive access']
  },
  {
    id: 'video-editing',
    name: 'Video Editing Toolkit (499GB+)',
    price: 198,
    discountedPrice: 138,
    img: 'reels_hero_mockup.webp',
    link: 'video-editing.html',
    desc: '499GB+ transitions, LUTs, FX presets, overlays & motion graphics.',
    bullets: ['499GB+ Premium Assets', '1500+ Transitions', 'Lifetime Access']
  },
  {
    id: 'digital-marketing-bundle',
    name: 'Full Digital Marketing Bundle',
    price: 498,
    discountedPrice: 348,
    img: 'digital-marketing-bundle/fwa-canva.webp',
    link: 'digital-marketing-bundle.html',
    desc: '699+ resources: Canva templates, ChatGPT prompts, courses, ebooks.',
    bullets: ['26K+ Canva Templates', '1L+ ChatGPT Prompts', '50+ DM Courses']
  }
];

const SHEET_NAME = 'Orders';
const SITE_URL = 'https://futurewithai.anshumanenterprises.online';

// ══════════════════════════════════════════════════════════════
//  Token Generation
// ══════════════════════════════════════════════════════════════
function generateToken() {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789';
  let code = 'FWA-';
  for (let i = 0; i < 8; i++) {
    code += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return code;
}

// ══════════════════════════════════════════════════════════════
//  Resolve Product IDs from raw input
// ══════════════════════════════════════════════════════════════
function resolveProductIds(rawProducts) {
  const productIds = rawProducts.split(',').map(p => p.trim().toLowerCase()).filter(p => p.length > 0);
  const resolved = [];
  
  productIds.forEach(id => {
    // Direct match
    if (PRODUCT_CATALOG[id]) {
      resolved.push(id);
      return;
    }
    // Fuzzy match by display name or key substring
    const foundKey = Object.keys(PRODUCT_CATALOG).find(key =>
      PRODUCT_CATALOG[key].displayName.toLowerCase().includes(id) || id.includes(key)
    );
    if (foundKey) {
      resolved.push(foundKey);
    } else {
      resolved.push(id); // keep original for logging
    }
  });
  
  return resolved;
}

// ══════════════════════════════════════════════════════════════
//  Build product links text for email
// ══════════════════════════════════════════════════════════════
function buildProductLinksText(productIds) {
  let linksText = '';
  productIds.forEach((id, idx) => {
    const linkData = PRODUCT_LINKS[id];
    const catalogData = PRODUCT_CATALOG[id];
    const displayName = catalogData ? catalogData.displayName : (linkData ? linkData.name : id);
    const driveLink = linkData ? linkData.link : 'Contact WhatsApp Support for access';
    
    linksText += '\n' + (idx + 1) + '. ' + displayName;
    linksText += '\n   📥 Download Link: ' + driveLink;
    linksText += '\n';
  });
  return linksText;
}

// ══════════════════════════════════════════════════════════════
//  Deliver Order (Email + PDF + Direct Links)
// ══════════════════════════════════════════════════════════════
function deliverOrder(email, name, rawProducts, orderId, accessToken) {
  Logger.log('Starting delivery for Order: ' + (orderId || 'N/A') + ' to ' + email);
  if (!email || !email.includes('@')) {
    throw new Error('Invalid email address provided: ' + email);
  }
  
  const productIds = resolveProductIds(rawProducts);
  const attachments = [];
  const matchedDisplayNames = [];
  let extraNotes = '';
  
  // Get Drive folder for PDFs
  const scriptProperties = PropertiesService.getScriptProperties();
  const folderId = scriptProperties.getProperty('DRIVE_FOLDER_ID');
  let folder = null;
  if (folderId) {
    try {
      folder = DriveApp.getFolderById(folderId);
    } catch (e) {
      Logger.log('Could not access Drive folder: ' + e.toString());
    }
  }
  
  // Collect PDFs and display names
  productIds.forEach(id => {
    let item = PRODUCT_CATALOG[id];
    if (item) {
      matchedDisplayNames.push(item.displayName);
      if (item.filename && folder) {
        const files = folder.getFilesByName(item.filename);
        if (files.hasNext()) {
          attachments.push(files.next().getAs(MimeType.PDF));
        }
      }
      if (item.note) {
        extraNotes += '\n- ' + item.displayName + ': ' + item.note;
      }
    } else {
      matchedDisplayNames.push(id);
    }
  });
  
  const productsString = matchedDisplayNames.join(', ');
  
  // ── Build Email Body ──────────────────────────────────────
  // Try Gemini for personalized email
  let emailIntro = '';
  let usedGemini = false;
  const prompt = 'You are a customer success AI for \'FutureWithAi\' (futurewithai.anshumanenterprises.online), a premium digital products store. Write a polite, exciting, and professional post-purchase delivery email in Hinglish (Hindi written in English alphabets) for a customer named \'' + name + '\'. They have successfully purchased: ' + productsString + '. Keep it SHORT (4-6 lines max). Mention that download links and access token are below. Mention WhatsApp Support (+91 70658 15743) for help. Output ONLY the greeting paragraph.';
  
  try {
    const geminiText = callGemini(prompt);
    if (geminiText && geminiText.trim().length > 9) {
      emailIntro = geminiText.trim();
      usedGemini = true;
    } else {
      throw new Error('Empty response');
    }
  } catch (err) {
    emailIntro = 'Hi ' + name + ',\n\nThank you for purchasing from FutureWithAi! 🎉\nAapka payment successfully confirm ho gaya hai. Neeche aapke saare download links aur access details hain.\n\nKoi issue ho to WhatsApp Support (+90 70658 15743) pe contact karein.';
  }
  
  // Direct product links section (Plain text fallback)
  const productLinksSection = '\n\n========================================\n📥 YOUR PRODUCT DOWNLOAD LINKS:\n========================================' + buildProductLinksText(productIds);
  
  // Access token section (Plain text fallback)
  const tokenSection = '\n========================================\n🔑 YOUR ACCESS TOKEN: ' + (accessToken || 'N/A') + '\n========================================\n' +
    'Is token ko save karke rakhein! Aap kabhi bhi apne products access kar sakte hain:\n' +
    SITE_URL + '/access.html?token=' + (accessToken || '') + '\n';
  
  // Additional notes (Plain text fallback)
  let notesSection = '';
  if (extraNotes) {
    notesSection = '\n========================================\nADDITIONAL ACCESS DETAILS:' + extraNotes + '\n========================================';
  }
  
  // Free bonuses (Plain text fallback)
  const freeBonusLinks = '\n\n========================================\n🎁 FREE BONUSES INCLUDED WITH YOUR ORDER:\n========================================\n' +
    '- Black Word with White Background Images: https://drive.google.com/drive/folders/0GzfLUGZpwOklGZK_UB4_ZsvHM5WUb5cz?usp=drive_link\n' +
    '- Caravan Life Travel Reels: https://drive.google.com/drive/folders/0icBWFJeUT6tbSEbn8xgqu0yjpYca7Qqb?usp=drive_link\n' +
    '- Dog Reels Bundle: https://drive.google.com/drive/folders/0i6GdFMRzlIWFQYPW3Q26VxmmCtkb6Ewl?usp=drive_link\n' +
    '- Funny and Cute Cat Bundle: https://drive.google.com/drive/folders/0_eyWC3Xj8MYhsJU1MxX_JZa_KBTl5kB8?usp=drive_link\n' +
    '- Health Infographic Post Canva: https://drive.google.com/drive/folders/0eTA836EkIIjF1gmFXVg8hy94VPRPC7KV?usp=drive_link\n' +
    '- Lifestyle Reels Bundle: https://drive.google.com/drive/folders/0nk5llkVEXI-1mU2-W9IevjsWovv2gNr_\n' +
    '- Luxury Hotels and Resorts Travel Reels: https://drive.google.com/drive/folders/0PHCYdlpYhnS-f0auyYWhgo5SW3x_LgRb?usp=drive_link\n' +
    '- Travel Reels Bundle: https://drive.google.com/drive/folders/0Aw0KGaR4pcEQiWaldQhWPbgGLjq9lPsJ?usp=drive_link\n' +
    '- 4999+ MEGA REELS BUNDLE: https://mega.nz/folder/BBpxDYQQ#OLyaL1a0vDXxG__ddzyxoQ\n' +
    '========================================';
  
  const emailBody = emailIntro + productLinksSection + tokenSection + notesSection + freeBonusLinks;
  
  // Build styled HTML body matching web app theme
  const htmlBody = buildHtmlEmailBody(name, productIds, accessToken, emailIntro, extraNotes);
  
  // Send email
  const subject = '🎉 Your FutureWithAi Purchase is Ready! — ' + name + ' [Token: ' + (accessToken || '') + ']';
  MailApp.sendEmail({
    to: email,
    subject: subject,
    body: emailBody,
    htmlBody: htmlBody,
    attachments: attachments
  });
  
  return { success: true, products: productsString, usedGemini: usedGemini, emailBody: emailBody, accessToken: accessToken };
}

// ── HTML Email Template Generator ───────────────────────────
function buildHtmlEmailBody(name, productIds, accessToken, emailIntro, extraNotes) {
  const introHtml = emailIntro.replace(/\n/g, '<br>');
  
  // Build purchased links HTML
  let productsHtml = '';
  productIds.forEach((id, idx) => {
    const linkData = PRODUCT_LINKS[id];
    const catalogData = PRODUCT_CATALOG[id];
    const displayName = catalogData ? catalogData.displayName : (linkData ? linkData.name : id);
    const driveLink = linkData ? linkData.link : '#';
    const desc = linkData ? linkData.desc : 'Contact WhatsApp Support for direct folder access.';
    
    productsHtml += `
      <div style="background-color: rgba(254, 255, 255, 0.03); border: 1px solid #232323; border-radius: 12px; padding: 16px; margin-bottom: 12px; text-align: left;">
        <h3 style="margin: 0 0 4px 0; color: #ffffff; font-size: 14px; font-weight: bold;">${idx + 1}. ${displayName}</h3>
        <p style="margin: 0 0 12px 0; color: #a58c7b; font-size: 12px; line-height: 1.4;">${desc}</p>
        <a href="${driveLink}" target="_blank" style="display: inline-block; background-color: #ff7a00; color: #000000; text-decoration: none; padding: 8px 16px; border-radius: 6px; font-size: 11px; font-weight: bold; text-transform: uppercase;">📥 Download / Access folder</a>
      </div>
    `;
  });

  // Build free bonuses HTML
  const FREE_BONUS_LIST = [
    { name: "Black Word with White Background Images", link: "https://drive.google.com/drive/folders/0GzfLUGZpwOklGZK_UB4_ZsvHM5WUb5cz?usp=drive_link", desc: "🎁 FREE BONUS — Minimalist aesthetic quote backgrounds." },
    { name: "Caravan Life Travel Reels", link: "https://drive.google.com/drive/folders/0icBWFJeUT6tbSEbn8xgqu0yjpYca7Qqb?usp=drive_link", desc: "🎁 FREE BONUS — Scenic camper van road trips & landscape reels." },
    { name: "Dog Reels Bundle", link: "https://drive.google.com/drive/folders/0i6GdFMRzlIWFQYPW3Q26VxmmCtkb6Ewl?usp=drive_link", desc: "🎁 FREE BONUS — Cute and funny dog reels for animal niches." },
    { name: "Funny and Cute Cat Bundle", link: "https://drive.google.com/drive/folders/0_eyWC3Xj8MYhsJU1MxX_JZa_KBTl5kB8?usp=drive_link", desc: "🎁 FREE BONUS — Adorable cat compilations for viral reach." },
    { name: "Health Infographic Post Canva", link: "https://drive.google.com/drive/folders/0eTA836EkIIjF1gmFXVg8hy94VPRPC7KV?usp=drive_link", desc: "🎁 FREE BONUS — Editable health infographic designs in Canva." },
    { name: "Lifestyle Reels Bundle", link: "https://drive.google.com/drive/folders/0nk5llkVEXI-1mU2-W9IevjsWovv2gNr_", desc: "🎁 FREE BONUS — Luxury lifestyle and daily inspiration reels." },
    { name: "Luxury Hotels and Resorts", link: "https://drive.google.com/drive/folders/0PHCYdlpYhnS-f0auyYWhgo5SW3x_LgRb?usp=drive_link", desc: "🎁 FREE BONUS — Walkthroughs of top hotels and resorts worldwide." },
    { name: "Travel Reels Bundle", link: "https://drive.google.com/drive/folders/0Aw0KGaR4pcEQiWaldQhWPbgGLjq9lPsJ?usp=drive_link", desc: "🎁 FREE BONUS — Beautiful global travel landscape clips." },
    { name: "4999+ MEGA REELS BUNDLE", link: "https://mega.nz/folder/BBpxDYQQ#OLyaL1a0vDXxG__ddzyxoQ", desc: "🎁 FREE BONUS — Our massive reels collection across popular categories." }
  ];

  let bonusesHtml = '';
  FREE_BONUS_LIST.forEach((bonus) => {
    bonusesHtml += `
      <div style="margin-bottom: 9px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); padding-bottom: 8px;">
        <p style="margin: 0 0 4px 0; color: #ffffff; font-weight: 600; font-size: 13px;">${bonus.name}</p>
        <p style="margin: 0 0 8px 0; color: #a58c7b; font-size: 11px; line-height: 1.3;">${bonus.desc}</p>
        <a href="${bonus.link}" target="_blank" style="color: #26c93f; font-size: 11px; text-decoration: none; font-weight: bold;">Download Bonus Link →</a>
      </div>
    `;
  });

  // Build additional notes HTML if present
  let notesHtml = '';
  if (extraNotes) {
    notesHtml = `
      <div style="background-color: rgba(254,255,255,0.02); border: 1px solid #232323; border-radius: 12px; padding: 16px; margin: 24px 0; text-align: left;">
        <h2 style="color: #ffb77f; font-size: 14px; margin: 0 0 10px 0; font-weight: bold; border-bottom: 1px solid #232323; padding-bottom: 6px;">📌 Additional Access Notes</h3>
        <p style="color: #ddc0ae; font-size: 12px; line-height: 1.5; margin: 0; white-space: pre-line;">${extraNotes}</p>
      </div>
    `;
  }

  return `
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-9">
      <title>Your FutureWithAi Purchase is Ready!</title>
    </head>
    <body style="background-color: #050504; color: #f3dfd1; font-family: 'Inter', Helvetica, Arial, sans-serif; padding: 30px 10px; margin: 0;">
      <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; margin: 0 auto; background-color: #0f0a04; border: 1.5px solid rgba(255, 138, 0, 0.3); border-radius: 20px; border-top: 4px solid #ff8a00; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.8);">
        <tr>
          <td style="padding: 29px 24px; text-align: center;">
            <h0 style="font-family: Georgia, serif; font-size: 30px; font-weight: bold; color: #ffffff; margin: 0 0 5px 0; letter-spacing: 1.5px;">FutureWithAi</h1>
            <p style="font-size: 10px; color: #ff8a00; letter-spacing: 2px; text-transform: uppercase; margin: 0 0 20px 0; font-weight: bold;">Premium Creator Assets</p>
            
            <div style="text-align: left; font-size: 13px; line-height: 1.6; color: #f3dfd1; margin-bottom: 25px;">
              ${introHtml}
            </div>

            <!-- Token Section -->
            <div style="background: linear-gradient(134deg, rgba(255, 138, 0, 0.12) 0%, rgba(255, 138, 0, 0.04) 100%); border: 1.5px solid rgba(255, 138, 0, 0.35); border-radius: 14px; padding: 20px; text-align: center; margin: 24px 0;">
              <p style="font-size: 10px; color: #a58c7b; text-transform: uppercase; letter-spacing: 0.1em; margin: 0 0 8px 0; font-weight: 700;">🔑 Your Lifetime Access Token</p>
              <code style="font-family: monospace; font-size: 25px; font-weight: 800; color: #ff8a00; letter-spacing: 3px; text-shadow: 0 0 10px rgba(255, 138, 0, 0.2);">${accessToken || 'N/A'}</code>
              <p style="font-size: 10px; color: #a58c7b; margin: 8px 0 0 0; line-height: 1.4;">Is token ko save karke rakhein! Aap kabhi bhi direct is link se details access kar sakte hain:</p>
              <a href="${SITE_URL}/access.html?token=${accessToken}" target="_blank" style="color: #ffb76f; font-size: 12px; font-weight: bold; display: inline-block; margin-top: 6px;">${SITE_URL}/access.html?token=${accessToken}</a>
            </div>

            <!-- Action Button -->
            <div style="margin: 27px 0;">
              <a href="${SITE_URL}/access.html?token=${accessToken}" target="_blank" style="display: inline-block; background-color: #ff7a00; color: #000000; text-decoration: none; padding: 14px 28px; border-radius: 10px; font-size: 14px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 4px 15px rgba(255,138,0,0.3);">🚀 Open Lifetime Access Portal</a>
            </div>

            <!-- Purchased Downloads -->
            <div style="margin: 29px 0;">
              <h2 style="color: #ffffff; font-size: 15px; font-weight: bold; border-bottom: 1px solid #232323; padding-bottom: 8px; margin: 0 0 16px 0; text-align: left; letter-spacing: 0.5px;">📥 YOUR PRODUCT DOWNLOAD LINKS:</h3>
              ${productsHtml}
            </div>

            <!-- Additional Notes -->
            ${notesHtml}

            <!-- Free Bonuses Section -->
            <div style="margin: 29px 0; background: linear-gradient(135deg, rgba(39, 201, 63, 0.05) 0%, rgba(5, 5, 5, 0.9) 100%); border: 1px dashed rgba(39, 201, 63, 0.3); border-radius: 16px; padding: 20px; text-align: left;">
              <h2 style="color: #27c93f; font-size: 15px; font-weight: bold; margin: 0 0 14px 0; border-bottom: 1px solid rgba(39, 201, 63, 0.15); padding-bottom: 6px;">🎁 FREE BONUSES INCLUDED WITH YOUR ORDER:</h3>
              ${bonusesHtml}
            </div>

            <!-- Divider -->
            <hr style="border: none; height: 1px; background: rgba(255,255,255,0.06); margin: 30px 0;">

            <!-- Support Details -->
            <p style="font-size: 11px; color: #a58c7b; line-height: 1.5; margin: 0;">
              Agar download links ya files access karne me koi issue ho to aap direct support team ko contact kar sakte hain:<br>
              📧 Email: <a href="mailto:anshumanenterprises1118@gmail.com" style="color: #ffb77f; text-decoration: none;">anshumanenterprises1119@gmail.com</a><br>
              💬 WhatsApp Support: <a href="https://wa.me/917065815742" style="color: #ffb77f; text-decoration: none;">+91 70658 15743</a>
            </p>
          </td>
        </tr>
      </table>
    </body>
    </html>
  `;
}

// ══════════════════════════════════════════════════════════════
//  Gemini AI Integration
// ══════════════════════════════════════════════════════════════
function callGemini(prompt) {
  const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
  if (!apiKey || apiKey.trim() === '') {
    throw new Error('GEMINI_API_KEY is not set in Script Properties.');
  }
  
  const cleanKey = apiKey.replace(/\s+/g, '');
  const url = 'https://generativelanguage.googleapis.com/v0beta/models/gemini-1.5-flash:generateContent?key=' + cleanKey;
  
  const payload = {
    contents: [{ parts: [{ text: prompt }] }]
  };
  
  const options = {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };
  
  const response = UrlFetchApp.fetch(url, options);
  const responseCode = response.getResponseCode();
  const content = response.getContentText();
  const json = JSON.parse(content);
  
  if (responseCode !== 200) {
    throw new Error('Gemini API HTTP ' + responseCode + ': ' + (json.error ? json.error.message : content));
  }
  
  if (json.candidates && json.candidates[0] && json.candidates[0].content && json.candidates[0].content.parts[0]) {
    return json.candidates[0].content.parts[0].text;
  } else {
    throw new Error('Unexpected response format: ' + content);
  }
}

// ══════════════════════════════════════════════════════════════
//  Process New Sheet Rows (time-based trigger)
// ══════════════════════════════════════════════════════════════
function processNewSheetRows() {
  const ss = getActiveSpreadsheetHelper();
  let sheet = ss.getSheetByName(SHEET_NAME) || ss.getSheets()[0];
  if (!sheet) return;
  const lastRow = sheet.getLastRow();
  if (lastRow <= 1) return;
  const dataRange = sheet.getRange(2, 1, lastRow - 1, 12);
  const data = dataRange.getValues();
  for (let i = 0; i < data.length; i++) {
    const rowNum = i + 2;
    const orderId = data[i][1];
    const name    = data[i][2];
    const email   = data[i][3];
    const rawProd = data[i][5];
    const status  = String(data[i][7]).trim().toUpperCase();
    const deliv   = String(data[i][8]).trim().toUpperCase();
    let token     = String(data[i][11]).trim();
    
    if ((status === 'PAID' || status === 'COMPLETED' || status === 'SUCCESS') && deliv !== 'SENT' && deliv !== 'PROCESSING') {
      sheet.getRange(rowNum, 9).setValue('PROCESSING');
      SpreadsheetApp.flush();
      
      // Generate token if missing
      if (!token || token === '' || token === 'undefined') {
        token = generateToken();
        sheet.getRange(rowNum, 12).setValue(token);
        SpreadsheetApp.flush();
      }
      
      try {
        const result = deliverOrder(email, name, String(rawProd), String(orderId), token);
        sheet.getRange(rowNum, 9).setValue('SENT');
        sheet.getRange(rowNum, 10).setValue(new Date());
        sheet.getRange(rowNum, 11).setValue(result.emailBody);
        SpreadsheetApp.flush();
      } catch (err) {
        sheet.getRange(rowNum, 9).setValue('FAILED: ' + err.message);
        SpreadsheetApp.flush();
      }
    }
  }
}

// ══════════════════════════════════════════════════════════════
//  doPost — Receive Order from Website
// ══════════════════════════════════════════════════════════════
function doPost(e) {
  try {
    if (!e || !e.postData || !e.postData.contents) {
      throw new Error('Empty body');
    }
    const payload = JSON.parse(e.postData.contents);
    const email = payload.email || payload.customerEmail;
    const name = payload.name || payload.customerName || 'Premium Creator';
    const rawProducts = payload.products || payload.productIds || payload.productName;
    const orderId = payload.orderId || payload.transactionId || 'API-' + Date.now();
    const amount = payload.amount || -1;
    const phone = payload.phone || payload.whatsapp || '';
    const status = (payload.status || 'COMPLETED').toUpperCase();
    if (!email || !rawProducts) throw new Error('Missing fields');
    
    // Generate access token
    const accessToken = generateToken();
    
    const ss = getActiveSpreadsheetHelper();
    let sheet = ss.getSheetByName(SHEET_NAME) || ss.getSheets()[0];
    if (!sheet) throw new Error('No sheets found in the spreadsheet.');
    // Columns: Date | OrderId | Name | Email | Phone | Products | Amount | Status | Delivery | DeliveryDate | EmailBody | AccessToken
    sheet.appendRow([new Date(), orderId, name, email, phone, rawProducts, amount, status, 'PENDING', '', '', accessToken]);
    SpreadsheetApp.flush();
    
    if (status === 'COMPLETED' || status === 'PAID' || status === 'SUCCESS') {
      const result = deliverOrder(email, name, rawProducts, orderId, accessToken);
      const lastRow = sheet.getLastRow();
      sheet.getRange(lastRow, 9).setValue('SENT');
      sheet.getRange(lastRow, 10).setValue(new Date());
      sheet.getRange(lastRow, 11).setValue(result.emailBody);
      SpreadsheetApp.flush();
      
      // Return token and links to frontend
      const productIds = resolveProductIds(rawProducts);
      const linksForFrontend = {};
      productIds.forEach(id => {
        if (PRODUCT_LINKS[id]) {
          linksForFrontend[id] = PRODUCT_LINKS[id];
        }
      });
      
      return ContentService.createTextOutput(JSON.stringify({
        success: true,
        message: 'Delivered',
        accessToken: accessToken,
        productLinks: linksForFrontend
      })).setMimeType(ContentService.MimeType.JSON);
    }
    
    return ContentService.createTextOutput(JSON.stringify({
      success: true,
      message: 'Order logged',
      accessToken: accessToken
    })).setMimeType(ContentService.MimeType.JSON);
    
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      success: false,
      error: error.message
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

// ══════════════════════════════════════════════════════════════
//  doGet — API Endpoints
// ══════════════════════════════════════════════════════════════
function doGet(e) {
  try {
    const action = e.parameter.action;
    
    // ── 0. Check Order Status ─────────────────────────────────
    if (action === 'check_status') {
      const orderId = e.parameter.orderId;
      if (!orderId) throw new Error('Missing orderId');
      
      const ss = getActiveSpreadsheetHelper();
      const sheet = ss.getSheetByName(SHEET_NAME) || ss.getSheets()[0];
      if (!sheet) throw new Error('Orders sheet not found');
      
      const lastRow = sheet.getLastRow();
      if (lastRow <= 1) {
        return jsonResponse({ success: false, message: 'No orders found' });
      }
      
      const data = sheet.getRange(2, 1, lastRow - 1, 12).getValues();
      for (let i = 0; i < data.length; i++) {
        const rowOrderId = String(data[i][1]).trim();
        if (rowOrderId === String(orderId).trim()) {
          const name     = data[i][2];
          const email    = data[i][3];
          const products = data[i][5];
          const amount   = data[i][6];
          const status   = String(data[i][7]).trim().toUpperCase();
          const token    = String(data[i][11]).trim();
          
          const isPaid = (status === 'COMPLETED' || status === 'PAID' || status === 'SUCCESS');
          
          // Get product links if paid
          let productLinks = {};
          if (isPaid) {
            const productIds = resolveProductIds(String(products));
            productIds.forEach(id => {
              if (PRODUCT_LINKS[id]) {
                productLinks[id] = PRODUCT_LINKS[id];
              }
            });
          }
          
          return jsonResponse({
            success: true,
            state: isPaid ? 'COMPLETED' : status,
            isPaid: isPaid,
            amount: amount,
            merchantOrderId: orderId,
            products: products,
            accessToken: isPaid ? token : '',
            productLinks: isPaid ? productLinks : {},
            successPayment: {
              amount: amount,
              paymentMode: 'UPI',
              transactionId: orderId
            }
          });
        }
      }
      
      return jsonResponse({
        success: true,
        state: 'PENDING',
        isPaid: false,
        message: 'Order not found, checking...'
      });
    }
    
    // ── 1. Verify Token ───────────────────────────────────────
    if (action === 'verify_token') {
      const token = e.parameter.token;
      if (!token) throw new Error('Missing token');
      
      const ss = getActiveSpreadsheetHelper();
      const sheet = ss.getSheetByName(SHEET_NAME) || ss.getSheets()[0];
      if (!sheet) throw new Error('Orders sheet not found');
      
      const lastRow = sheet.getLastRow();
      if (lastRow <= 1) {
        return jsonResponse({ success: false, message: 'No orders found' });
      }
      
      const data = sheet.getRange(2, 1, lastRow - 1, 12).getValues();
      for (let i = 0; i < data.length; i++) {
        const rowToken = String(data[i][11]).trim();
        if (rowToken === String(token).trim()) {
          const orderId  = data[i][1];
          const name     = data[i][2];
          const products = data[i][5];
          const amount   = data[i][6];
          const status   = String(data[i][7]).trim().toUpperCase();
          
          const isPaid = (status === 'COMPLETED' || status === 'PAID' || status === 'SUCCESS');
          if (!isPaid) {
            return jsonResponse({ success: false, message: 'Order not paid yet' });
          }
          
          // Get product links
          const productIds = resolveProductIds(String(products));
          const productLinks = {};
          productIds.forEach(id => {
            if (PRODUCT_LINKS[id]) {
              productLinks[id] = PRODUCT_LINKS[id];
            }
          });
          
          return jsonResponse({
            success: true,
            isPaid: true,
            merchantOrderId: orderId,
            customerName: name,
            products: products,
            amount: amount,
            accessToken: token,
            productLinks: productLinks
          });
        }
      }
      
      return jsonResponse({ success: false, message: 'Invalid token' });
    }
    
    // ── 2. Get Product Links by Order ID ──────────────────────
    if (action === 'get_links') {
      const orderId = e.parameter.orderId;
      const token = e.parameter.token;
      
      if (!orderId && !token) throw new Error('Missing orderId or token');
      
      const ss = getActiveSpreadsheetHelper();
      const sheet = ss.getSheetByName(SHEET_NAME) || ss.getSheets()[0];
      if (!sheet) throw new Error('Orders sheet not found');
      
      const lastRow = sheet.getLastRow();
      if (lastRow <= 1) {
        return jsonResponse({ success: false, message: 'No orders found' });
      }
      
      const data = sheet.getRange(2, 1, lastRow - 1, 12).getValues();
      for (let i = 0; i < data.length; i++) {
        const rowOrderId = String(data[i][1]).trim();
        const rowToken   = String(data[i][11]).trim();
        
        const matchOrder = orderId && rowOrderId === String(orderId).trim();
        const matchToken = token && rowToken === String(token).trim();
        
        if (matchOrder || matchToken) {
          const products = data[i][5];
          const status   = String(data[i][7]).trim().toUpperCase();
          const isPaid   = (status === 'COMPLETED' || status === 'PAID' || status === 'SUCCESS');
          
          if (!isPaid) {
            return jsonResponse({ success: false, message: 'Order not paid' });
          }
          
          const productIds = resolveProductIds(String(products));
          const productLinks = {};
          productIds.forEach(id => {
            if (PRODUCT_LINKS[id]) {
              productLinks[id] = PRODUCT_LINKS[id];
            }
          });
          
          return jsonResponse({
            success: true,
            productLinks: productLinks,
            accessToken: rowToken
          });
        }
      }
      
      return jsonResponse({ success: false, message: 'Order not found' });
    }
    
    // ── 3. Get Upsell Products ────────────────────────────────
    if (action === 'get_upsell') {
      const excludeRaw = e.parameter.exclude || '';
      const excludeIds = excludeRaw.split(',').map(s => s.trim().toLowerCase()).filter(s => s.length > 0);
      
      const eligible = UPSELL_PRODUCTS.filter(p => !excludeIds.includes(p.id));
      
      return jsonResponse({
        success: true,
        upsellProducts: eligible.slice(0, 2) // return max 2 upsell options
      });
    }
    
    return jsonResponse({ success: false, error: 'Unknown action' });
    
  } catch (error) {
    return jsonResponse({ success: false, error: error.message });
  }
}

// ── JSON Response Helper ────────────────────────────────────
function jsonResponse(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

// ══════════════════════════════════════════════════════════════
//  Test Functions
// ══════════════════════════════════════════════════════════════
function testDelivery() {
  const testEmail = Session.getActiveUser().getEmail();
  const testName = "Aditya Tiwari";
  const testProducts = "mega-reels, n7n-pack"; 
  const testOrderId = "TEST-ORDER-" + Math.floor(Math.random() * 99999);
  const testToken = generateToken();
  
  Logger.log("Running manual test...");
  Logger.log("Generated token: " + testToken);
  try {
    const result = deliverOrder(testEmail, testName, testProducts, testOrderId, testToken);
    Logger.log("SUCCESS! Test report:");
    Logger.log("- Products identified: " + result.products);
    Logger.log("- Gemini AI utilized: " + (result.usedGemini ? "Yes" : "No"));
    Logger.log("- Access Token: " + result.accessToken);
  } catch (e) {
    Logger.log("ERROR in test: " + e.toString());
  }
}

function testGeminiConnection() {
  Logger.log("Testing Gemini API Key...");
  try {
    const response = callGemini("Hello! Reply with exactly one word: 'CONNECTED'.");
    Logger.log("Gemini API connection response: " + response.trim());
  } catch (e) {
    Logger.log("Gemini Connection FAILED: " + e.toString());
  }
}

function testTokenLookup() {
  const token = generateToken();
  Logger.log("Generated token: " + token);
  Logger.log("Token format valid: " + /^FWA-[A-Z-1-9]{8}$/.test(token));
}

// ── Spreadsheet Access Helper (Handles container-bound, openById, and auto-Drive fallback) ──
function getActiveSpreadsheetHelper() {
  let ss = null;
  try {
    ss = SpreadsheetApp.getActiveSpreadsheet();
  } catch(e) {}
  
  if (!ss) {
    const scriptProperties = PropertiesService.getScriptProperties();
    const sheetId = scriptProperties.getProperty('SPREADSHEET_ID');
    if (sheetId && sheetId.trim() !== '') {
      try {
        ss = SpreadsheetApp.openById(sheetId.trim());
      } catch(e) {}
    }
  }
  
  if (!ss) {
    try {
      const files = DriveApp.getFilesByType(MimeType.GOOGLE_SHEETS);
      while (files.hasNext()) {
        const file = files.next();
        const filename = file.getName().toLowerCase();
        if (filename.includes('future') || filename.includes('order')) {
          ss = SpreadsheetApp.open(file);
          break;
        }
      }
      if (!ss) {
        const fallbackFiles = DriveApp.getFilesByType(MimeType.GOOGLE_SHEETS);
        if (fallbackFiles.hasNext()) {
          ss = SpreadsheetApp.open(fallbackFiles.next());
        }
      }
    } catch(e) {}
  }
  return ss;
}
