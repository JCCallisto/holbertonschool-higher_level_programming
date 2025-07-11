#!/usr/bin/env python3

import requests
import sys

try:
    response = requests.get('http://127.0.0.1:5000/basic-protected')
    if response.status_code == 401:
        print("PASS: Basic auth without credentials returns 401")
        sys.exit(0)
    else:
        print(f"FAIL: Expected 401, got {response.status_code}")
        sys.exit(1)
except requests.exceptions.ConnectionError:
    print("FAIL: Cannot connect to Flask app")
    sys.exit(1)
except Exception as e:
    print(f"FAIL: {e}")
    sys.exit(1)
