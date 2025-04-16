from flask import Blueprint, request, jsonify, render_template, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from swiftcore.models import db, User

bp = Blueprint('auth', __name__)
@bp.route('/')
def home():
    return "Welcome to SwiftConnect!"
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']

        if User.query.get(username):
            return "User already exists!", 400

        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.get(request.form['username'])

        if user and check_password_hash(user.password, request.form['password']):
            session['username'] = user.username
            return render_template('home.html', username=user.username)
        return "Invalid credentials", 401

    return render_template('login.html')