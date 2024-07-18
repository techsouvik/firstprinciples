from flask import Blueprint, request, jsonify
from auth_service.controllers.auth_controller import register_user, login_user, verify_token

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return jsonify(register_user(data))

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify(login_user(data))

@auth_bp.route('/verify', methods=['POST'])
def verify():
    token = request.headers.get('x-access-token')
    return jsonify(verify_token(token))
