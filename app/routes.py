from flask import Blueprint, request, jsonify, make_response
from app import db 
from app.models.pet import Pet
from app.models.friendship import Friendship



pet_bp = Blueprint("pet", __name__, url_prefix="/pet")
friendship_bp = Blueprint("friendship", __name__, url_prefix="/friendship")


@pet_bp.route("", methods=["POST"])
def create_a_profile():
    request_body = request.get_json()
    