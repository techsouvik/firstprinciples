from flask import Blueprint, request, jsonify
from blog_service.controllers.blog_controller import create_blog, update_blog, delete_blog

blog_bp = Blueprint('blog_bp', __name__)

@blog_bp.route('/blog', methods=['POST'])
def create():
    token = request.headers.get('x-access-token')
    data = request.get_json()
    return jsonify(create_blog(token=token, data=data))

@blog_bp.route('/blog/<int:blog_id>', methods=['PUT'])
def update(blog_id):
    token = request.headers.get('x-access-token')
    data = request.get_json()
    return jsonify(update_blog(token=token, blog_id=blog_id, data=data))

@blog_bp.route('/blog/<int:blog_id>', methods=['DELETE'])
def delete(blog_id):
    token = request.headers.get('x-access-token')
    return jsonify(delete_blog(token=token, blog_id=blog_id))
