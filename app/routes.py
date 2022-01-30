from flask import Blueprint, request, jsonify, make_response
from app import db 
from app.models.human import Human
from app.models.pet import Pet

human_bp = Blueprint("human", __name__, url_prefix="/human")

pet_bp = Blueprint("pet", __name__, url_prefix="/pet")

#human routes
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

@human_bp.route("/<username>", methods=["GET", "DELETE"])
def manage_profile_by_username(username):
    username=Human.query.get(username)
    if request.method == "GET":
        if not username:
            return jsonify({"Profile not found."}), 404
        else:
            #look into routers???
            pass

    elif request.method == "DELETE":
        if not username:
            return jsonify({"Profile was not found."}), 404
        else:
            db.session.delete(username)
            db.session.commit()
            return make_response({"User deleted."})


#pet routes
@pet_bp.route("/<username>", methods=["POST"])
def add_a_pet(username):
    current_user = Human.query.get(username)
    if not username:
        return make_response({"Username not found."}, 400)
    request_body = request.get_json()
    if request_body['name'].strip() == "" or 'name' not in request_body:
        return make_response({"Your pet must have a name."}, 400)
    else:
        new_profile = Pet(name=request_body["name"], zipcode=Human.pet["zipcode"])

        db.session.add(new_profile)
        db.session.commit()
        current_user.pets.append(Pet.query.get(new_profile.name))
        db.session.commit()

        return(new_profile.convert_human_to_dict()), 201


@pet_bp.route("/<username>/<name>", methods=["GET", "DELETE"])
def see_your_pet(username, name):
    your_pet_name = Pet.query.get(name)
    your_username = Human.query.get(username)
    found_pet = db.session.query(Pet).join(Human).filter(Human.username == your_username, Pet.name == your_pet_name)
    if request.method == "GET": 
        if not your_pet_name:
            return make_response({"Invalid pet name."}, 400)
        elif not found_pet:
            return make_response({"Pet profile not found."}, 404)
        elif not your_username: 
            return make_response({"Invalid username."}, 400)
        else:
            pass 
    
    elif request.method == "DELETE":
        if not your_username:
            return jsonify({"User not found."}), 404
        elif not your_pet_name:
            return jsonify({"Pet profile not found."}, 404)
        else:
            db.session.delete(your_pet_name)
            db.session.commit()
            return make_response({"Pet profile deleted."})



@pet_bp.route("/<username>/<zipcode>", methods=["GET"])
def find_new_pals(username, zipcode):
    target_zipcode = Pet.query.get(zipcode)
    your_username = Pet.query.get(username)
    pals_nearby = db.session.query(Pet.username, Pet.zipcode).filter(Pet.username != your_username, Pet.zipcode == target_zipcode)
    if not pals_nearby:
        return make_response({"No nearby pals."}, 404)
    elif not target_zipcode:
        return make_response({"Invalid zipcode."}, 400)
    elif not your_username:
        return make_response({"Invalid username."}, 400)
    else:
        pass 

