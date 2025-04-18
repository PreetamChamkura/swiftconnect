from flask import Blueprint, request, jsonify
import sqlite3

bp = Blueprint('tour', __name__)

@bp.route('/tours', methods=['POST'])
def create_tour():
    data = request.get_json()
    conn = sqlite3.connect('swiftie.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tour (location, era, time, date, username, playlist_id)
        VALUES (:location, :era, :time, :date, :username, :playlist_id)
    """, {
        'location': data['location'],
        'era': data.get('era'),
        'time': data.get('time'),
        'date': data['date'],
        'username': data['username'],
        'playlist_id': data.get('playlist_id')
    })
    conn.commit()
    conn.close()
    return jsonify({'message': 'Tour created successfully'})