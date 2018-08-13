from flask_restful import Resource, request


class Posts(Resource):
    def get(self):
        print(request.args)
        return {'hello': 'world'}

    def post(self):
        return {'status': True}