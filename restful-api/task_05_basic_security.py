from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-this-in-production'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic authentication"""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized access"}), 401

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle unauthorized JWT access"""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token"""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired JWT token"""
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked JWT token"""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle need for fresh JWT token"""
    return jsonify({"error": "Fresh token required"}), 401

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Protected route using basic authentication"""
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint that returns JWT token"""
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password required"}), 400

    username = data['username']
    password = data['password']

    if username in users and check_password_hash(users[username]['password'], password):
        additional_claims = {"role": users[username]['role']}
        access_token = create_access_token(identity=username, additional_claims=additional_claims)
        return jsonify({"access_token": access_token})

    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route using JWT authentication"""
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Protected route for admin users only"""
    claims = get_jwt()
    user_role = claims.get('role')

    if user_role != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run(debug=True)
