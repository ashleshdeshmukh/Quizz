from flask import Blueprint, request, jsonify
from backend.models import db, User
from flask_jwt_extended import create_access_token
import hashlib

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    hashed_pw = hashlib.sha256(data['password'].encode()).hexdigest()
    new_user = User(username=data['username'], password=hashed_pw, is_admin=data.get('is_admin', False))
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User registered")

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    hashed_pw = hashlib.sha256(data['password'].encode()).hexdigest()
    user = User.query.filter_by(username=data['username'], password=hashed_pw).first()
    if user:
        token = create_access_token(identity={'id': user.id, 'is_admin': user.is_admin})
        return jsonify({
            "token": token,
            "user_id": user.id,
            "username": user.username
        })
    #if user:
     #   token = create_access_token(identity={'id':user.id, 'is_admin':user.is_admin})
      #  return jsonify(token=token)
    return jsonify(message="Invalid credentials"), 401