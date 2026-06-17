/**
 * FutureWithAi - Global Shopping Cart System
 * Persistent Client-side Cart via LocalStorage
 */

(function () {
  // --- Cart State Management ---
  const STORAGE_KEY = 'fwai_cart_items';
  
  function getCart() {
    try {
      const items = localStorage.getItem(STORAGE_KEY);
      return items ? JSON.parse(items) : [];
    } catch (e) {
      console.error('Error reading cart from localStorage', e);
      return [];
    }
  }

  function saveCart(cart) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(cart));
    } catch (e) {
      console.error('Error saving cart to localStorage', e);
    }
  }

  // --- Dynamic Cart UI Injection ---
  function injectCartUI() {
    // Inject Drawer HTML if not present
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
            <i data-lucide="shopping-cart" style="width: 22px; height: 22px; color: var(--primary-container);"></i>
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
            Checkout Now <i data-lucide="arrow-right" style="width: 16px; height: 16px;"></i>
          </button>
        </div>
      `;
      document.body.appendChild(drawer);
    }

    // Inject Toast Container if not present
    if (!document.getElementById('toastContainer')) {
      const toastContainer = document.createElement('div');
      toastContainer.className = 'toast-container';
      toastContainer.id = 'toastContainer';
      document.body.appendChild(toastContainer);
    }

    // Bind Drawer Close Events
    const closeBtn = document.getElementById('closeCartBtn');
    const overlay = document.getElementById('cartOverlay');
    if (closeBtn) closeBtn.addEventListener('click', closeCart);
    if (overlay) overlay.addEventListener('click', closeCart);

    // Bind Checkout Event
    const checkoutBtn = document.getElementById('cartCheckoutBtn');
    if (checkoutBtn) {
      checkoutBtn.addEventListener('click', handleCartCheckout);
    }

    // Listen for global toggle clicks
    document.querySelectorAll('.cart-toggle-trigger').forEach(el => {
      el.addEventListener('click', (e) => {
        e.preventDefault();
        openCart();
      });
    });
  }

  // --- Cart Actions ---
  window.addToCart = function (id, name, price, img, link) {
    const cart = getCart();
    const existing = cart.find(item => item.id === id);

    if (existing) {
      showToast(`"${name}" is already in your cart!`, 'info');
      openCart();
      return;
    }

    cart.push({ id, name, price, img, link });
    saveCart(cart);
    
    // Update visuals
    updateCartUI();
    showToast(`Added "${name}" to cart!`, 'success');
    
    // Auto open cart drawer to guide user
    setTimeout(openCart, 500);
  };

  window.removeFromCart = function (id) {
    let cart = getCart();
    const item = cart.find(item => item.id === id);
    cart = cart.filter(item => item.id !== id);
    saveCart(cart);
    updateCartUI();
    if (item) {
      showToast(`Removed "${item.name}" from cart`, 'info');
    }
  };

  window.clearCart = function () {
    saveCart([]);
    updateCartUI();
    showToast('Cart cleared', 'info');
  };

  // --- Drawer Control ---
  window.openCart = function () {
    const drawer = document.getElementById('cartDrawer');
    const overlay = document.getElementById('cartOverlay');
    if (drawer && overlay) {
      drawer.classList.add('open');
      overlay.classList.add('show');
      document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }
  };

  window.closeCart = function () {
    const drawer = document.getElementById('cartDrawer');
    const overlay = document.getElementById('cartOverlay');
    if (drawer && overlay) {
      drawer.classList.remove('open');
      overlay.classList.remove('show');
      document.body.style.overflow = '';
    }
  };

  // --- UI Rendering ---
  window.updateCartUI = function () {
    const cart = getCart();
    
    // 1. Update Navigation Badges
    const badges = document.querySelectorAll('.cart-badge');
    badges.forEach(badge => {
      badge.textContent = cart.length;
      if (cart.length > 0) {
        badge.classList.add('active');
      } else {
        badge.classList.remove('active');
      }
    });

    // 2. Render Drawer List
    const listEl = document.getElementById('cartItemsList');
    if (!listEl) return;

    if (cart.length === 0) {
      listEl.innerHTML = `
        <div class="cart-empty-state">
          <i data-lucide="shopping-bag" style="width: 48px; height: 48px; stroke-width: 1.5;"></i>
          <div class="cart-empty-title">Your Cart is Empty</div>
          <div class="cart-empty-desc">Explore our premium digital product collection and add templates to get started.</div>
        </div>
      `;
      const checkoutBtn = document.getElementById('cartCheckoutBtn');
      if (checkoutBtn) checkoutBtn.style.opacity = '0.5';
    } else {
      listEl.innerHTML = cart.map(item => `
        <div class="cart-item">
          <img class="cart-item-img" src="${item.img}" alt="${item.name}">
          <div class="cart-item-details">
            <div class="cart-item-title">${item.name}</div>
            <div class="cart-item-price">₹${item.price}</div>
          </div>
          <button class="cart-item-remove" onclick="removeFromCart('${item.id}')" title="Remove Item">✕</button>
        </div>
      `).join('');
      
      const checkoutBtn = document.getElementById('cartCheckoutBtn');
      if (checkoutBtn) checkoutBtn.style.opacity = '1';
    }

    // 3. Update Subtotal
    const subtotal = cart.reduce((sum, item) => sum + item.price, 0);
    const subtotalEl = document.getElementById('cartSubtotal');
    if (subtotalEl) {
      subtotalEl.textContent = `₹${subtotal}`;
    }

    // 4. Update Lucide Icons
    if (window.lucide) {
      lucide.createIcons();
    }
  };

  // --- Toast System ---
  window.showToast = function (message, type = 'success') {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = 'toast';
    
    let icon = 'check-circle';
    if (type === 'info') icon = 'info';
    if (type === 'error') icon = 'alert-triangle';

    toast.innerHTML = `
      <i data-lucide="${icon}" style="width: 16px; height: 16px;"></i>
      <span>${message}</span>
    `;

    container.appendChild(toast);
    if (window.lucide) lucide.createIcons();

    // Trigger slide-in
    setTimeout(() => toast.classList.add('show'), 10);

    // Remove after 3.5s
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 400);
    }, 3500);
  };

  // --- Checkout Processing ---
  function handleCartCheckout() {
    const cart = getCart();
    if (cart.length === 0) {
      showToast('Add at least one product to check out!', 'error');
      return;
    }

    const amount = cart.reduce((sum, item) => sum + item.price, 0);
    const productNames = cart.map(item => item.name).join(', ');
    
    // Store in SessionStorage for payment-success page reference
    try {
      sessionStorage.setItem('ae_pg_product_name', productNames);
      sessionStorage.setItem('ae_pg_amount', amount);
    } catch (e) {}

    // Redirect to checkout.html with queries
    const checkoutUrl = `checkout.html?amount=${amount}&products=${encodeURIComponent(productNames)}`;
    window.location.href = checkoutUrl;
  }

  // --- Initialization ---
  window.addEventListener('DOMContentLoaded', () => {
    injectCartUI();
    updateCartUI();
  });
})();
