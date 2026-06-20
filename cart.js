/**
 * FutureWithAi - Global Shopping Cart System
 * Persistent Client-side Cart via LocalStorage
 * + Smart Upsell Modal before Checkout
 */

(function () {
  // --- Cart State Management ---
  const STORAGE_KEY = 'fwai_cart_items';

  function getCart() {
    try {
      const items = localStorage.getItem(STORAGE_KEY);
      return items ? JSON.parse(items) : [];
    } catch (e) {
      return [];
    }
  }

  function saveCart(cart) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(cart));
    } catch (e) {}
  }

  // ─── Upsell Product Catalog (only ≤₹99 eligible) ───────────────────────────
  const UPSELL_CATALOG = [
    {
      id: 'n8n-pack',
      name: 'n8n Automation Pack',
      fullName: 'n8n Automation Pack (2000+ Workflows)',
      desc: '2000+ ready-to-use automation workflows for marketing, CRM & operations.',
      bullets: ['2000+ Production-ready JSONs', 'Slack + WhatsApp + Email bots', 'Full PLR / Resell License'],
      price: 99,
      img: 'hero-image.webp',
      link: 'n8n-pack.html',
      emoji: '🤖',
    },
    {
      id: 'mega-reels',
      name: 'Viral Reels Goldmine Pack',
      fullName: '100,000+ Viral Reels Goldmine Pack',
      desc: 'Ready-to-post HD reels — cricket, gym, AI anime, motivation & more.',
      bullets: ['100,000+ Viral Edited Shorts', 'Zero watermarks, Full HD', 'Instant Google Drive access'],
      price: 99,
      img: 'reels_hero_mockup.webp',
      link: 'mega-reels.html',
      emoji: '📱',
    },
  ];

  const DISCOUNT_PCT = 30; // % off on upsell

  // Pick an upsell product NOT already in the cart
  function getUpsellProduct(cart) {
    const cartIds = cart.map(i => i.id);
    // Rotate based on cart size so different products show for 1, 2, 3 items
    const eligible = UPSELL_CATALOG.filter(p => !cartIds.includes(p.id));
    if (eligible.length === 0) return null;
    // For 1 item in cart → first eligible; for 2 → next eligible; etc.
    return eligible[(cart.length - 1) % eligible.length] || eligible[0];
  }

  // ─── Dynamic Cart UI Injection ───────────────────────────────────────────────
  function injectCartUI() {
    // Cart Drawer
    if (!document.getElementById('cartDrawer')) {
      const overlay = document.createElement('div');
      overlay.className = 'cart-drawer-overlay';
      overlay.id = 'cartOverlay';
      document.body.appendChild(overlay);

      const drawer = document.createElement('div');
      drawer.className = 'cart-drawer';
      drawer.id = 'cartDrawer';
      drawer.innerHTML = `
        <div class="cart-drawer-header">
          <div class="cart-drawer-title">
            <i data-lucide="shopping-cart" style="width:22px;height:22px;color:var(--primary-container,#ff8a00);"></i>
            <span>Your Cart</span>
          </div>
          <button class="cart-close-btn" id="closeCartBtn" title="Close Cart">✕</button>
        </div>
        <div class="cart-items-list" id="cartItemsList"></div>
        <div class="cart-drawer-footer">
          <div class="cart-subtotal-row">
            <span class="cart-subtotal-label">Subtotal:</span>
            <span class="cart-subtotal-price" id="cartSubtotal">₹0</span>
          </div>
          <button class="cart-checkout-btn" id="cartCheckoutBtn">
            Checkout Now <i data-lucide="arrow-right" style="width:16px;height:16px;"></i>
          </button>
        </div>
      `;
      document.body.appendChild(drawer);
    }

    // Toast Container
    if (!document.getElementById('toastContainer')) {
      const tc = document.createElement('div');
      tc.className = 'toast-container';
      tc.id = 'toastContainer';
      document.body.appendChild(tc);
    }

    // Upsell Modal (injected once)
    if (!document.getElementById('upsellModal')) {
      injectUpsellModal();
    }

    // Bind Events
    const closeBtn  = document.getElementById('closeCartBtn');
    const overlay   = document.getElementById('cartOverlay');
    if (closeBtn) closeBtn.addEventListener('click', closeCart);
    if (overlay)  overlay.addEventListener('click', closeCart);

    const checkoutBtn = document.getElementById('cartCheckoutBtn');
    if (checkoutBtn) checkoutBtn.addEventListener('click', handleCartCheckout);

    document.querySelectorAll('.cart-toggle-trigger').forEach(el => {
      el.addEventListener('click', e => { e.preventDefault(); openCart(); });
    });
  }

  // ─── Upsell Modal HTML + CSS ─────────────────────────────────────────────────
  function injectUpsellModal() {
    // CSS
    const style = document.createElement('style');
    style.textContent = `
      #upsellOverlay {
        display:none; position:fixed; inset:0; z-index:999999;
        background:rgba(0,0,0,0.85); backdrop-filter:blur(8px);
        align-items:center; justify-content:center;
      }
      #upsellOverlay.active { display:flex; }

      .upsell-modal {
        background:linear-gradient(145deg,#0f0a04 0%,#1a0e04 60%,#0a0604 100%);
        border:1.5px solid rgba(255,138,0,0.35);
        border-radius:24px; padding:0; width:90%; max-width:480px;
        box-shadow:0 24px 60px rgba(0,0,0,0.8),0 0 40px rgba(255,138,0,0.12);
        animation:upsellIn 0.45s cubic-bezier(0.175,0.885,0.32,1.275) both;
        overflow:hidden; position:relative;
      }
      @keyframes upsellIn {
        from { opacity:0; transform:scale(0.88) translateY(24px); }
        to   { opacity:1; transform:scale(1) translateY(0); }
      }

      /* Top accent strip */
      .upsell-top-strip {
        background:linear-gradient(90deg,#b34500,#ff8a00,#ffb347,#ff8a00,#b34500);
        background-size:200% 100%; animation:stripAnim 3s linear infinite;
        height:4px; width:100%;
      }
      @keyframes stripAnim { 0%,100%{background-position:0% 50%} 50%{background-position:100% 50%} }

      .upsell-body { padding:28px 28px 24px; }

      .upsell-header-badge {
        display:inline-flex; align-items:center; gap:6px;
        background:rgba(255,59,48,0.15); border:1px solid rgba(255,59,48,0.3);
        color:#ff3b30; border-radius:20px; padding:4px 12px;
        font-size:11px; font-weight:800; letter-spacing:0.5px;
        margin-bottom:14px; text-transform:uppercase;
      }
      .upsell-headline {
        font-family:'Playfair Display',serif;
        font-size:22px; font-weight:700; color:#fff;
        margin-bottom:6px; line-height:1.25;
      }
      .upsell-subline {
        font-size:13px; color:rgba(255,255,255,0.55); margin-bottom:18px;
      }

      .upsell-product-card {
        background:rgba(255,255,255,0.04); border:1px solid rgba(255,138,0,0.2);
        border-radius:16px; padding:16px; display:flex; gap:14px; align-items:flex-start;
        margin-bottom:16px;
      }
      .upsell-prod-img {
        width:72px; height:72px; border-radius:12px; object-fit:cover;
        flex-shrink:0; border:1px solid rgba(255,138,0,0.15);
      }
      .upsell-prod-info { flex:1; }
      .upsell-prod-name {
        font-size:15px; font-weight:700; color:#fff; margin-bottom:4px; line-height:1.3;
      }
      .upsell-prod-desc { font-size:12px; color:rgba(255,255,255,0.5); margin-bottom:10px; }
      .upsell-bullets { list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:5px; }
      .upsell-bullets li {
        font-size:11.5px; color:rgba(255,255,255,0.6);
        display:flex; align-items:center; gap:6px;
      }
      .upsell-bullets li::before { content:"✓"; color:#27c93f; font-weight:800; flex-shrink:0; }

      .upsell-price-row {
        display:flex; align-items:center; gap:10px; margin:14px 0 16px;
        padding:12px 16px; background:rgba(255,138,0,0.08);
        border:1px solid rgba(255,138,0,0.18); border-radius:12px;
      }
      .upsell-badge-off {
        background:linear-gradient(135deg,#ff3b30,#ff6b35);
        color:#fff; font-size:12px; font-weight:800;
        padding:4px 10px; border-radius:8px; flex-shrink:0;
      }
      .upsell-price-orig { font-size:14px; color:rgba(255,255,255,0.35); text-decoration:line-through; }
      .upsell-price-now  { font-size:28px; font-weight:800; color:#ff8a00; line-height:1; }
      .upsell-price-save { font-size:11px; color:#27c93f; font-weight:700; margin-left:auto; }

      .upsell-btn-yes {
        display:block; width:100%;
        background:linear-gradient(135deg,#ff8a00,#ffb347); color:#000;
        font-weight:800; font-size:15px; padding:16px;
        border-radius:14px; border:none; cursor:pointer;
        letter-spacing:0.3px; margin-bottom:10px;
        box-shadow:0 6px 24px rgba(255,138,0,0.4);
        transition:all 0.3s ease; font-family:'Inter',sans-serif;
      }
      .upsell-btn-yes:hover { transform:translateY(-2px); box-shadow:0 10px 32px rgba(255,138,0,0.55); }

      .upsell-btn-no {
        display:block; width:100%; background:none; border:none;
        color:rgba(255,255,255,0.35); font-size:12.5px;
        cursor:pointer; padding:6px; text-align:center;
        font-family:'Inter',sans-serif; transition:color 0.2s;
      }
      .upsell-btn-no:hover { color:rgba(255,255,255,0.6); text-decoration:underline; }

      .upsell-trust-note {
        text-align:center; font-size:11px; color:rgba(255,255,255,0.25);
        margin-top:10px;
      }
    `;
    document.head.appendChild(style);

    // Modal HTML
    const modalOverlay = document.createElement('div');
    modalOverlay.id = 'upsellOverlay';
    modalOverlay.innerHTML = `
      <div class="upsell-modal" id="upsellModalBox">
        <div class="upsell-top-strip"></div>
        <div class="upsell-body">
          <div class="upsell-header-badge" id="upsellBadge">⚡ EXCLUSIVE OFFER</div>
          <div class="upsell-headline" id="upsellHeadline">Wait! Add one more & save 30%</div>
          <div class="upsell-subline" id="upsellSubline">You're already getting a great deal. Grab this add-on at a special checkout discount:</div>

          <div class="upsell-product-card">
            <img class="upsell-prod-img" id="upsellProdImg" src="" alt="Product">
            <div class="upsell-prod-info">
              <div class="upsell-prod-name" id="upsellProdName">Loading...</div>
              <div class="upsell-prod-desc" id="upsellProdDesc"></div>
              <ul class="upsell-bullets" id="upsellBullets"></ul>
            </div>
          </div>

          <div class="upsell-price-row">
            <span class="upsell-badge-off" id="upsellOffBadge">30% OFF</span>
            <span class="upsell-price-orig" id="upsellPriceOrig">₹99</span>
            <span class="upsell-price-now" id="upsellPriceNow">₹69</span>
            <span class="upsell-price-save" id="upsellPriceSave">Save ₹30!</span>
          </div>

          <button class="upsell-btn-yes" id="upsellBtnYes">
            ✅ Yes! Add to Cart & Checkout →
          </button>
          <button class="upsell-btn-no" id="upsellBtnNo">
            No thanks, I don't want this deal
          </button>
          <div class="upsell-trust-note">🔒 Secure Payment · ⚡ Instant Access · One-time payment</div>
        </div>
      </div>
    `;
    document.body.appendChild(modalOverlay);
  }

  // Show the upsell modal with the right product
  function showUpsellModal(product, onAccept, onDecline) {
    const disc = Math.round(product.price * (1 - DISCOUNT_PCT / 100));
    const saved = product.price - disc;

    // Populate
    document.getElementById('upsellProdImg').src  = product.img;
    document.getElementById('upsellProdName').textContent = product.name;
    document.getElementById('upsellProdDesc').textContent = product.desc;
    document.getElementById('upsellBullets').innerHTML = product.bullets
      .map(b => `<li>${b}</li>`).join('');
    document.getElementById('upsellPriceOrig').textContent = `₹${product.price}`;
    document.getElementById('upsellPriceNow').textContent  = `₹${disc}`;
    document.getElementById('upsellPriceSave').textContent = `Save ₹${saved}!`;

    const cart = getCart();
    if (cart.length >= 2) {
      document.getElementById('upsellBadge').textContent    = '🎁 BUNDLE BONUS';
      document.getElementById('upsellHeadline').textContent = 'You\'re buying ' + cart.length + ' products — here\'s a bonus deal!';
      document.getElementById('upsellSubline').textContent  = 'Complete your bundle with this add-on at 30% off — only at checkout:';
    } else {
      document.getElementById('upsellBadge').textContent    = '⚡ ONE-TIME OFFER';
      document.getElementById('upsellHeadline').textContent = 'Hold on! Add this at 30% off';
      document.getElementById('upsellSubline').textContent  = 'Customers who buy this also grab this bestseller — available at checkout price only:';
    }

    document.getElementById('upsellOverlay').classList.add('active');

    // Button handlers (replace old ones)
    const btnYes = document.getElementById('upsellBtnYes');
    const btnNo  = document.getElementById('upsellBtnNo');
    const newYes = btnYes.cloneNode(true);
    const newNo  = btnNo.cloneNode(true);
    btnYes.parentNode.replaceChild(newYes, btnYes);
    btnNo.parentNode.replaceChild(newNo, btnNo);

    newYes.addEventListener('click', () => {
      document.getElementById('upsellOverlay').classList.remove('active');
      onAccept(product, disc);
    });
    newNo.addEventListener('click', () => {
      document.getElementById('upsellOverlay').classList.remove('active');
      onDecline();
    });
  }

  // ─── Cart Actions ─────────────────────────────────────────────────────────────
  window.addToCart = function (id, name, price, img, link) {
    const cart = getCart();
    if (cart.find(item => item.id === id)) {
      showToast(`"${name}" is already in your cart!`, 'info');
      // openCart(); (disabled automatic drawer)
      return;
    }
    cart.push({ id, name, price, img, link });
    saveCart(cart);
    updateCartUI();
    showToast(`Added "${name}" to cart!`, 'success');
    // setTimeout(openCart, 500); (disabled automatic drawer)
  };

  window.removeFromCart = function (id) {
    let cart = getCart();
    const item = cart.find(i => i.id === id);
    cart = cart.filter(i => i.id !== id);
    saveCart(cart);
    updateCartUI();
    if (item) showToast(`Removed "${item.name}" from cart`, 'info');
  };

  window.clearCart = function () {
    saveCart([]);
    updateCartUI();
    showToast('Cart cleared', 'info');
  };

  // ─── Drawer Control ───────────────────────────────────────────────────────────
  window.openCart = function () {
    const drawer  = document.getElementById('cartDrawer');
    const overlay = document.getElementById('cartOverlay');
    if (drawer && overlay) {
      drawer.classList.add('open');
      overlay.classList.add('show');
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeCart = function () {
    const drawer  = document.getElementById('cartDrawer');
    const overlay = document.getElementById('cartOverlay');
    if (drawer && overlay) {
      drawer.classList.remove('open');
      overlay.classList.remove('show');
      document.body.style.overflow = '';
    }
  };

  // ─── UI Rendering ─────────────────────────────────────────────────────────────
  window.updateCartUI = function () {
    const cart = getCart();

    // Badges
    document.querySelectorAll('.cart-badge').forEach(badge => {
      badge.textContent = cart.length;
      badge.classList.toggle('active', cart.length > 0);
    });

    const listEl = document.getElementById('cartItemsList');
    if (!listEl) return;

    if (cart.length === 0) {
      listEl.innerHTML = `
        <div class="cart-empty-state">
          <i data-lucide="shopping-bag" style="width:48px;height:48px;stroke-width:1.5;"></i>
          <div class="cart-empty-title">Your Cart is Empty</div>
          <div class="cart-empty-desc">Explore our premium digital product collection and add items to get started.</div>
        </div>`;
      const btn = document.getElementById('cartCheckoutBtn');
      if (btn) btn.style.opacity = '0.5';
    } else {
      listEl.innerHTML = cart.map(item => `
        <div class="cart-item">
          <div class="cart-item-details">
            <div class="cart-item-title">${item.name}</div>
            <div class="cart-item-price">₹${item.price}</div>
          </div>
          <button class="cart-item-remove" onclick="removeFromCart('${item.id}')" title="Remove">✕</button>
        </div>`).join('');
      const btn = document.getElementById('cartCheckoutBtn');
      if (btn) btn.style.opacity = '1';
    }

    const subtotal = cart.reduce((s, i) => s + i.price, 0);
    const el = document.getElementById('cartSubtotal');
    if (el) el.textContent = `₹${subtotal}`;

    if (window.lucide) lucide.createIcons();

    // Notify product page to refresh Add button states
    window.dispatchEvent(new Event('cartUpdated'));
  };

  // ─── Toast System ─────────────────────────────────────────────────────────────
  window.showToast = function (message, type = 'success') {
    const container = document.getElementById('toastContainer');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = 'toast';
    let icon = 'check-circle';
    if (type === 'info')  icon = 'info';
    if (type === 'error') icon = 'alert-triangle';
    toast.innerHTML = `<i data-lucide="${icon}" style="width:16px;height:16px;"></i><span>${message}</span>`;
    container.appendChild(toast);
    if (window.lucide) lucide.createIcons();
    setTimeout(() => toast.classList.add('show'), 10);
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 400);
    }, 3500);
  };

  function doCheckout() {
    const cart = getCart();
    const amount = cart.reduce((s, i) => s + i.price, 0);
    const productNames = cart.map(i => i.name).join(', ');
    try {
      sessionStorage.setItem('ae_pg_product_name', productNames);
      sessionStorage.setItem('ae_pg_amount', amount);
    } catch (e) {}
    // Redirect absolutely to the main domain checkout page with the cart content serialized in the URL
    window.location.href = `https://anshumanenterprises.online/futurewithai/checkout.html?cart=${encodeURIComponent(JSON.stringify(cart))}`;
  }

  function handleCartCheckout() {
    const cart = getCart();
    if (cart.length === 0) {
      showToast('Add at least one product to check out!', 'error');
      return;
    }
    
    // Upselling Trick: Intercept with checkout upsell modal if eligible
    const upsellProd = getUpsellProduct(cart);
    if (upsellProd) {
      showUpsellModal(
        upsellProd,
        (product, discountedPrice) => {
          // Accept: add discounted upsell product to cart and checkout
          const currentCart = getCart();
          currentCart.push({
            id: product.id,
            name: `${product.name} (30% Checkout Offer)`,
            price: discountedPrice,
            img: product.img,
            link: product.link
          });
          saveCart(currentCart);
          doCheckout();
        },
        () => {
          // Decline: proceed directly to checkout
          doCheckout();
        }
      );
    } else {
      doCheckout();
    }
  }

  // Direct Buy Now function
  window.buyNow = function (id, name, price, img, link) {
    const cart = getCart();
    if (!cart.find(item => item.id === id)) {
      cart.push({ id, name, price, img, link });
      saveCart(cart);
      updateCartUI();
    }
    handleCartCheckout();
  };

  // Continuous Social Proof Purchase Toast Simulation
  window.startGlobalPurchaseSimulation = function () {
    const toast = document.getElementById('purchase-toast');
    if (!toast) return;

    const buyers = [
      { name: 'Rahul Sharma', city: 'Delhi' },
      { name: 'Aniket Patel', city: 'Ahmedabad' },
      { name: 'Vikram Rao', city: 'Bengaluru' },
      { name: 'Priya Sen', city: 'Kolkata' },
      { name: 'Sanjay Deshmukh', city: 'Mumbai' },
      { name: 'Amit Tiwari', city: 'Indore' },
      { name: 'Jayesh Dave', city: 'Pune' },
      { name: 'Sneha Reddy', city: 'Hyderabad' },
      { name: 'Kunal Kapoor', city: 'Chandigarh' },
      { name: 'Meera Nair', city: 'Kochi' },
      { name: 'Rohan Verma', city: 'Lucknow' },
      { name: 'Divya Joshi', city: 'Jaipur' },
      { name: 'Suresh Kumar', city: 'Chennai' },
      { name: 'Aditya Gupta', city: 'Noida' },
      { name: 'Neha Sharma', city: 'Gurugram' },
      { name: 'Arjun Mehta', city: 'Surat' },
      { name: 'Ritu Kapoor', city: 'Bhopal' }
    ];

    // Catalog bestsellers list for cross-selling
    const catalogProducts = [
      { name: 'n8n Automation Pack (2000+ Workflows)', price: 99, link: 'n8n-pack.html' },
      { name: '100,000+ Viral Reels Goldmine Pack', price: 99, link: 'mega-reels.html' },
      { name: 'Ultimate Video Editing Toolkit (500GB)', price: 199, link: 'video-editing.html' },
      { name: '1500+ Manually Tested Web Apps Pack', price: 199, link: 'web-apps.html' },
      { name: 'Full Digital Marketing Resource Bundle', price: 499, link: 'digital-marketing-bundle.html' },
      { name: '2700+ Elementor Pro Templates', price: 59, link: 'product-2700-elementor-pro-templates-forwordpresssite.html' },
      { name: '1.37tb All Money Making Courses Bundle', price: 29, link: 'product-37tb-all-money-making-courses-bundle.html' },
      { name: '700+ AI English Reels Bundle', price: 29, link: 'product-700-ai-english-reelsshort.html' },
      { name: '1500+ Glowing Motion Graphics Reels', price: 39, link: 'product-1500-glowing-motion-graphics-reels-bundle.html' }
    ];

    const avatar = document.getElementById('purchase-toast-avatar') || document.getElementById('toast-avatar');
    const buyerName = document.getElementById('purchase-toast-name') || document.getElementById('toast-buyer-name');
    const prodName = document.getElementById('purchase-toast-prod') || document.getElementById('toast-prod-name') || document.getElementById('toast-product-name');
    const timeEl = document.getElementById('purchase-toast-time') || document.getElementById('toast-time');

    let currentIdx = 0;

    // Detect if we are on a specific product detail page to highlight that product
    const heroTitleEl = document.querySelector('h1');
    const currentPageProduct = heroTitleEl ? heroTitleEl.textContent.trim() : '';

    function showNextToast() {
      const b = buyers[currentIdx];
      let selectedProduct;

      // 60% chance to show the current page product if available, otherwise random catalog cross-sell
      if (currentPageProduct && Math.random() < 0.6) {
        selectedProduct = { name: currentPageProduct, price: 99, link: window.location.pathname };
        // Attempt to find exact price if shown on page
        const priceEl = document.querySelector('.price-now, .prod-price, .pay-today-price');
        if (priceEl) {
          const matchedPrice = priceEl.textContent.match(/\d+/);
          if (matchedPrice) selectedProduct.price = parseInt(matchedPrice[0], 10);
        }
      } else {
        selectedProduct = catalogProducts[Math.floor(Math.random() * catalogProducts.length)];
      }

      // Upselling Trick: Make simulated toast notifications clickable links to the product pages!
      toast.style.cursor = 'pointer';
      toast.onclick = () => {
        window.location.href = selectedProduct.link;
      };

      if (avatar) {
        const initials = b.name.split(' ').map(n => n[0]).join('');
        avatar.textContent = initials || b.name.charAt(0);
      }
      if (buyerName) {
        buyerName.textContent = `${b.name} (${b.city})`;
      }
      if (prodName) {
        prodName.innerHTML = `purchased <strong>${selectedProduct.name}</strong> <span style="color:#ff8a00; font-weight:bold; margin-left:4px;">for ₹${selectedProduct.price}</span>`;
      }
      if (timeEl) {
        timeEl.textContent = ["Just now", "1 min ago", "2 mins ago", "3 mins ago"][Math.floor(Math.random() * 4)];
      }

      toast.classList.add('show');

      // Hide after 5 seconds
      setTimeout(() => {
        toast.classList.remove('show');
        currentIdx = (currentIdx + 1) % buyers.length;
        // Schedule next toast after 8 seconds of silence for a continuous flowing loop
        setTimeout(showNextToast, 8000);
      }, 5000);
    }

    // Start simulation after 4 seconds
    setTimeout(showNextToast, 4000);
  };

  function injectWhatsAppPopup() {
    // Check local storage flags
    if (localStorage.getItem('fwai_wa_popup_dismissed') === 'true' || localStorage.getItem('fwai_wa_popup_joined') === 'true') {
      return;
    }

    // Dynamic Style Injection
    const style = document.createElement('style');
    style.textContent = `
      #waPopupOverlay {
        display: none; position: fixed; inset: 0; z-index: 1000000;
        background: rgba(0, 0, 0, 0.85); backdrop-filter: blur(8px);
        align-items: center; justify-content: center;
      }
      #waPopupOverlay.active { display: flex; }
      .wa-popup-box {
        background: linear-gradient(145deg, #0a0604 0%, #150c06 50%, #050302 100%);
        border: 1.5px solid rgba(37, 211, 102, 0.35);
        border-radius: 24px; padding: 32px 32px 28px; width: 90%; max-width: 440px;
        box-shadow: 0 24px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(37, 211, 102, 0.12);
        animation: waPopupIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) both;
        position: relative; text-align: center; overflow: hidden;
      }
      @keyframes waPopupIn {
        from { opacity: 0; transform: scale(0.88) translateY(30px); }
        to { opacity: 1; transform: scale(1) translateY(0); }
      }
      .wa-top-glow {
        position: absolute; top: -100px; left: 50%; transform: translateX(-50%);
        width: 200px; height: 200px;
        background: radial-gradient(circle, rgba(37, 211, 102, 0.2) 0%, transparent 70%);
        filter: blur(30px); pointer-events: none;
      }
      .wa-icon-container {
        width: 72px; height: 72px; border-radius: 50%;
        background: rgba(37, 211, 102, 0.10); border: 1.5px solid rgba(37, 211, 102, 0.25);
        display: flex; align-items: center; justify-content: center;
        margin: 0 auto 20px; position: relative;
        box-shadow: 0 0 20px rgba(37, 211, 102, 0.1);
        animation: waIconPulse 2s infinite ease-in-out;
      }
      @keyframes waIconPulse {
        0%, 100% { transform: scale(1); box-shadow: 0 0 20px rgba(37, 211, 102, 0.1); }
        50% { transform: scale(1.05); box-shadow: 0 0 30px rgba(37, 211, 102, 0.25); }
      }
      .wa-icon-container svg { width: 38px; height: 38px; fill: #25D366; }
      .wa-popup-title {
        font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 700;
        color: #fff; margin-bottom: 10px; line-height: 1.25;
      }
      .wa-popup-desc {
        font-size: 13.5px; color: rgba(255, 255, 255, 0.6);
        margin-bottom: 20px; line-height: 1.5; padding: 0 10px;
      }
      .wa-benefits-list {
        text-align: left; margin: 0 auto 24px; max-width: 320px;
        display: flex; flex-direction: column; gap: 10px;
      }
      .wa-benefit-item {
        font-size: 12.5px; color: rgba(255, 255, 255, 0.7);
        display: flex; align-items: center; gap: 10px;
      }
      .wa-benefit-item svg {
        color: #25D366; fill: none; flex-shrink: 0; width: 14px; height: 14px;
      }
      .wa-btn-join {
        display: flex; align-items: center; justify-content: center; gap: 8px;
        width: 100%; background: linear-gradient(135deg, #25D366, #1ebd5c);
        color: #fff; font-family: 'Inter', sans-serif; font-weight: 800;
        font-size: 15px; padding: 16px; border-radius: 14px; border: none;
        cursor: pointer; box-shadow: 0 6px 20px rgba(37, 211, 102, 0.35);
        transition: all 0.3s ease; text-decoration: none;
      }
      .wa-btn-join:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 28px rgba(37, 211, 102, 0.5);
        background: linear-gradient(135deg, #20bd5a, #1a9e4d);
      }
      .wa-btn-later {
        display: block; background: none; border: none;
        color: rgba(255, 255, 255, 0.35); font-size: 12.5px;
        font-family: 'Inter', sans-serif; cursor: pointer;
        margin: 16px auto 0; text-align: center; transition: color 0.2s;
        text-decoration: underline;
      }
      .wa-btn-later:hover { color: rgba(255, 255, 255, 0.6); }
      .wa-close-cross {
        position: absolute; top: 16px; right: 16px; background: none;
        border: none; color: rgba(255, 255, 255, 0.25); font-size: 20px;
        cursor: pointer; transition: color 0.2s; padding: 4px; line-height: 1;
      }
      .wa-close-cross:hover { color: #fff; }
    `;
    document.head.appendChild(style);

    // Modal HTML
    const modalOverlay = document.createElement('div');
    modalOverlay.id = 'waPopupOverlay';
    modalOverlay.innerHTML = `
      <div class="wa-popup-box">
        <div class="wa-top-glow"></div>
        <button class="wa-close-cross" id="waCloseCrossBtn">✕</button>
        <div class="wa-icon-container">
          <svg viewBox="0 0 24 24">
            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L0 24l6.335-1.662c1.746.953 3.71 1.458 5.709 1.459h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
          </svg>
        </div>
        <div class="wa-popup-title">Join Our Community! 🚀</div>
        <div class="wa-popup-desc">Get weekly premium digital bonuses, exclusive discount offers, and 24/7 direct support.</div>
        
        <div class="wa-benefits-list">
          <div class="wa-benefit-item">
            <svg viewBox="0 0 24 24" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>🎁 Exclusive Weekly Free Assets Vault</span>
          </div>
          <div class="wa-benefit-item">
            <svg viewBox="0 0 24 24" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>⚡ Fresh n8n Workflows & AI Prompt Sheets</span>
          </div>
          <div class="wa-benefit-item">
            <svg viewBox="0 0 24 24" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>💬 Live Chat & 1-on-1 Admin Support</span>
          </div>
        </div>

        <button class="wa-btn-join" id="waJoinBtn">
          🟢 Join WhatsApp Community
        </button>
        <button class="wa-btn-later" id="waLaterBtn">
          Maybe Later
        </button>
      </div>
    `;
    document.body.appendChild(modalOverlay);

    const closeOverlay = () => {
      modalOverlay.classList.remove('active');
      setTimeout(() => modalOverlay.remove(), 500);
    };

    const handleDismiss = () => {
      localStorage.setItem('fwai_wa_popup_dismissed', 'true');
      closeOverlay();
    };

    const handleJoin = () => {
      localStorage.setItem('fwai_wa_popup_joined', 'true');
      window.open('https://chat.whatsapp.com/L7M5r6mMdoKEh3cvM5F1xr', '_blank');
      closeOverlay();
    };

    document.getElementById('waCloseCrossBtn').addEventListener('click', handleDismiss);
    document.getElementById('waLaterBtn').addEventListener('click', handleDismiss);
    document.getElementById('waJoinBtn').addEventListener('click', handleJoin);
    
    // Also close on background click
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) {
        handleDismiss();
      }
    });

    // Fade in
    setTimeout(() => {
      modalOverlay.classList.add('active');
    }, 10);
  }

  // ─── Initialization ───────────────────────────────────────────────────────────
  window.addEventListener('DOMContentLoaded', () => {
    injectCartUI();
    updateCartUI();
    // Start global purchase simulation automatically if the toast container is present
    setTimeout(window.startGlobalPurchaseSimulation, 1000);

    // Show WhatsApp Community Popup after 3 seconds
    setTimeout(injectWhatsAppPopup, 3000);

    // Make all product cards (.prod-card and .suggest-card) globally clickable to view details
    document.body.addEventListener('click', (e) => {
      const card = e.target.closest('.prod-card, .suggest-card');
      if (!card) return;

      // Ignore clicks on buttons, links, dropdowns, input elements, or items inside them
      if (e.target.closest('a, button, select, input')) {
        return;
      }

      // Find the details/redirect anchor tag link in this card
      const link = card.querySelector('a');
      if (link && link.href) {
        window.location.href = link.href;
      }
    });
  });
})();
