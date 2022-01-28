from flask import Blueprint, request, jsonify, make_response
from app import db 
from app.models.human import Human
from app.models.pet import Pet

human_bp = Blueprint("human", __name__, url_prefix="/human")

pet_bp = Blueprint("pet", __name__, url_prefix="/pet")

@human_bp.route("", methods=["POST"])
def create_a_profile():
    request_body = request.get_json()
    if request_body['username'].strip() == "" or 'username' not in request_body:
        return make_response({"You must have a username."}, 400)
    elif request_body['zipcode'].strip() == "" or 'zipcode' not in request_body:
        return make_response({"You must have a zipcode."}, 400)
    else:
        new_profile = Human(username=request_body["username"], zipcode=request_body["zipcode"])

        db.session.add(new_profile)
        db.session.commit()
        return(new_profile.convert_human_to_dict()), 201

@human_bp.route("", methods=["GET"])
def get_profile_by_username(username):
    username=Human.query.get(username)
    if not username:
        return jsonify({"Profile was not found."}), 404
    else:
        #look into routers???
        pass


@pet_bp.route("", methods=["POST"])
def add_a_pet():
    request_body = request.get_json()
    if request_body['name'].strip() == "" or 'name' not in request_body:
        return make_response({"Your pet must have a name."}, 400)
    else:
        new_profile = Pet(name=request_body["name"], zipcode=Human.pet["zipcode"])

        db.session.add(new_profile)
        db.session.commit()
        return(new_profile.convert_human_to_dict()), 201
        
        
        


@pet_bp.route("/<username>/<name>", methods=["GET"])
def see_your_pet():
