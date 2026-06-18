import urllib.request
import urllib.parse
import json
import sys

# Force UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzLJxvjXfqXF10N1YIju5pihlp3OgjjJtGl9bqNr2uHvn94cKodeS2U0kB0yNTieFuV/exec"
REAL_ORDER_ID = "AEN8N-MQIXXKDF-4813D0B1"

def test_real_order():
    url = f"{APPS_SCRIPT_URL}?action=check_status&orderId={urllib.parse.quote(REAL_ORDER_ID)}"
    print(f"Checking status of real order: {REAL_ORDER_ID}")
    print(f"URL: {url}\n")
    
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            response_text = resp.read().decode("utf-8")
            result = json.loads(response_text)
            print("Response from Google Apps Script:")
            print(json.dumps(result, indent=2))
            
            if result.get("isPaid"):
                print("\n[SUCCESS] Payment verified! Access token and product links generated successfully.")
            else:
                print("\n[PENDING/FAILED] Order is not paid or failed. State:", result.get("state"))
    except Exception as e:
        print(f"Error checking status: {e}")

if __name__ == "__main__":
    test_real_order()
