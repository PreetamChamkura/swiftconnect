from flask import Blueprint, jsonify
import sqlite3

bp = Blueprint('explore', __name__, url_prefix='/explore')

@bp.route('/songs')
def get_songs():
    conn = sqlite3.connect('swiftie.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT song_id, title, album, era FROM song
    """)
    songs = cursor.fetchall()
    conn.close()
    return jsonify([
        {'song_id': s[0], 'title': s[1], 'album': s[2], 'era': s[3]}
        for s in songs
    ])
