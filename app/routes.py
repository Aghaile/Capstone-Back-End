from flask import Blueprint, request, jsonify, make_response
from app import db 
from app.models.pet import Pet


pet_bp = Blueprint("pet", __name__, url_prefix="/pet")