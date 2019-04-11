import re
from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)
todos = {}
parser = reqparse.RequestParser()
parser.add_argument('url')


class Short(Resource):

    def delete(self):
        todos.clear()
        return None, 204

    def get(self):
        return todos, 200

    def post(self):
        arguments = parser.parse_args()
        url = arguments['url']

        if not checking_url_validity(url):
            return "URL is invalid", 400
        if not url:
            return "Arguments are invalid", 400
        for id, i in list(todos.items()):
            if i == url:
                return str(id), 201

        id = shorten_url(url)
        return str(id), 201


class Short_identification(Resource):

    def delete(self, id):
        if id not in todos:
            return None, 404
        todos.pop(id)
        return None, 204

    def get(self, id):
        if id not in todos:
            return None, 404
        return todos[id], 301

    def put(self, id):
        if id not in todos:
            return None, 404
        arguments = parser.parse_args()
        url = arguments['url']

        if not checking_url_validity(url):
            return "URL is invalid", 400
        if not url:
            return "Arguments are invalid", 400
        todos[id] = url
        return None, 200


def shorten_url(url):
    url_keys = todos.keys()
    length = 0

    if len(url_keys) != 0:
        length = int(max(url_keys, key=int))

    todos[str(length+1)] = url
    return length


def checking_url_validity(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)


api.add_resource(Short, '/')
api.add_resource(Short_identification, '/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)