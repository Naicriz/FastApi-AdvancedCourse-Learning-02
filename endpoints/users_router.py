# Python
import json
from typing import List

# FastAPI
from fastapi import APIRouter, Body

from models import User, UserUpdateReg

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


# Register user
@user_router.post(path="/signup",
                  response_model=User,
                  status_code=201,
                  summary="Register a new user")
async def signup(user: UserUpdateReg = Body(...)):
    """
    # **Signup**

    This path operation will register a new user in the application.

    **Parameters:**\n
    Request Body:
    - `user: UserUpdateReg`

    Returns a json with the basic user information:
    - `user_id: uuid`
    - `email: emailstr`
    - `first_name: str`
    - `last_name: str`
    - `username: str`
    - `birth_date: date`
    """
    with open("utils/users.json", "r+", encoding="utf_8") as f:
        results = json.loads(f.read())  # List[User]
        user_dict = user.dict()  # dict
        user_dict["user_id"] = str(user_dict["user_id"])  # UUID to str
        user_dict["birth_day"] = str(user_dict["birth_day"])  # date to str
        results.append(user_dict)  # Add new user to the list
        f.seek(0)  # Go to the beginning of the file to overwrite it
        f.write(json.dumps(results))  # Write the new list to the file (json)


# Login user
@user_router.post(path="/login",
                  response_model=User,
                  status_code=200,
                  summary="Login a user")
async def login():
    pass


# Show all users
@user_router.get(path="",
                 response_model=List[User],
                 status_code=200,
                 summary="Show all users")
async def show_all_users():
    pass


# Show user by ID
@user_router.get(path="/{user_id}",
                 response_model=User,
                 status_code=200,
                 summary="Show a user")
async def show_user():
    pass


# Delete user by ID
@user_router.delete(path="/{user_id}",
                    response_model=User,
                    status_code=200,
                    summary="Delete a user")
async def delete_user():
    pass


# Update user by ID
@user_router.put(path="/{user_id}",
                 response_model=UserUpdateReg,
                 status_code=200,
                 summary="Update a user")
async def update_user():
    pass
