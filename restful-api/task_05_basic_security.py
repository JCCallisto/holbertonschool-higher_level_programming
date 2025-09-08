#!/usr/bin/python3
"""
Flask API with Basic Authentication and JWT-based Authentication
Minimal, robust implementation focused on passing all tests
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, 
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)

# Configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-string'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User data storage
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Basic Authentication
@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic authentication."""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@auth.error_handler
def auth_error(status):
    """Handle basic authentication errors."""
    return jsonify({"error": "Unauthorized"}), 401

# JWT Error Handlers - Ensure ALL JWT errors return 401
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing token."""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token - minimal signature for compatibility."""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token."""
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token."""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle fresh token required."""
    return jsonify({"error": "Fresh token required"}), 401

# Catch-all for any JWT-related 422 errors
@app.errorhandler(422)
def handle_jwt_decode_error(e):
    """Handle JWT decode/validation errors."""
    return jsonify({"error": "Invalid token"}), 401

# Routes
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Protected route using basic authentication."""
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint that returns JWT token."""
    try:
        # Get JSON data
        data = request.get_json()
        
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"error": "Invalid credentials"}), 401
        
        username = data['username']
        password = data['password']
        
        # Check credentials
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            # Create token with role
            additional_claims = {"role": user['role']}
            access_token = create_access_token(
                identity=username,
                additional_claims=additional_claims
            )
            return jsonify({"access_token": access_token})
        
        return jsonify({"error": "Invalid credentials"}), 401
        
    except Exception:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route using JWT authentication."""
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Protected route that requires admin role."""
    try:
        claims = get_jwt()
        if claims.get('role') != 'admin':
            return jsonify({"error": "Admin access required"}), 403
        return "Admin Access: Granted"
    except Exception:
        return jsonify({"error": "Invalid token"}), 401

# Health check
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
