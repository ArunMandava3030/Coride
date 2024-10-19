# Coride - Flask REST API with MongoDB Integration

## Overview

Coride is a simple RESTful API built using Flask and MongoDB. This project allows users to perform basic CRUD (Create, Read, Update, Delete) operations on user data. The application is containerized using Docker and can be easily set up using Docker Compose.

## Features

- **Create a User (POST /users)**: Add a new user with a name, email, and password.
- **Get All Users (GET /users)**: Retrieve all users from the database.
- **Get a Single User (GET /users/<id>)**: Retrieve a specific user by their MongoDB ObjectID.
- **Update a User (PUT /users/<id>)**: Update an existing user’s information by their ID.
- **Delete a User (DELETE /users/<id>)**: Delete a user by their ID.

## Project Structure

Coride/
│
├── app.py
├── mongo.py
├── resources/
│   └── user_resources.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── tests/
    └── postman_screenshots/
## Prerequisites

Before you begin, ensure that the following are installed on your development machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)
##
Setup and Run the Application


To get up and running with this project on your own local machine, follow these steps:

### Step 1: Clone the Repository

Clone the repository from Github

```bash
git clone https://github.com/ArunMandava3030/Coride.git
cd Coride
Step 2: Build and Run the Docker Containers

Using Docker Compose build and run the application with MongoDB:
```
The Flask API will be available at http://localhost:5000.
MongoDB will be running inside the container, and that will be already bound to Flask.
Step 3: API Endpoints
After launching all the containers are running. Using Postman, Curl, or any other HTTP client, the following API endpoints can be interacted with:
 GET /users Fetch all the users from MongoDB.
Example:
ssh user@localhost
Copy code
curl -X GET http://localhost:5000/users
POST /users Creates new users in the database.
Request body:
json
Copy code
{
    "name": "John Doe",
"email": "john@example.com",
  "password": "password123"
}
GET /users/<id>
Get a user by MongoDB ObjectID.
 
Example
 
bash
Copy code
curl -X GET http://localhost:5000/users/your_user_id_here
PUT /users/<id>
Update the current user details.
 
Request Body
 
json
Copy code
{
    "name": "John Smith",
    "email": "johnsmith@example.com"
}
DELETE /users/<id>
Delete a user from the database.
 
Example
 
bash
Copy code
curl -X DELETE http://localhost:5000/users/your_user_id_here
Docker Compose Details
The docker-compose.yml declares two services:
Flask App
Running the Python/Flask application.
MongoDB: A NoSQL database for user data.
Structure here:


yaml
Copy code
version: '3'

services:
  flask:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - mongo
  mongo:
    image: mongo:4.2
    ports:
      - "27017:27017"
    volumes:
- ./data/db:/data/db
How to Stop and Remove Containers
To stop the running containers run:
 
bash
Copy code
docker-compose down
This will stop both the Flask and MongoDB services and remove the containers.
 
Postman Test Cases Screenshots
Here are the screenshots of the API requests and responses sent using Postman:
 
1. POST /users - Create a New User
 
2. GET /users - Retrieve All Users

3. GET /users/<id> - Retrieve a Single User

4. PUT /users/<id> - Update a User

5. DELETE /users/<id> - Delete a User

Testing
You can test the API through the use of Postman. All screenshots are retained in the tests/postman_screenshots/ folder. The above structure of the API is followed in testing the CRUD operations.
If you're not using Docker, be certain the URI for MongoDB is set correctly in your app.py file. If everything is correct, this should allow the app to run with the local MongoDB instance inside the Docker container by default.

python
Copy code
app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"
If you're using Docker-based deployment, you don't need to change a thing because Docker Compose will handle the network between the Flask and MongoDB containers.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

yaml
Copy code

### Git Commands to Push the Code into GitHub

Follow the below steps to push the code into your GitHub repository:

1. **Navigate into your project directory**:

```bash
cd /path/to/Coride
Initialize Git (if not done already):
bash
Copy code
git init
Add your remote repository:
bash
Copy code
git remote add origin https://github.com/ArunMandava3030/Coride.git
Add all the files:
bash
Copy code
git add .
Commit your changes:
bash
Copy code
git commit -m "Initial commit for Coride Flask MongoDB API with Docker"
Push the changes into the GitHub repository:
bash
Copy code
END
git branch -M main  # If 'main' is the default branch
 git push -u origin main



