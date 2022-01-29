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

@human_bp.route("/<username>", methods=["GET"])
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
def see_your_pet(username, name):
    your_pet_name = Pet.query.get(name)
    your_username = Human.query.get(username)
    found_pet = db.session.query(Pet).join(Human).filter(Human.username == your_username, Pet.name == your_pet_name)
    if not your_pet_name:
        return make_response({"Invalid pet name"}, 400)
    elif not found_pet:
        return make_response({"Pet not found"}, 404)
    elif not your_username: 
        return make_response({"Invalid username"}, 400)
    else:
        pass 


@pet_bp.route("/<username>/<zipcode>", methods=["GET"])
def find_new_pals(username, zipcode):
    target_zipcode = Pet.query.get(zipcode)
    your_username = Pet.query.get(username)
    pets_nearby = db.session.query(Pet.username, Pet.zipcode).filter(Pet.username != your_username, Pet.zipcode == target_zipcode)
    if not pets_nearby:
        return make_response({"No pets near yours"}, 404)
    elif not target_zipcode:
        return make_response({"Invalid zipcode"}, 400)
    elif not your_username:
        return make_response({"Invalid username"}, 400)
    else:
        pass 
