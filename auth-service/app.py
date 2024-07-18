from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from auth_service.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from auth_service.views.auth_views import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
