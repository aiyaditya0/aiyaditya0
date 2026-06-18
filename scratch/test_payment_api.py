import urllib.request
import json

def test_api_query(name, url_suffix, payload):
    url = "https://ae-payment-server.vercel.app/initiate-phonepe-payment" + url_suffix
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            print(f"{name} -> Status: {resp.status}, Amount: {res.get('amount')}, OrderId: {res.get('merchantOrderId')}")
    except Exception as e:
        print(f"{name} -> Error: {e}")

test_api_query("Query param: ?amount=99", "?amount=99", {
    "name": "Test User", "email": "test@example.com", "whatsapp": "9876543210", "bizType": "Freelancer", "goals": ""
})

test_api_query("Query param: ?amount=199", "?amount=199", {
    "name": "Test User", "email": "test@example.com", "whatsapp": "9876543210", "bizType": "Freelancer", "goals": ""
})

test_api_query("Query param: ?amount=9900 (paise)", "?amount=9900", {
    "name": "Test User", "email": "test@example.com", "whatsapp": "9876543210", "bizType": "Freelancer", "goals": ""
})
