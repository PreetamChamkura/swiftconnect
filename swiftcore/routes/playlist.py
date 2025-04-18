from flask import Blueprint, request, jsonify
import sqlite3

bp = Blueprint('playlist', __name__, url_prefix='/playlist')

@bp.route('/', methods=['POST'])
def create_playlist():
    data = request.get_json()
    username = data.get('username')
    conn = sqlite3.connect('swiftie.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO playlist (username) VALUES (:username)
    """, {'username': username})
    conn.commit()
    conn.close()
    return jsonify({'message': 'Playlist created successfully'})

@bp.route('/<username>', methods=['GET'])
def get_user_playlists(username):
    conn = sqlite3.connect('swiftie.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT playlist_id FROM playlist WHERE username = :username
    """, {'username': username})
    playlists = cursor.fetchall()
    conn.close()
    return jsonify({'playlists': [p[0] for p in playlists]})
