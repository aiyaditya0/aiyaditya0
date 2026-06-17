"""
FutureWithAi - Apps Script Delivery Test
Run this to simulate a real payment order and verify email delivery.
"""
import urllib.request
import urllib.parse
import json
import time
import sys

# Force UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzLJxvjXfqXF10N1YIju5pihlp3OgjjJtGl9bqNr2uHvn94cKodeS2U0kB0yNTieFuV/exec"

def test_post_order(email, product_id="mega-reels"):
    """Send a mock payment POST to the Apps Script and verify the response."""
    payload = {
        "email": email,
        "name": "Test User",
        "products": product_id,
        "orderId": "TEST-" + str(int(time.time())),
        "amount": 99,
        "status": "COMPLETED"
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        APPS_SCRIPT_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    print(f"\n[SEND] Sending test order to Apps Script...")
    print(f"   Email: {email}")
    print(f"   Product: {product_id}")
    print(f"   OrderId: {payload['orderId']}")
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            response_text = resp.read().decode("utf-8")
            result = json.loads(response_text)
            
            print(f"\n[OK] Response received!")
            print(f"   Success: {result.get('success')}")
            print(f"   Message: {result.get('message', 'N/A')}")
            print(f"   Access Token: {result.get('accessToken', 'N/A')}")
            
            if result.get('productLinks'):
                print(f"\n[LINKS] Product Links returned:")
                for pid, link_data in result['productLinks'].items():
                    print(f"   - {link_data.get('name', pid)}: {link_data.get('link', 'N/A')}")
            
            if result.get('error'):
                print(f"\n[ERROR] Error from server: {result['error']}")
            
            return result
    except Exception as e:
        print(f"\n[FAIL] Request failed: {e}")
        return None

def test_get_status(order_id):
    """Test the check_status GET endpoint."""
    url = f"{APPS_SCRIPT_URL}?action=check_status&orderId={urllib.parse.quote(order_id)}"
    print(f"\n[CHECK] Checking order status for: {order_id}")
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            print(f"   State: {result.get('state', 'N/A')}")
            print(f"   isPaid: {result.get('isPaid', False)}")
            print(f"   Token: {result.get('accessToken', 'N/A')}")
            return result
    except Exception as e:
        print(f"[FAIL] Status check failed: {e}")
        return None

if __name__ == "__main__":
    print("=" * 55)
    print("  FutureWithAi -- Apps Script Delivery Test")
    print("=" * 55)
    
    # Change email to your test email
    TEST_EMAIL = "adityat32145@gmail.com"
    TEST_PRODUCT = "mega-reels"
    
    result = test_post_order(TEST_EMAIL, TEST_PRODUCT)
    
    if result and result.get("success"):
        print("\n[PASS] Test PASSED! Email should be delivered to:", TEST_EMAIL)
        # Also test status check
        order_id = "TEST-" + str(int(time.time()) - 2)
        test_get_status(order_id)
    else:
        print("\n[WARN] Test had issues. Check the response above.")
    
    print("\n" + "=" * 55)
