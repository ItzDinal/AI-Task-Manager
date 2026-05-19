import json
import urllib.request
import urllib.parse

base_url = 'http://127.0.0.1:8000/api/v1/auth'

# create a user for login
payload = {'email': 'auth_test_internal4@example.com', 'password': 'Secret123!'}
req = urllib.request.Request(
    f'{base_url}/register',
    data=json.dumps(payload).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST',
)
with urllib.request.urlopen(req, timeout=20) as resp:
    print('register', resp.status)
    print(resp.read().decode())

# login
login_data = urllib.parse.urlencode({'username': payload['email'], 'password': payload['password']}).encode('utf-8')
req = urllib.request.Request(
    f'{base_url}/login',
    data=login_data,
    headers={'Content-Type': 'application/x-www-form-urlencoded'},
    method='POST',
)
with urllib.request.urlopen(req, timeout=20) as resp:
    print('login', resp.status)
    token = json.loads(resp.read().decode())['access_token']
    print(token)

# current user
req = urllib.request.Request(
    f'{base_url}/me',
    headers={'Authorization': f'Bearer {token}'},
    method='GET',
)
with urllib.request.urlopen(req, timeout=20) as resp:
    print('me', resp.status)
    print(resp.read().decode())
