from flask import Blueprint, request
from flask_restplus import Api, Resource

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: TODOS[todo_id]}

    def put(self, todo_id):
        TODOS[todo_id] = request.form['data']
        return {todo_id: TODOS[todo_id]}

@api.route('/all')
class TodoSimple(Resource):
    def get(self):
        return TODOS

