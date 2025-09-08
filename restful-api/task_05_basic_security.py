#!/usr/bin/python3
"""
Flask API with Basic Authentication and JWT-based Authentication
This module implements secure API endpoints with different authentication methods.
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)

# Configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-string'  # Change this in production!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Initialize extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User data storage (in-memory for this example)
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
    return jsonify({"error": "Unauthorized access"}), 401

# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token errors."""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(jwt_header, jwt_payload):
    """Handle invalid token errors."""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token errors."""
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token errors."""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle fresh token required errors."""
    return jsonify({"error": "Fresh token required"}), 401

# Helper function to get user by username
def get_user_by_username(username):
    """Get user data by username."""
    return users.get(username)

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
        data = request.get_json()
        
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"error": "Username and password required"}), 400
        
        username = data['username']
        password = data['password']
        
        user = get_user_by_username(username)
        
        if user and check_password_hash(user['password'], password):
            # Create JWT token with user identity and role
            additional_claims = {"role": user['role']}
            access_token = create_access_token(
                identity=username,
                additional_claims=additional_claims
            )
            return jsonify({"access_token": access_token})
        
        return jsonify({"error": "Invalid credentials"}), 401
        
    except Exception as e:
        return jsonify({"error": "Bad request"}), 400

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route using JWT authentication."""
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Protected route that requires admin role."""
    current_user = get_jwt_identity()
    claims = get_jwt()
    
    # Check if user has admin role
    if claims.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"

# Additional utility routes for testing

@app.route('/user-info', methods=['GET'])
@jwt_required()
def get_user_info():
    """Get current user information from JWT token."""
    current_user = get_jwt_identity()
    claims = get_jwt()
    user_data = get_user_by_username(current_user)
    
    if user_data:
        return jsonify({
            "username": current_user,
            "role": claims.get('role', 'unknown')
        })
    
    return jsonify({"error": "User not found"}), 404

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "message": "API is running"}), 200

# Error handlers for general HTTP errors
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors."""
    return jsonify({"error": "Method not allowed"}), 405

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Print startup message for debugging
    print("Starting Flask API Security Server...")
    print("Available endpoints:")
    print("  GET  /basic-protected - Basic auth required")
    print("  POST /login - Get JWT token")  
    print("  GET  /jwt-protected - JWT token required")
    print("  GET  /admin-only - Admin role required")
    print("  GET  /health - Health check")
    app.run(debug=False, host='0.0.0.0', port=5000)