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
    filename: '500-animation-explaining-motivation-video.pdf',
    displayName: '1. 500+ Animation Explaining motivation video'
  },
  '500-text-overlay-motivational-videos': {
    filename: '500-text-overlay-motivational-videos.pdf',
    displayName: '2. 500+ Text Overlay motivational videos'
  },
  '500-english-health-reels-bundle': {
    filename: '500-english-health-reels-bundle.pdf',
    displayName: '3. 500+ English Health Reels bundle'
  },
  '700-ai-english-reelsshort': {
    filename: '700-ai-english-reelsshort.pdf',
    displayName: '4. 700+ AI (ENGLISH) Reelsshort'
  },
  '1000-business-growth-reels-bundle': {
    filename: '1000-business-growth-reels-bundle.pdf',
    displayName: '6. 1000+ Business growth Reels Bundle'
  },
  '200-mega-car-reels-bundle': {
    filename: '200-mega-car-reels-bundle.pdf',
    displayName: '9. 200+ Mega Car Reels Bundle'
  },
  '2200-gym-fitness-reels-bundle': {
    filename: '2200-gym-fitness-reels-bundle.pdf',
    displayName: '10. 2200+ Gym_ Fitness Reels Bundle'
  },
  '550-fitness-health-infographic-post-canva': {
    filename: '550-fitness-health-infographic-post-canva.pdf',
    displayName: '11. 550+ Fitness Health Infographic Post Canva'
  },
  'all-in-one-youtuber-kit': {
    filename: 'all-in-one-youtuber-kit.pdf',
    displayName: '12. All In One Youtuber Kit'
  },
  '1000-natures-reels-bundle': {
    filename: '1000-natures-reels-bundle.pdf',
    displayName: '13. 1000 Natures Reels Bundle'
  },
  '1200-space-content-reels-bundle': {
    filename: '1200-space-content-reels-bundle.pdf',
    displayName: '14. 1200+ Space Content Reels Bundle'
  },
  'ai-reels-bundle': {
    filename: 'ai-reels-bundle.pdf',
    displayName: 'AI Reels Bundle'
  },
  'animation-visual-reels-bundle': {
    filename: 'animation-visual-reels-bundle.pdf',
    displayName: 'Animation Visual Reels Bundle'
  },
  'art-and-craft-reels-bundle': {
    filename: 'art-and-craft-reels-bundle.pdf',
    displayName: 'Art and Craft Reels Bundle'
  },
  '1500-glowing-motion-graphics-reels-bundle': {
    filename: '1500-glowing-motion-graphics-reels-bundle.pdf',
    displayName: '1500+ GLowing motion graphics reels bundle:'
  },
  '500-luxury-reels': {
    filename: '500-luxury-reels.pdf',
    displayName: '500+ LUXURY REELS'
  },
  '400-php-scripts': {
    filename: '400-php-scripts.pdf',
    displayName: '400+ PHP scripts'
  },
  '200-ultimate-web-applications-theme-plugins': {
    filename: '200-ultimate-web-applications-theme-plugins.pdf',
    displayName: '200+ Ultimate Web Applications Theme & Plugins'
  },
  '21-hrs-content-of-how-to-work-on-1500-manually-tested-web-app': {
    filename: '21-hrs-content-of-how-to-work-on-1500-manually-tested-web-app.pdf',
    displayName: '21 Hrs Content of How to Work on 1500+ Manually Tested Web App:'
  },
  '1500-premium-transitions': {
    filename: '1500-premium-transitions.pdf',
    displayName: '1500 PREMIUM TRANSITIONS'
  },
  'latest-editing-2026': {
    filename: 'latest-editing-2026.pdf',
    displayName: 'LATEST EDITING 2026'
  },
  'graphics-bundle': {
    filename: 'graphics-bundle.pdf',
    displayName: 'Graphics Bundle'
  },
  'igital-marketing-bundle': {
    filename: 'igital-marketing-bundle.pdf',
    displayName: 'igital Marketing Bundle'
  },
  '2700-elementor-pro-templates-forwordpresssite': {
    filename: '2700-elementor-pro-templates-forwordpresssite.pdf',
    displayName: '2700+ Elementor Pro Templates Forwordpresssite'
  },
  '37tb-all-money-making-courses-bundle': {
    filename: '37tb-all-money-making-courses-bundle.pdf',
    displayName: '1.37tb All Money Making Courses Bundle'
  }
};

const SHEET_NAME = 'Orders';

function deliverOrder(email, name, rawProducts, orderId) {
  Logger.log('Starting delivery for Order: ' + (orderId || 'N/A') + ' to ' + email);
  if (!email || !email.includes('@')) {
    throw new Error('Invalid email address provided: ' + email);
  }
  const productIds = rawProducts.split(',').map(p => p.trim().toLowerCase()).filter(p => p.length > 0);
  const attachments = [];
  const matchedDisplayNames = [];
  let extraNotes = '';
  const scriptProperties = PropertiesService.getScriptProperties();
  const folderId = scriptProperties.getProperty('DRIVE_FOLDER_ID');
  if (!folderId) {
    throw new Error('DRIVE_FOLDER_ID script property is missing!');
  }
  let folder;
  try {
    folder = DriveApp.getFolderById(folderId);
  } catch (e) {
    throw new Error('Could not access Google Drive Folder. Check ID: ' + e.toString());
  }
  productIds.forEach(id => {
    let item = PRODUCT_CATALOG[id];
    if (!item) {
      const foundKey = Object.keys(PRODUCT_CATALOG).find(key => 
        PRODUCT_CATALOG[key].displayName.toLowerCase().includes(id) || id.includes(key)
      );
      if (foundKey) item = PRODUCT_CATALOG[foundKey];
    }
    if (item) {
      matchedDisplayNames.push(item.displayName);
      if (item.filename) {
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
  const prompt = 'You are a customer success AI for \'FutureWithAi\' (futurewithai.anshumanenterprises.online), a premium digital products store. Write a polite, exciting, and professional post-purchase delivery email in Hinglish (Hindi written in English alphabets) for a customer named \'' + name + '\'. They have successfully purchased: ' + productsString + '. Inform them that their official PDF access instruction file(s) are attached. Explain that each PDF contains secure Google Drive links and lifetime access. Advise them to check spam/updates. Mention WhatsApp Support (+91 70658 15743) for help. Keep it friendly. Output ONLY the email body.';
  let emailBody = '';
  let usedGemini = false;
  try {
    const geminiText = callGemini(prompt);
    if (geminiText && geminiText.trim().length > 10) {
      emailBody = geminiText;
      usedGemini = true;
    } else {
      throw new Error('Empty response from Gemini.');
    }
  } catch (err) {
    emailBody = 'Hi ' + name + ',\n\nThank you for purchasing from FutureWithAi!\n\nPlease find your digital delivery PDFs attached to this email. Each PDF contains your secure Google Drive download links and setup instructions.\n\nNote: Check your Spam/Updates folder if you do not see them. Contact WhatsApp Support (+91 70658 15743) if you need help.\n\nBest regards,\nFutureWithAi Team';
  }
  if (extraNotes) {
    emailBody += '\n\n========================================\nADDITIONAL ACCESS DETAILS:' + extraNotes + '\n========================================';
  }
  
  const freeBonusLinks = '\n\n========================================\n🎁 FREE BONUSES INCLUDED WITH YOUR ORDER:\nWe have included all of our premium free resource packs as a special bonus for you! Access them directly below:\n' +
    '- Black Word with White Background Images: https://drive.google.com/drive/folders/1GzfLUGZpwOklGZK_UB4_ZsvHM5WUb5cz?usp=drive_link\n' +
    '- Caravan Life Travel Reels: https://drive.google.com/drive/folders/1icBWFJeUT6tbSEbn8xgqu0yjpYca7Qqb?usp=drive_link\n' +
    '- Dog Reels Bundle: https://drive.google.com/drive/folders/1i6GdFMRzlIWFQYPW3Q26VxmmCtkb6Ewl?usp=drive_link\n' +
    '- Funny and Cute Cat Bundle: https://drive.google.com/drive/folders/1_eyWC3Xj8MYhsJU1MxX_JZa_KBTl5kB8?usp=drive_link\n' +
    '- Health Infographic Post Canva: https://drive.google.com/drive/folders/1eTA836EkIIjF1gmFXVg8hy94VPRPC7KV?usp=drive_link\n' +
    '- Lifestyle Reels Bundle: https://drive.google.com/drive/folders/1nk5llkVEXI-1mU2-W9IevjsWovv2gNr_\n' +
    '- Luxury Hotels and Resorts Travel Reels: https://drive.google.com/drive/folders/1PHCYdlpYhnS-f0auyYWhgo5SW3x_LgRb?usp=drive_link\n' +
    '- Travel Reels Bundle: https://drive.google.com/drive/folders/1Aw0KGaR4pcEQiWaldQhWPbgGLjq9lPsJ?usp=drive_link\n' +
    '- 5000+ MEGA REELS BUNDLE: https://mega.nz/folder/BBpxDYQQ#OLyaL1a0vDXxG__ddzyxoQ\n' +
    '========================================';
  emailBody += freeBonusLinks;

  const subject = '🎉 Your FutureWithAi Purchase is Ready! — ' + name;
  MailApp.sendEmail({
    to: email,
    subject: subject,
    body: emailBody,
    attachments: attachments
  });
  return { success: true, products: productsString, usedGemini: usedGemini, emailBody: emailBody };
}

function callGemini(prompt) {
  const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
  if (!apiKey || apiKey.trim() === '') {
    throw new Error('GEMINI_API_KEY is not set in Script Properties.');
  }
  
  const cleanKey = apiKey.replace(/\s+/g, '');
  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=' + cleanKey;
  
  const payload = {
    contents: [{
      parts: [{
        text: prompt
      }]
    }]
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

function processNewSheetRows() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) return;
  const lastRow = sheet.getLastRow();
  if (lastRow <= 1) return;
  const dataRange = sheet.getRange(2, 1, lastRow - 1, 11);
  const data = dataRange.getValues();
  for (let i = 0; i < data.length; i++) {
    const rowNum = i + 2;
    const orderId = data[i][1];
    const name    = data[i][2];
    const email   = data[i][3];
    const rawProd = data[i][5];
    const status  = String(data[i][7]).trim().toUpperCase();
    const deliv   = String(data[i][8]).trim().toUpperCase();
    if ((status === 'PAID' || status === 'COMPLETED' || status === 'SUCCESS') && deliv !== 'SENT' && deliv !== 'PROCESSING') {
      sheet.getRange(rowNum, 9).setValue('PROCESSING');
      SpreadsheetApp.flush();
      try {
        const result = deliverOrder(email, name, String(rawProd), String(orderId));
        sheet.getRange(rowNum, 9).setValue('SENT');
        sheet.getRange(rowNum, 10).setValue(new Date());
        sheet.getRange(rowNum, 11).setValue(result.emailBody);
      } catch (err) {
        sheet.getRange(rowNum, 9).setValue('FAILED: ' + err.message);
      }
      SpreadsheetApp.flush();
    }
  }
}

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
    const amount = payload.amount || 0;
    const phone = payload.phone || payload.whatsapp || '';
    const status = (payload.status || 'COMPLETED').toUpperCase();
    if (!email || !rawProducts) throw new Error('Missing fields');
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = ss.getSheetByName(SHEET_NAME);
    sheet.appendRow([new Date(), orderId, name, email, phone, rawProducts, amount, status, 'PENDING', '', '']);
    SpreadsheetApp.flush();
    if (status === 'COMPLETED' || status === 'PAID' || status === 'SUCCESS') {
      const result = deliverOrder(email, name, rawProducts, orderId);
      const lastRow = sheet.getLastRow();
      sheet.getRange(lastRow, 9).setValue('SENT');
      sheet.getRange(lastRow, 10).setValue(new Date());
      sheet.getRange(lastRow, 11).setValue(result.emailBody);
      SpreadsheetApp.flush();
      return ContentService.createTextOutput(JSON.stringify({ success: true, message: 'Delivered' })).setMimeType(ContentService.MimeType.JSON);
    }
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ success: false, error: error.message })).setMimeType(ContentService.MimeType.JSON);
  }
}

function testDelivery() {
  const testEmail = Session.getActiveUser().getEmail();
  const testName = "Aditya Tiwari";
  const testProducts = "mega-reels, n8n-pack"; 
  const testOrderId = "TEST-ORDER-" + Math.floor(Math.random() * 100000);
  
  Logger.log("Running manual test...");
  try {
    const result = deliverOrder(testEmail, testName, testProducts, testOrderId);
    Logger.log("SUCCESS! Test report:");
    Logger.log("- Products identified: " + result.products);
    Logger.log("- Gemini AI utilized: " + (result.usedGemini ? "Yes" : "No"));
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

function doGet(e) {
  try {
    const action = e.parameter.action;
    if (action === 'check_status') {
      const orderId = e.parameter.orderId;
      if (!orderId) throw new Error('Missing orderId');
      
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      const sheet = ss.getSheetByName(SHEET_NAME);
      if (!sheet) throw new Error('Orders sheet not found');
      
      const lastRow = sheet.getLastRow();
      if (lastRow <= 1) {
        return ContentService.createTextOutput(JSON.stringify({ success: false, message: 'No orders found' })).setMimeType(ContentService.MimeType.JSON);
      }
      
      const data = sheet.getRange(2, 1, lastRow - 1, 8).getValues();
      for (let i = 0; i < data.length; i++) {
        const rowOrderId = String(data[i][1]).trim();
        if (rowOrderId === String(orderId).trim()) {
          const name = data[i][2];
          const email = data[i][3];
          const products = data[i][5];
          const amount = data[i][6];
          const status = String(data[i][7]).trim().toUpperCase();
          
          const isPaid = (status === 'COMPLETED' || status === 'PAID' || status === 'SUCCESS');
          return ContentService.createTextOutput(JSON.stringify({
            success: true,
            state: isPaid ? 'COMPLETED' : status,
            isPaid: isPaid,
            amount: amount,
            merchantOrderId: orderId,
            products: products,
            successPayment: {
              amount: amount,
              paymentMode: 'UPI',
              transactionId: orderId
            }
          })).setMimeType(ContentService.MimeType.JSON);
        }
      }
      
      return ContentService.createTextOutput(JSON.stringify({
        success: true,
        state: 'PENDING',
        isPaid: false,
        message: 'Order not found, checking...'
      })).setMimeType(ContentService.MimeType.JSON);
    }
    
    return ContentService.createTextOutput(JSON.stringify({ success: false, error: 'Unknown action' })).setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ success: false, error: error.message })).setMimeType(ContentService.MimeType.JSON);
  }
}
