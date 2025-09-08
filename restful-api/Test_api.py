#!/usr/bin/env python3
"""
Test script for the Flask API Security implementation
Run this script to test all the authentication endpoints
"""

import requests
import json
import base64
from requests.auth import HTTPBasicAuth

# Base URL - adjust if running on different host/port
BASE_URL = "http://localhost:5000"

def test_basic_auth():
    """Test Basic Authentication endpoints"""
    print("=== Testing Basic Authentication ===")
    
    # Test without credentials
    print("1. Testing /basic-protected without credentials:")
    response = requests.get(f"{BASE_URL}/basic-protected")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test with invalid credentials
    print("\n2. Testing /basic-protected with invalid credentials:")
    response = requests.get(f"{BASE_URL}/basic-protected", auth=HTTPBasicAuth('invalid', 'wrong'))
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test with valid credentials
    print("\n3. Testing /basic-protected with valid credentials:")
    response = requests.get(f"{BASE_URL}/basic-protected", auth=HTTPBasicAuth('user1', 'password'))
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text}")
    
def test_jwt_auth():
    """Test JWT Authentication endpoints"""
    print("\n=== Testing JWT Authentication ===")
    
    # Test login with invalid credentials
    print("1. Testing /login with invalid credentials:")
    response = requests.post(f"{BASE_URL}/login", 
                           json={"username": "invalid", "password": "wrong"})
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test login with valid credentials (user)
    print("\n2. Testing /login with valid user credentials:")
    response = requests.post(f"{BASE_URL}/login", 
                           json={"username": "user1", "password": "password"})
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        user_token = response.json()['access_token']
        print(f"   Token received: {user_token[:50]}...")
    
    # Test login with valid credentials (admin)
    print("\n3. Testing /login with valid admin credentials:")
    response = requests.post(f"{BASE_URL}/login", 
                           json={"username": "admin1", "password": "password"})
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        admin_token = response.json()['access_token']
        print(f"   Token received: {admin_token[:50]}...")
    
    return user_token if 'user_token' in locals() else None, admin_token if 'admin_token' in locals() else None

def test_jwt_protected_routes(user_token, admin_token):
    """Test JWT protected routes"""
    print("\n=== Testing JWT Protected Routes ===")
    
    # Test /jwt-protected without token
    print("1. Testing /jwt-protected without token:")
    response = requests.get(f"{BASE_URL}/jwt-protected")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test /jwt-protected with invalid token
    print("\n2. Testing /jwt-protected with invalid token:")
    headers = {"Authorization": "Bearer invalid_token"}
    response = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test /jwt-protected with valid token
    if user_token:
        print("\n3. Testing /jwt-protected with valid user token:")
        headers = {"Authorization": f"Bearer {user_token}"}
        response = requests.get(f"{BASE_URL}/jwt-protected", headers=headers)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text}")

def test_role_based_access(user_token, admin_token):
    """Test role-based access control"""
    print("\n=== Testing Role-Based Access Control ===")
    
    # Test /admin-only without token
    print("1. Testing /admin-only without token:")
    response = requests.get(f"{BASE_URL}/admin-only")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test /admin-only with user token (should fail)
    if user_token:
        print("\n2. Testing /admin-only with user token:")
        headers = {"Authorization": f"Bearer {user_token}"}
        response = requests.get(f"{BASE_URL}/admin-only", headers=headers)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    
    # Test /admin-only with admin token (should succeed)
    if admin_token:
        print("\n3. Testing /admin-only with admin token:")
        headers = {"Authorization": f"Bearer {admin_token}"}
        response = requests.get(f"{BASE_URL}/admin-only", headers=headers)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text}")

def main():
    """Run all tests"""
    print("Starting API Security Tests...")
    print("Make sure your Flask app is running on http://localhost:5000")
    print("-" * 60)
    
    try:
        # Test health endpoint
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code != 200:
            print("Error: Cannot connect to the API. Make sure it's running.")
            return
        
        # Run tests
        test_basic_auth()
        user_token, admin_token = test_jwt_auth()
        test_jwt_protected_routes(user_token, admin_token)
        test_role_based_access(user_token, admin_token)
        
        print("\n" + "=" * 60)
        print("Testing completed!")
        
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to the API. Make sure it's running on http://localhost:5000")
    except Exception as e:
        print(f"Error during testing: {e}")

if __name__ == "__main__":
    main()
