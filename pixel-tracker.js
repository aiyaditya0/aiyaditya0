(function() {
  const PIXEL_ID = '2550902175328844'; // Replace with actual Meta Pixel ID

  // Check if we are in development environment
  const isDev = window.location.hostname === 'localhost' || 
                window.location.hostname === '127.0.0.1' || 
                window.location.hostname.includes('192.168.') ||
                window.location.search.includes('debug=true');

  function logDebug(eventName, details) {
    if (isDev) {
      console.log(`%c[Meta Pixel Debug] Event: ${eventName}`, 'color: #ff8a00; font-weight: bold;', details || '');
    }
  }

  // Meta Pixel Base Code Integration
  if (!window.fbq) {
    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    
    fbq('init', PIXEL_ID);
    logDebug('init', PIXEL_ID);
  }

  // Capture test_event_code from URL and persist in sessionStorage (defaulting to TEST71779)
  let testCode = 'TEST71779';
  try {
    const params = new URLSearchParams(window.location.search);
    const urlTestCode = params.get('test_event_code');
    if (urlTestCode) {
      testCode = urlTestCode;
      sessionStorage.setItem('fb_test_event_code', urlTestCode);
    } else {
      const cached = sessionStorage.getItem('fb_test_event_code');
      if (cached) {
        testCode = cached;
      } else {
        sessionStorage.setItem('fb_test_event_code', testCode);
      }
    }
  } catch (e) {}

  // Central tracking function that automatically attaches test_event_code
  function trackEvent(eventName, eventParams) {
    if (window.fbq) {
      const options = {};
      if (testCode) {
        options.test_event_code = testCode;
      }
      fbq('track', eventName, eventParams || {}, options);
      logDebug(eventName, { params: eventParams, options: options });
    }
  }

  // Track PageView on all pages
  trackEvent('PageView');

  // Helper to get current dynamic price
  function getCurrentPrice(defaultVal) {
    // 1. Try to read current price from DOM element (index.html or checkout.html)
    const el = document.getElementById('pricing-current-amount') || document.getElementById('co-price-val');
    if (el) {
      const match = el.textContent.match(/\d+/);
      if (match) {
        return parseInt(match[0], 10);
      }
    }
    
    // 2. Try parsing URL params (checkout.html?amount=300)
    try {
      const params = new URLSearchParams(window.location.search);
      const amount = parseInt(params.get('amount'), 10);
      if (!isNaN(amount) && amount > 0) {
        return amount;
      }
    } catch (e) {}

    // 3. Dynamic default price based on launch offer date
    const OFFER_END = new Date('2026-06-17T03:16:00Z').getTime();
    if (Date.now() < OFFER_END) {
      return 349;
    }
    return 399;
  }

  // Page-specific tracking
  const path = window.location.pathname;
  
  const isLandingPage = path === '/' || 
                        path.endsWith('/index.html') || 
                        path.endsWith('/') || 
                        path.endsWith('/futurewithai') || 
                        path.endsWith('/futurewithai/index.html');
  
  if (isLandingPage) {
    const landingPrice = getCurrentPrice(349);
    trackEvent('ViewContent', {
      value: landingPrice,
      currency: 'INR'
    });

    // Track clicks on CTAs leading to checkout
    const attachCtaListeners = () => {
      document.querySelectorAll('a[href*="checkout.html"]').forEach(btn => {
        if (btn.dataset.fbTracked) return;
        btn.dataset.fbTracked = 'true';
        btn.addEventListener('click', () => {
          const href = btn.getAttribute('href') || '';
          let clickPrice = landingPrice;
          if (href.includes('amount=300')) {
            clickPrice = 300;
          }
          trackEvent('InitiateCheckout', {
            value: clickPrice,
            currency: 'INR'
          });
        });
      });
    };

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', attachCtaListeners);
    } else {
      attachCtaListeners();
    }
  }

  // Checkout Page tracking
  if (path.endsWith('/checkout.html')) {
    // 1. InitiateCheckout (Track on Page Load)
    const trackInitCheckout = () => {
      const coPrice = getCurrentPrice(349);
      trackEvent('InitiateCheckout', {
        value: coPrice,
        currency: 'INR'
      });
    };

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', trackInitCheckout);
    } else {
      trackInitCheckout();
    }

    // 2. AddPaymentInfo (Track on Form Submit)
    const attachFormListener = () => {
      const checkoutForm = document.getElementById('checkout-form');
      if (checkoutForm && !checkoutForm.dataset.fbTracked) {
        checkoutForm.dataset.fbTracked = 'true';
        checkoutForm.addEventListener('submit', () => {
          const coPrice = getCurrentPrice(349);
          trackEvent('AddPaymentInfo', {
            value: coPrice,
            currency: 'INR'
          });
        });
      }
    };

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', attachFormListener);
    } else {
      attachFormListener();
    }
  }
})();
