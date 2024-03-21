from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return self.name

taskFields = {
    'name': fields.String
}

class Items(Resource):
    @marshal_with(taskFields)
    def get(self):
        tasks = Task.query.all()
        return tasks
    
    @marshal_with(taskFields)
    def post(self):
        data = request.json
        task = Task(name=data['name'])
        db.session.add(task)
        db.session.commit()
        tasks = Task.query.all()
        return tasks

class Item(Resource):
    @marshal_with(taskFields)
    def get(self,pk):
        task = Task.query.filter_by(id=pk).first()
        return task
    
#     def put(self,pk):
#         data = request.json
#         testDB[pk]['name'] = data['name']
#         return testDB
    
#     def delete(self,pk):
#         del testDB[pk]
#         return testDB

api.add_resource(Items, '/')
# api.add_resource(Item, '/<int:pk>')

# Basic route
# @app.route('/')
# def hello():
#     return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)