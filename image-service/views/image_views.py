from flask import Blueprint, request, jsonify
from image_service.controllers.image_controller import upload_image

image_bp = Blueprint('image_bp', __name__)

@image_bp.route('/upload', methods=['POST'])
def upload():
    data = request.files
    return jsonify(upload_image(data))
