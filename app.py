from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

testDB = {
    1:{'name':'Clean car'},
    2:{'name':'Write blog'},
    3:{'name':'Start stream'},
}

class Items(Resource):
    def get(self):
        return testDB
    def post(self):
        data = request.json
        itemId = len(testDB.keys()) + 1
        testDB[itemId] = {'name':data['name']}
        return testDB

class Item(Resource):
    def get(self,pk):
        return testDB[pk]

api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>')

# Basic route
# @app.route('/')
# def hello():
#     return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)