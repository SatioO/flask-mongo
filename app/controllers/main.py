from flask import Blueprint, jsonify, make_response

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return make_response(jsonify({'status': 'online'}), 200)
