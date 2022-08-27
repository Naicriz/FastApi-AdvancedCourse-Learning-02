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
        # load the json file into a list of dicts (results)
        results = json.load(f)
        # convert the user object to a dict (user_dict)
        user_dict = user.dict()
        # append the user_dict to the results list of dicts (results)
        results.append(user_dict)
        # set the file cursor to the beginning of the file
        f.seek(0)
        # dump the results list of dicts to the json file
        json.dump(results, f, default=str, indent=4)


'''
@deprecated
#    with open("utils/users.json", "r+", encoding="utf_8") as f:
#        # List[User]
#        results = json.loads(f.read())
#        # Convert to dict
#        user_dict = user.dict()
#        # UUID to str
#        user_dict["user_id"] = str(user_dict["user_id"])
#        # date to str
#        user_dict["birth_day"] = str(user_dict["birth_day"])
#        # Add new user to the list of users
#        results.append(user_dict)
#        # Go to the beginning of the file to overwrite it
#        f.seek(0)
#        # Write the new list to the file (json)
#        f.write(json.dumps(results))
'''


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
