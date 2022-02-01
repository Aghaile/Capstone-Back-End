from flask import Blueprint, request, jsonify, make_response
from app import db 
from app.models.pet import Pet
from app.models.friendship import Friendship



pet_bp = Blueprint("pet", __name__, url_prefix="/pet")
friendship_bp = Blueprint("friendship", __name__, url_prefix="/friendship")


@pet_bp.route("", methods=["POST"]) #for the "create profile" page
def create_a_profile():
    request_body = request.get_json()
    if request_body['name'].strip() == "" or 'name' not in request_body:
        return make_response({"details": "Request body must include name."}, 400)
    elif request_body['zipcode'].strip() == "" or 'zipcode' not in request_body:
        return make_response({"details": "Request body must include zipcode."}, 400)
    elif request_body['phone_number'].strip() == "" or 'phone_number' not in request_body:
        return make_response({"details": "Request body must include a phone number."}, 400)
    else:
        # taking info fr request_body and converting it to new Board object
        new_profile = Pet.convert_pet_to_dict(request_body)
        # committing changes to db
        db.session.add(new_profile)
        db.session.commit()
        return(new_profile.convert_pet_to_dict()), 201

@pet_bp.route("/pet/<pet_id>", methods=["GET", "PATCH", "DELETE"]) #for the welcome page
def find_a_profile(pet_id):
    # either get Card back or None, card here is an object
    pet = Pet.query.get(pet_id)
    if pet is None:
        return make_response({"message": f"{pet.name} was not found"}, 404)

    # PATCH will change just one part of the record, not the whole record

    if request.method == "PATCH":
        form_data = request.get_json()
        if "bio" in form_data:
            pet.bio = form_data["bio"]
        elif "zipcode" in form_data:
            pet.zipcode = form_data["zipcode"]
        elif "phone_number" in form_data:
            pet.phone_number = ["phone_number"]
            db.session.commit()
            return make_response({}, 200)

    if request.method == "DELETE":
        # query db for specific card object by the card id
        # if Card.query.filter_by(id=card_id):
        db.session.delete(pet)
        db.session.commit()
        return make_response({'message': f"{pet.name}'s profile was deleted"}, 200)