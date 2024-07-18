from blog_service.models.blog_post import BlogPost
from blog_service.app import db, redis_client
import jwt
from flask import current_app as app

def token_required(f):
    def wrap(*args, **kwargs):
        token = kwargs.get('token')
        if not token:
            return {'message': 'Token is missing'}, 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return {'message': 'Token is invalid'}, 401
        return f(data['user_id'], *args, **kwargs)
    return wrap

@token_required
def create_blog(user_id, data):
    new_post = BlogPost(title=data['title'], content=data['content'], user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    if 'image_id' in data:
        redis_client.rpush('image_queue', new_post.id)
    return {'message': 'Blog post created'}, 201

@token_required
def update_blog(user_id, blog_id, data):
    blog = BlogPost.query.get(blog_id)
    if blog.user_id != user_id:
        return {'message': 'Permission denied'}, 403
    blog.title = data['title']
    blog.content = data['content']
    db.session.commit()
    if 'image_id' in data:
        redis_client.rpush('image_queue', blog.id)
    return {'message': 'Blog post updated'}, 200

@token_required
def delete_blog(user_id, blog_id):
    blog = BlogPost.query.get(blog_id)
    if blog.user_id != user_id:
        return {'message': 'Permission denied'}, 403
    db.session.delete(blog)
    db.session.commit()
    return {'message': 'Blog post deleted'}, 200
