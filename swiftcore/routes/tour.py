from flask import Blueprint, request, jsonify, render_template
import sqlite3

bp = Blueprint('tour', __name__, url_prefix='/tour')

@bp.route('/create', methods=['GET', 'POST'])
def create_tour():
    if request.method == 'POST':
        location = request.form['location']
        era = request.form.get('era')
        time = request.form.get('time')
        date = request.form['date']
        username = request.form['username']
        playlist_id = request.form.get('playlist_id')

        conn = sqlite3.connect('swiftie.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tour (location, era, time, date, username, playlist_id)
            VALUES (:location, :era, :time, :date, :username, :playlist_id)
        """, {
            'location': location,
            'era': era,
            'time': time,
            'date': date,
            'username': username,
            'playlist_id': playlist_id
        })
        conn.commit()
        conn.close()

        return render_template('success.html', message="Tour created successfully!")

    return render_template('create_tour.html')

@bp.route('/<int:tour_id>/delete', methods=['POST'])
def delete_tour(tour_id):
    conn = sqlite3.connect('swiftie.db')
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM tour WHERE tour_id = :tour_id
    """, {'tour_id': tour_id})
    conn.commit()
    conn.close()

    return redirect(url_for('tour.get_user_tours', username=session['username']))

@bp.route('/<username>', methods=['GET'])
def get_user_tours(username):
    conn = sqlite3.connect('swiftie.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT tour_id, location, era, time, date FROM tour WHERE username = :username
    """, {'username': username})
    tours = cursor.fetchall()
    conn.close()
    return render_template('user_tours.html', tours=tours)
