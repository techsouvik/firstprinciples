from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from blog_service.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

from blog_service.views.blog_views import blog_bp
app.register_blueprint(blog_bp, url_prefix='/blog')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
