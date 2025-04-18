from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/')
def home():
    return "Welcome to SwiftConnect!"

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('swiftie.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE username = :username", {'username': username})
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password):
            session['username'] = user['username']
            conn.close()
            return render_template('home.html', username=user['username'])

        conn.close()
        return "Invalid credentials", 401

    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']

        conn = sqlite3.connect('swiftie.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE username = :username", {'username': username})
        if cursor.fetchone():
            conn.close()
            return "User already exists!", 400

        cursor.execute("INSERT INTO user (username, password, email) VALUES (:username, :password, :email)", {
            'username': username,
            'password': password,
            'email': email
        })
        conn.commit()
        conn.close()
        return redirect(url_for('auth.login'))

    return render_template('register.html')
