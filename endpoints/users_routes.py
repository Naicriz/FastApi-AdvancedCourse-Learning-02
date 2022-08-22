# Python
from typing import List

# FastAPI
from fastapi import APIRouter

from models.user import User

users_routes = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@users_routes.post(path="/signup",
                   response_model=User,
                   status_code=201,
                   summary="Register a new user")
async def signup():
    pass


@users_routes.post(path="/login",
                   response_model=User,
                   status_code=200,
                   summary="Login a user")
async def login():
    pass


@users_routes.get(path="/users",
                  response_model=List[User],
                  status_code=200,
                  summary="Show all users")
async def show_all_users():
    pass


@users_routes.get(path="/users/{user_id}",
                  response_model=User,
                  status_code=200,
                  summary="Show a user")
async def show_user():
    pass


@users_routes.delete(path="/users/{user_id}/delete",
                     response_model=User,
                     status_code=200,
                     summary="Delete a user")
async def delete_user():
    pass


@users_routes.put(path="/users/{user_id}/update",
                  response_model=User,
                  status_code=200,
                  summary="Update a user")
async def update_user():
    pass
