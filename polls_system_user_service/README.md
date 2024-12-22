# Polls System - User Service

## Description
The service is responsible for managing users in the system:
- Create a new user
- Update user information
- Delete user information
- Get user information
- Get all users information


## API Endpoints
- **GET** `/users` - Get all users
- **GET** `/users/{user_id}` - Get user by id
- **GET** `/users/{user_id}/is_registered` - Get user's registration status
- **POST** `/users` - Create a new user
- **PUT** `/users/{user_id}` - Update user information by user_id
- **PUT** `/users/register/{user_id}` - Register an existing user by user_id
- **DELETE** `/users/{userId}` - Delete a user by user_id


## Get Started

1. Clone the repository
2. run `pip install -r requirements.txt` to install dependencies
3. run `docker-compose up -d` to build the docker image for db and poll service
4. to run the service locally run `uvicorn app.main:app --reload` command
