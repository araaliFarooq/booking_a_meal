from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from views import Administrator
api.add_resource(Administrator, "/app/v1/auth/signup")

