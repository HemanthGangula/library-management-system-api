from flask import Blueprint, request, jsonify
from typing import Optional
import uuid

bp = Blueprint('auth', __name__, url_prefix='/auth')

# In-memory storage for tokens
active_tokens: set = set()

# Simple user store for demonstration purposes
USER_DATA = {
    "admin": "password123"
}

@bp.route('/login', methods=['POST'])
def login() -> jsonify:
    data = request.get_json()
    username: Optional[str] = data.get('username')
    password: Optional[str] = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Username and password are required.'}), 400
    
    if USER_DATA.get(username) == password:
        token: str = str(uuid.uuid4())
        active_tokens.add(token)
        return jsonify({'token': token}), 200
    
    return jsonify({'message': 'Invalid credentials.'}), 401

@bp.route('/logout', methods=['POST'])
def logout() -> jsonify:
    data = request.get_json()
    token: Optional[str] = data.get('token')
    
    if token in active_tokens:
        active_tokens.remove(token)
        return jsonify({'message': 'Logged out successfully.'}), 200
    
    return jsonify({'message': 'Invalid token.'}), 400