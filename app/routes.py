from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.crystal import Crystal

def validate_model(cls, model_id):

    try: 
        model_id = int(model_id)
    except:
        abort(make_response(f"{cls.__name__} {model_id} is invalid. Must be an integer", 400))

    model_item = cls.query.get(model_id)

    if not model_item:
        abort(make_response(f"Crystal {model_id} was not found.", 404))

    return model_item

crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

@crystal_bp.route("", methods=["POST"])

# define a route for creating a crystal resource
def handle_crystals():
    request_body = request.get_json()
    
    new_crystal = Crystal.from_dict(request_body)

    db.session.add(new_crystal)
    db.session.commit()

    return jsonify(f"Crystal {new_crystal.name} has successfully been created!"), 201

@crystal_bp.route("", methods=["GET"])

# define a route for reading all crystals
def read_all_crystals():
    
    # filter the crystal query results to 
    # those whose color matches the requested color
    color_query = request.args.get("color")
    
    if color_query:
        crystals = Crystal.query.filter_by(color=color_query)
    else:
        crystals = Crystal.query.all()
    
    crystals_response = []

    for crystal in crystals:
        crystals_response.append(crystal.to_dict())

    return jsonify(crystals_response)

# define a route for getting a single crystal
@crystal_bp.route("/<crystal_id>", methods=["GET"])

def read_one_crystal(crystal_id):
    # validate crystal id
    # query our db
    crystal = validate_model(Crystal, crystal_id)

    return crystal.to_dict(), 200

# define a route for updating a single crystal
@crystal_bp.route("/<crystal_id>", methods=["PUT"])

def update_crystal(crystal_id):
    # validate crystal id
    # crystal_id = validate_model(crystal_id)

    crystal = validate_model(Crystal, crystal_id)

    request_body = request.get_json()

    crystal.name = request_body["name"]
    crystal.color = request_body["color"]
    crystal.powers = request_body["powers"]

    db.session.commit()

    return make_response(f"Crystal {crystal_id} has been successfully updated.", 200)

# define a route for deleting a single crystal
@crystal_bp.route("/<crystal_id>", methods=["DELETE"])

def delete_crystal(crystal_id):
    # validate crystal id
    # crystal_id = validate_model(crystal_id)

    crystal = validate_model(Crystal, crystal_id)

    db.session.delete(crystal)
    db.session.commit()

    return make_response(f"Crystal {crystal_id} has been successfully deleted.", 200)