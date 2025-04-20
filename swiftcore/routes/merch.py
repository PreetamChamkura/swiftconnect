# swiftcore/routes/merch.py
from flask import Blueprint, request, render_template, redirect, url_for
import sqlite3

bp = Blueprint('merch', __name__, url_prefix='/merch')

@bp.route('/add', methods=['GET', 'POST'])
def add_merch():
    if request.method == 'POST':
        name = request.form['name']
        image_url = request.form['image_url']

        conn = sqlite3.connect('swiftie.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO merch (name, image_url) VALUES (:name, :image_url)", {
            'name': name,
            'image_url': image_url
        })
        conn.commit()
        conn.close()

        return render_template('success.html', message="Merch added successfully!")

    return render_template('add_merch.html')
