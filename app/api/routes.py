from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
import hashlib
from app.extensions import db
from app.Domain.user import User
from app.api import verify_user

api_routes = Blueprint('api', __name__)


@api_routes.route('/api/example', methods=['GET'])
def example_route():
    data = {
        'message': 'Example API route',
        'status': 'success'
    }
    return jsonify(data), 200


@api_routes.route('/user/login', methods=['POST'])
def user_login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = verify_user(username, password)

    if user:
        access_token = create_access_token(identity=user.username)
        return jsonify({'access_token': access_token,
                        'user': {'username': user.username, 'email': user.email, 'name': user.name,
                                 'surname': user.surname}})
    else:
        return jsonify({'message': 'Kullanıcı adı veya şifre yanlış'}), 401


@api_routes.route('/user/register', methods=['POST'])
def user_register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    password_confirm = data.get('passwordConfirm')
    name = data.get('name')
    surname = data.get('surname')

    if password != password_confirm:
        return jsonify({'message': 'Kullanıcı adı veya şifre yanlış'}), 400

    if not username or not email or not password or not name or not surname:
        return jsonify({'message': 'Lütfen tüm alanları doldurun'}), 400

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'message': 'Kullanıcı adı yada email zaten mevcut'}), 400

    hashed_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()

    user = User(username=username, email=email, password=hashed_pass, name=name, surname=surname)
    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=user.username)

    return jsonify(
        {'user': {'username': user.username, 'email': user.email, 'name': user.name, 'surname': user.surname},
         'access_token': access_token}), 201
