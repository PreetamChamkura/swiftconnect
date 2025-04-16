from flask import Blueprint, request, jsonify
from swiftcore.models import db, Tour

bp = Blueprint('tour', __name__)
@bp.route('/tours', methods=['POST'])
def create_tour():
    data = request.get_json()
    tour = Tour(
        name=data['name'],
        location=data['location'],
        date=data['date'],
        username=data['username']
    )
    db.session.add(tour)
    db.session.commit()
    return jsonify({'message': 'Tour created successfully'})
