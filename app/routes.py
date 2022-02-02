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
    elif request_body['zipcode'] == "" or 'zipcode' not in request_body:
        return make_response({"details": "Request body must include zipcode."}, 400)
    elif request_body['phone_number'] == "" or 'phone_number' not in request_body:
        return make_response({"details": "Request body must include a phone number."}, 400)
    new_profile = Pet(
        name = request_body["name"],
        zipcode = request_body["zipcode"],
        phone_number = request_body["phone_number"]
        )
    db.session.add(new_profile)
    db.session.commit()
    confirmed = new_profile.convert_pet_to_dict()
    return jsonify(confirmed), 201

@pet_bp.route("/<pet_id>", methods=["GET", "PATCH", "DELETE"]) #for the welcome page
def find_a_profile(pet_id):
    if not pet_id.isnumeric():
         return jsonify(None), 400

    pet = Pet.query.get(pet_id)

    if not pet:
        return jsonify({"message": f"Pet {pet_id} was not found"}), 404
    
    if request.method == "GET":
        return jsonify(pet.convert_pet_to_dict()), 200

    elif request.method == "PATCH":
        pet_update_request_body = request.get_json()
        pet.name = pet_update_request_body["name"],
        pet.bio = pet_update_request_body["bio"],
        pet.age = pet_update_request_body["age"],
        pet.gender = pet_update_request_body["gender"],
        pet.zipcode = pet_update_request_body["zipcode"],
        pet.phone_number = pet_update_request_body["phone_number"]

        db.session.commit()

        updated_pet_response = pet.convert_pet_to_dict()

        return jsonify(updated_pet_response), 200

    elif request.method == "DELETE":
        db.session.delete(pet)
        db.session.commit()
        pet_delete_response = pet.convert_pet_to_dict()

        print("********", pet_delete_response), 200
        return jsonify(pet_delete_response), 200


# @friendship_bp.route("/<pet_id>", methods=["GET"])
# def get_all_friendships_for_one_pet(pet_id):
#     if not Pet.query.get(pet_id):
#         return jsonify({"details": f"{pet_id} was not found"}), 404

#     sort_query = request.args.get("sort")
#     if sort_query == "potential_pals":
#         pals = Friendship.query.get(Friendship.friendship_id).filter_by(potential_pals=True).all()
#     if sort_query == "pending_pals":
#         pals = Friendship.query.get(Friendship.friendship_id).filter_by(pending_pals=True).all()
#     if sort_query == "pawsitively_pals":
#         pals = Friendship.query.get(Friendship.friendship_id).filter_by(pawsitively_pals=True).all()
#     else:
#         # no order specified
#         pals = Friendship.query.get(pet_id).pals
#     return jsonify([pals]), 200

# @friendship_bp.route("/add", methods=["POST"])
# def add_new_pal():
#     pal_request_body = request.get_json()
    
#     if "pet_id" not in pal_request_body or "pal_id" not in pal_request_body:
#         return jsonify(None), 400

#     your_pet = Pet.query.get(pal_request_body["pet_id"])
#     if your_pet is None:
#         return jsonify(None), 404

#     friends_pet = Pet.query.get(pal_request_body["pal_id"])
#     if friends_pet is None:
#         return jsonify(None), 404
    
#     if Friendship.your_pet.pawsitively_pals == True:
#         return jsonify({"message": "You are already pals!"}), 400
    
#     db.session.query(Friendship).filter(Friendship.pal_id == your_pet).update({"pawsitively_pals": (True)})

#     new_pal = Friendship(
#         pet_id=your_pet,
#     )

#     db.session.add(new_pal)
#     db.session.commit() 
    
#     friend_confirmed = {
#         "pal_id": pal_id.pet_id,
#         "video_id": new_rental.video_id,
#         "due_date": new_rental.due_date,
#         "videos_checked_out_count": videos_checked_out,
#         "available_inventory": video.total_inventory
#         }
#     return jsonify(rental_receipt), 200
