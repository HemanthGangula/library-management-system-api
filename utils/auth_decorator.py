from flask import request, jsonify
from functools import wraps
from typing import Callable
from routes.auth import active_tokens

def token_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        token: str = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing.'}), 401
        if token not in active_tokens:
            return jsonify({'message': 'Invalid or expired token.'}), 401
        return f(*args, **kwargs)
    return decorated