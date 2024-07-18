from flask import Flask
from image_service.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from image_service.views.image_views import image_bp
app.register_blueprint(image_bp, url_prefix='/image')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
