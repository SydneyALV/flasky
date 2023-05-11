from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.crystal import Crystal
from app.models.healer import Healer

crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")
healer_bp = Blueprint("healers", __name__, url_prefix="/healers")

def validate_model(cls, model_id):

    try: 
        model_id = int(model_id)
    except:
        abort(make_response(f"{cls.__name__} {model_id} is invalid. Must be an integer", 400))

    model_item = cls.query.get(model_id)

    if not model_item:
        abort(make_response(f"Crystal {model_id} was not found.", 404))

    return model_item

# Crystal Routes
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

# Healer Routes
@healer_bp.route("", methods=['POST'])
# define a route for creating a crystal resource
def create_healer():
    request_body = request.get_json()
    
    new_healer = Healer(
        name=request_body["name"]
    )
    
    db.session.add(new_healer)
    db.session.commit()
    
    return jsonify(f"Yayyyy Healer {new_healer.name} successfully created!"), 201


@healer_bp.route("", methods=["GET"])
def read_all_healers():
    
    healers = Healer.query.all()
        
    healers_response = []
    
    for healer in healers:
        healers_response.append({
            "id": healer.id,
            "name": healer.name
            })
    
    return jsonify(healers_response)

@healer_bp.route("/<healer_id>/crystals", methods=["POST"])
def create_crystal_by_id(healer_id):
    healer = validate_model(Healer, healer_id)
    
    request_body = request.get_json()

    new_crystal = Crystal.from_dict()

    db.session.add(new_crystal)
    db.session.commit()

    return jsonify(f"Crystal {new_crystal.name} from Healer {healer.name} has successfully been created!"), 201 

@healer_bp.route("/<healer_id>/crystals", methods=["GET"])
def get_all_crystals_by_healer_id(healer_id):
    healer = validate_model(Healer, healer_id)

    crystals_response = []

    for crystal in healer.crystals:
        crystals_response.append(crystal.to_dict())

    return jsonify(crystals_response)