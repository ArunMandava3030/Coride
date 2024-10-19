import os

from flask import Flask
from flask_restful import Api
from mongo import mongo  # Import mongo from the new mongo.py
from resources.user_resources import UserListResource, UserResource

def create_app():
    app = Flask(__name__)
    # Use environment variable for MONGO_URI
    app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost:27017/myDatabase')  
    mongo.init_app(app)

    api = Api(app)
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<id>')

    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
