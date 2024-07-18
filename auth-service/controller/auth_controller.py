from auth_service.models.user import User
from auth_service.app import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from flask import current_app as app

def register_user(data):
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return {'message': 'Registered successfully'}, 201

def login_user(data):
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return {'message': 'Login failed'}, 401
    token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, app.config['SECRET_KEY'])
    return {'token': token}, 200

def verify_token(token):
    if not token:
        return {'message': 'Token is missing'}, 401
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        user = User.query.filter_by(id=data['user_id']).first()
        if not user:
            return {'message': 'Token is invalid'}, 401
    except Exception as e:
        return {'message': 'Token is invalid'}, 401
    return {'message': 'Token is valid'}, 200
