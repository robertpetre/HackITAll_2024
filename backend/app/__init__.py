from flask import Flask
from flask_cors import CORS
from .routes import routes
app = Flask(__name__)

CORS(app, supports_credentials=True)

app.register_blueprint(routes, url_prefix='/api')



