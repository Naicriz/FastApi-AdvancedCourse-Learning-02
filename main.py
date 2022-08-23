from fastapi import FastAPI

from endpoints import inicial_router, user_router, tweet_router

app = FastAPI()

app.include_router(inicial_router)
app.include_router(user_router)
app.include_router(tweet_router)
