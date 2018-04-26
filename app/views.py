from flask_restful import Resource, reqparse
from models import Admin





class Administrator(Resource):
    def __init__(self):
        self.restaurant = {}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username")
        parser.add_argument("password")
        parser.add_argument("confirm_password")
        args = parser.parse_args()

        username = args["username"]
        password = args["password"]
        confirm_password = args["confirm_password"]

        if username in self.restaurant.keys():
            return ({"message":"Username already exists"}), 400

        if password == confirm_password:
            new_admin = Admin(username, password)
            self.restaurant[username] = new_admin
            
            return ({"message":"User created"}), 201

        return ({"message":"Passwords don't match"}), 400

