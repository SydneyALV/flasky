from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.crystal import Crystal

crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

@crystal_bp.route("", methods=["POST"])

# define a route for creating a crystal resource
def handle_crystals():
    request_body = request.get_json()
    
    new_crystal = Crystal(
        name = request_body["name"],
        color = request_body["color"],
        powers = request_body["powers"]
    )

    db.session.add(new_crystal)
    db.session.commit()

    return make_response(f"Crystal {new_crystal.name} has successfully been created!", 201)

@crystal_bp.route("", methods=["GET"])

# define a rute for reading all crystals
def read_all_crystals():
    crystals_response = []
    crystals = Crystal.query.all()

    for crystal in crystals:
        crystals_response.append({
            "id": crystal.id,
            "name": crystal.name,
            "color": crystal.color,
            "powers": crystal.powers
        })

    return jsonify(crystals_response)
