# restapi.py
# Flask REST API: User Manager

## Description:
This is a basic RESTful API using Flask that allows you to create, read, update, and delete (CRUD) users using HTTP methods.

## Tools Used:
- Python
- Flask
- Postman

## Endpoints:
- GET /users → Get all users
- GET /users/<id> → Get specific user
- POST /users → Add new user
- PUT /users/<id> → Update user
- DELETE /users/<id> → Delete user

## How to Run:
1. Install Flask: `pip install flask`
2. Run: `python app.py`
3. Test using Postman at `http://127.0.0.1:5000`
