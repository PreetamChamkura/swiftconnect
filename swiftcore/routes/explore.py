from flask import Blueprint, jsonify, render_template
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
    return render_template('explore_songs.html', songs=songs)
