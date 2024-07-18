import boto3
import redis
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from flask import current_app as app

def upload_image(data):
    s3 = boto3.client('s3', aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'], aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'])
    redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
    
    image = data['image']
    blog_id = redis_client.lpop('image_queue')
    if blog_id:
        s3.upload_fileobj(image, app.config['AWS_BUCKET_NAME'], image.filename)
        
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        metadata = MetaData(bind=engine)
        blogs = Table('blog_post', metadata, autoload=True)
        stmt = blogs.update().where(blogs.c.id == blog_id).values(image_uploaded=True)
        session = sessionmaker(bind=engine)()
        session.execute(stmt)
        session.commit()
    return {'message': 'Image uploaded successfully'}, 200
