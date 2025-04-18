from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="../templates")
    app.secret_key = 'super_secret_key'

    from swiftcore.routes.auth import bp as auth_bp
    from swiftcore.routes.tour import bp as tour_bp
    from swiftcore.routes.explore import bp as explore_bp
    from swiftcore.routes.wishlist import bp as wishlist_bp
    from swiftcore.routes.playlist import bp as playlist_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tour_bp)
    app.register_blueprint(explore_bp)
    app.register_blueprint(wishlist_bp)
    app.register_blueprint(playlist_bp)

    return app
