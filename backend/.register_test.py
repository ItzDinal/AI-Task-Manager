import json
import urllib.request

req = urllib.request.Request(
    'http://127.0.0.1:8001/api/v1/auth/register',
    data=json.dumps({'email': 'auth_test_user2@example.com', 'password': 'Secret123!'}).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST',
)
with urllib.request.urlopen(req, timeout=20) as resp:
    print(resp.status)
    print(resp.read().decode())
