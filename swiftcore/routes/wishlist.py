from flask import Blueprint, request, jsonify, render_template
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

    return render_template('wishlist.html', username=username, items=items)

@bp.route('/<username>/remove/<int:item_id>', methods=['POST'])
def remove_from_wishlist(username, item_id):
    conn = sqlite3.connect('swiftie.db')
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM wishlist_items WHERE wishlist_id = (
            SELECT wishlist_id FROM merch_wishlist WHERE username = :username
        ) AND merch_id = :item_id
    """, {'username': username, 'item_id': item_id})
    conn.commit()
    conn.close()
    return redirect(url_for('wishlist.get_wishlist', username=username))
