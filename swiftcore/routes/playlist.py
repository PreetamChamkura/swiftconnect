from flask import Blueprint, request, jsonify, render_template
import sqlite3

bp = Blueprint('playlist', __name__, url_prefix='/playlist')

@bp.route('/create', methods=['GET', 'POST'])
def create_playlist():
    if request.method == 'POST':
        username = request.form['username']

        conn = sqlite3.connect('swiftie.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO playlist (username) VALUES (:username)
        """, {'username': username})
        conn.commit()
        conn.close()

        return render_template('success.html', message="Playlist created successfully!")

    return render_template('create_playlist.html')

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

@bp.route('/add-song', methods=['GET', 'POST'])
def add_song_to_playlist():
    conn = sqlite3.connect('swiftie.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        playlist_id = request.form['playlist_id']
        song_id = request.form['song_id']
        cursor.execute("""
            INSERT INTO playlist_song (playlist_id, song_id)
            VALUES (:playlist_id, :song_id)
        """, {'playlist_id': playlist_id, 'song_id': song_id})
        conn.commit()
        conn.close()
        return render_template('success.html', message="Song added to playlist!")

    
    cursor.execute("SELECT playlist_id FROM playlist")
    playlists = cursor.fetchall()
    cursor.execute("SELECT song_id, title FROM song")
    songs = cursor.fetchall()
    conn.close()

    return render_template('add_song_to_playlist.html', playlists=playlists, songs=songs)

@bp.route('/<int:playlist_id>/share', methods=['GET'])
def share_playlist(playlist_id):
    shareable_link = url_for('playlist.get_user_playlists', username=session['username'], _external=True) + f'/{playlist_id}'
    return render_template('share_playlist.html', link=shareable_link)
