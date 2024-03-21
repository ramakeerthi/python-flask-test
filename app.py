from flask import Flask
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

api.add_resource(Items, '/')

# Basic route
# @app.route('/')
# def hello():
#     return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)