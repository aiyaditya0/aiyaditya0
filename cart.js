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
      img: 'hero-image.png',
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
      img: 'reels_hero_mockup.png',
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
      openCart();
      return;
    }
    cart.push({ id, name, price, img, link });
    saveCart(cart);
    updateCartUI();
    showToast(`Added "${name}" to cart!`, 'success');
    setTimeout(openCart, 500);
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
          <img class="cart-item-img" src="${item.img}" alt="${item.name}">
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

  // ─── Checkout + Smart Upsell ──────────────────────────────────────────────────
  function doCheckout() {
    const cart = getCart();
    const amount = cart.reduce((s, i) => s + i.price, 0);
    const productNames = cart.map(i => i.name).join(', ');
    try {
      sessionStorage.setItem('ae_pg_product_name', productNames);
      sessionStorage.setItem('ae_pg_amount', amount);
    } catch (e) {}
    window.location.href = `checkout.html?amount=${amount}&products=${encodeURIComponent(productNames)}`;
  }

  function handleCartCheckout() {
    const cart = getCart();
    if (cart.length === 0) {
      showToast('Add at least one product to check out!', 'error');
      return;
    }

    const upsell = getUpsellProduct(cart);

    if (!upsell) {
      // No eligible upsell — go straight to checkout
      doCheckout();
      return;
    }

    // Close cart drawer, show upsell modal
    closeCart();
    showUpsellModal(
      upsell,
      // ✅ Accept: add upsell product at discounted price, then checkout
      function onAccept(product, discountedPrice) {
        const cart = getCart();
        if (!cart.find(i => i.id === product.id)) {
          cart.push({
            id: product.id,
            name: product.fullName,
            price: discountedPrice,
            img: product.img,
            link: product.link,
          });
          saveCart(cart);
          updateCartUI();
          showToast(`Added "${product.name}" at ₹${discountedPrice}! 🎉`, 'success');
        }
        setTimeout(doCheckout, 600);
      },
      // ❌ Decline: go to checkout as-is
      function onDecline() {
        doCheckout();
      }
    );
  }

  // ─── Initialization ───────────────────────────────────────────────────────────
  window.addEventListener('DOMContentLoaded', () => {
    injectCartUI();
    updateCartUI();
  });
})();
