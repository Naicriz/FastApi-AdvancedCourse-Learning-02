# Python
from typing import List

# FastAPI
from fastapi import APIRouter

from models import User, UserUpdate

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


# Register user
@user_router.post(path="/signup",
                  response_model=User,
                  status_code=201,
                  summary="Register a new user")
async def signup():
    """
    Signup

    This path operation will register a new user in the application.

    Parameters:
        - Request Body: user: UserRegister

    
    Returns a json with the basic user information.
        - user_id: UUID
            - first_name: str
            - last_name: str
            - birth_date: str
            - email: str
            - username: str
            - password: str
    """
    pass


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
                 response_model=UserUpdate,
                 status_code=200,
                 summary="Update a user")
async def update_user():
    pass
