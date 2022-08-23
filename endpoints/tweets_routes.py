# Python
from typing import List

# FastAPI
from fastapi import APIRouter

from models.tweet import Tweet

tweets_routes = APIRouter(
    prefix="/tweets",
    tags=["Tweets"],
)


# Show all tweets
@tweets_routes.get(path="/",
                   response_model=List[Tweet],
                   status_code=200,
                   summary="Show all tweets")
async def show_all_tweets():
    pass


# Post a tweet
@tweets_routes.post(path="/post",
                    response_model=Tweet,
                    status_code=201,
                    summary="Post a tweet")
async def post_tweet():
    pass


# Show a tweet by ID
@tweets_routes.get(path="/{tweet_id}",
                   response_model=Tweet,
                   status_code=200,
                   summary="Show a tweet")
async def show_tweet():
    pass


# Delete a tweet by ID
@tweets_routes.delete(path="/{tweet_id}/delete",
                      response_model=Tweet,
                      status_code=200,
                      summary="Delete a tweet")
async def delete_tweet():
    pass


# Update a tweet by ID
@tweets_routes.put(path="/{tweet_id}/delete",
                   response_model=Tweet,
                   status_code=200,
                   summary="Update a tweet")
async def update_tweet():
    pass
