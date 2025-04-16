from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    tours = db.relationship('Tour', backref='user', lazy='select')
    playlists  = db.relationship('Playlist', backref='user', lazy='select')
    wishlist = db.relationship('MerchWishlist', backref='user', uselist=False)

class Tour(db.Model):
    __tablename__ = 'tours'
    tour_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)

class Song(db.Model):
    __tablename__ = 'songs'
    song_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    album = db.Column(db.String)
    era = db.Column(db.String)

class Playlist(db.Model):
    __tablename__ = 'playlists'
    playlist_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)

class PlaylistSong(db.Model):
    __tablename__ = 'playlist_songs'
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.playlist_id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.song_id'), primary_key=True)

class Merch(db.Model):
    __tablename__ = 'merch'
    merch_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)

class MerchWishlist(db.Model):
    __tablename__ = 'wishlists'
    wishlist_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)

class WishlistItem(db.Model):
    __tablename__ = 'wishlist_items'
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlists.wishlist_id'), primary_key=True)
    merch_id = db.Column(db.Integer, db.ForeignKey('merch.merch_id'), primary_key=True)


