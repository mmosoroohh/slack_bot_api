from flask_api import FlaskAPI
from config.env import app_env
from app.utils.slackhelper import SlackHelper
from flask import request, jsonify
from app.actions import Actions
from re import match

allowed_commands = [
    'show-task'
    'show-tasks'
    'my-task'
    'my-tasks'
    'activo'
]

def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')

    @app.route("/activo", methods=["POST"])
    def activo_bot():
        return "Welcome to Activo \n\n Please your center to continue..."

    return app
