from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from swiftcore.models import db, User

bp = Blueprint('auth', __name__, url_prefix='/auth')
@bp.route('/')
def home():
    return "Welcome to SwiftConnect 💖🎤✨"
@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = generate_password_hash(data['password'])
    email = data['email']

    if User.query.get(username):
        return jsonify({'error': 'User already exists'}), 400

    user = User(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.get(data['username'])

    if user and check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401