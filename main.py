from fastapi import FastAPI

from endpoints.inicial_routes import inicial_routes
from endpoints.users_routes import users_routes
from endpoints.tweets_routes import tweets_routes

app = FastAPI()

app.include_router(inicial_routes)
app.include_router(users_routes)
app.include_router(tweets_routes)
