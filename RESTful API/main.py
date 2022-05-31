from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api =Api()

data = {
    1: {"name": "RESTful API", "num": "44"},
    2: {"name": "Python training", "num": "22"},
    3: {"name": "Flask framework", "num": "53"}
}

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("num", type=int)

class Main(Resource):

    def get(self, data_id):
        if data_id == 0:
            return data
        else:
            return data [data_id]

    def delete(self, data_id):
        del data [data_id]   
        return data

    def post(self, data_id): 
        data[data_id] = parser.parse_args()
        return data

    def put(self, data_id):
        data[data_id] = parser.parse_args()
        return data

api.add_resource(Main, "/api/data/<int:data_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug= True, port=3000, host="127.0.0.1")