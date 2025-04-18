from flask import Blueprint, request, jsonify
import sqlite3

bp = Blueprint('wishlist', __name__, url_prefix='/wishlist')

@bp.route('/<username>', methods=['GET'])
def get_wishlist(username):
    conn = sqlite3.connect('swiftie.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT merch.name, merch.image_url
        FROM merch
        JOIN wishlist_items ON merch.merch_id = wishlist_items.merch_id
        JOIN merch_wishlist ON wishlist_items.wishlist_id = merch_wishlist.wishlist_id
        WHERE merch_wishlist.username = :username
    """, {'username': username})
    items = cursor.fetchall()
    conn.close()
    return jsonify([
        {'name': i[0], 'image_url': i[1]}
        for i in items
    ])
