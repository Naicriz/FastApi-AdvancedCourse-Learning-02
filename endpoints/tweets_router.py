# Python
from typing import List

# FastAPI
from fastapi import APIRouter

from models import Tweet

tweet_router = APIRouter(
    prefix="/tweets",
    tags=["Tweets"],
)


# Show all tweets
@tweet_router.get(path="/",
                  response_model=List[Tweet],
                  status_code=200,
                  summary="Show all tweets")
async def show_all_tweets():
    pass


# Post a tweet
@tweet_router.post(path="/post",
                   response_model=Tweet,
                   status_code=201,
                   summary="Post a tweet")
async def post_tweet():
    pass


# Show a tweet by ID
@tweet_router.get(path="/{tweet_id}",
                  response_model=Tweet,
                  status_code=200,
                  summary="Show a tweet")
async def show_tweet():
    pass


# Delete a tweet by ID
@tweet_router.delete(path="/{tweet_id}/delete",
                     response_model=Tweet,
                     status_code=200,
                     summary="Delete a tweet")
async def delete_tweet():
    pass


# Update a tweet by ID
@tweet_router.put(path="/{tweet_id}/delete",
                  response_model=Tweet,
                  status_code=200,
                  summary="Update a tweet")
async def update_tweet():
    pass
