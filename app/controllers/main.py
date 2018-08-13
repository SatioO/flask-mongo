from flask import Blueprint, jsonify, make_response, request

main = Blueprint('main', __name__, url_prefix='/api/v1')


@main.route('/', methods=['GET', 'POST'])
def root():
    return make_response(jsonify({'status': True}), 200)
