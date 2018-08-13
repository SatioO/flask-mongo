from flask import Flask
from flask_restful import Resource, Api
from mongoengine import connect
from app.controllers import Posts
from config import config_by_name


def connect_db(app):
    db_client = connect(
        host=app.config['DATABASE']['HOST'],
        port=app.config['DATABASE']['PORT'])

    return db_client


def create_app(app_env):
    app = Flask(__name__, instance_relative_config=True)
    # Load the default configuration
    app.config.from_object(config_by_name[app_env])

    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')

    db_client = connect_db(app)

    api = Api(app)

    # register our blueprints
    api.add_resource(Posts, '/posts')

    return app


# @app.errorhandler(404)
# def not_found(error):
#     return make_response(error, 404)

# @app.route("/")
# def root():
#     message = "online"
#     if request.json == None:
#         abort(404, message)

#     return make_response(jsonify({"status": message}), 200)
