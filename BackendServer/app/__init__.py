import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from flask import Flask, render_template
from flask_compress import Compress
from flask_restplus import Api

app = Flask(__name__)
app.config.from_object('config')
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
Compress(app)


@app.route("/")
def visualize():
    return "use other routes"


@app.errorhandler(404)
def not_found(error):
    return "TODO: 404 page", error

from app.base_routes.routes import mod_data as dataModule
app.register_blueprint(dataModule)