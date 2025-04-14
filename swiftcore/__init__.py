from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///swiftconnect.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'super_secret_key'
    db.init_app(app)
    from swiftcore.routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    with app.app_context():
        db.create_all()
    return app