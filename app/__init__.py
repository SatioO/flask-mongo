from flask import Flask, jsonify
from mongoengine import connect
from app.controllers import main


def connect_db(app):
    db_client = connect(
        host=app.config['DATABASE']['HOST'],
        port=app.config['DATABASE']['PORT'])

    return db_client


def create_app(app_env):
    app = Flask(__name__, instance_relative_config=True)
    # Load the default configuration
    app.config.from_object('config.' + app_env)
    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')

    db_client = connect_db(app)

    # HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"status": "Not Found"}), 404

    # register our blueprints
    app.register_blueprint(main)

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
