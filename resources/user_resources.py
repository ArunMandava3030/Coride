from flask_restful import Resource, reqparse
from bson.objectid import ObjectId
from mongo import mongo  # Import the initialized mongo object

# UserListResource handles all users
class UserListResource(Resource):
    def get(self):
        # Retrieve all users from MongoDB
        users = mongo.db.users.find()
        return [{'id': str(user['_id']), 'name': user['name'], 'email': user['email']} for user in users], 200

    def post(self):
        # Define and parse request arguments for user creation
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help="Name cannot be blank")
        parser.add_argument('email', required=True, help="Email cannot be blank")
        parser.add_argument('password', required=True, help="Password cannot be blank")
        args = parser.parse_args()

        # Insert a new user into MongoDB
        user_id = mongo.db.users.insert_one({
            'name': args['name'],
            'email': args['email'],
            'password': args['password']  # Consider hashing the password
        }).inserted_id

        return {'id': str(user_id)}, 201

# UserResource handles a single user identified by `user_id`
class UserResource(Resource):
    def get(self, user_id):
        # Retrieve a user by ID from MongoDB
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            return {'id': str(user['_id']), 'name': user['name'], 'email': user['email']}, 200
        return {'message': 'User not found'}, 404

    def put(self, user_id):
        # Parse request arguments for updating user information
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=False)
        parser.add_argument('email', required=False)
        parser.add_argument('password', required=False)
        args = parser.parse_args()

        # Build update fields dynamically
        update_fields = {}
        if args['name']:
            update_fields['name'] = args['name']
        if args['email']:
            update_fields['email'] = args['email']
        if args['password']:
            update_fields['password'] = args['password']  # Consider hashing the password

        # Update the user document in MongoDB
        result = mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': update_fields})

        if result.matched_count:
            return {'message': 'User updated successfully'}, 200
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        # Delete a user by ID from MongoDB
        result = mongo.db.users.delete_one({'_id': ObjectId(user_id)})

        if result.deleted_count:
            return {'message': 'User deleted successfully'}, 200
        return {'message': 'User not found'}, 404
