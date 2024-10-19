# Coride - Flask REST API with MongoDB

This is a Flask-based REST API that interacts with a MongoDB database. The API is Dockerized using Docker and `docker-compose` for easy setup and management. It provides endpoints to handle user data (CRUD operations).

## Features
- **GET /users**: Fetch all users from the MongoDB database.
- **POST /users**: Add a new user with `name`, `email`, and `password`.
- **GET /users/<id>**: Fetch a user by ID.
- **PUT /users/<id>**: Update an existing user's details by ID.
- **DELETE /users/<id>**: Delete a user by ID.

## Prerequisites

- Docker
- Docker Compose

## How to Set Up the Application

### Step 1: Clone the repository

```bash
git clone https://github.com/ArunMandava3030/Coride.git
cd Coride
