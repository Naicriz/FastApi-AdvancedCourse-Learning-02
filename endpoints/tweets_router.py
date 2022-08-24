# Python
import json
from typing import List

# FastAPI
from fastapi import APIRouter, Body

from models import Tweet

tweet_router = APIRouter(
    prefix="/tweets",
    tags=["Tweets"],
)


# Show all tweets
@tweet_router.get(path="",
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
async def post_tweet(tweet: Tweet = Body(...)):
    """
    # **Post a Tweet**

    This endpoint/path operation allows you to post a tweet to the application.

    **Parameters:**\n
    Request Body:
    - `tweet: Tweet`

    **Returns:** A json with the basic user information;
    - `twet_id: UUID`
    - `content: str`
    - `created_at: datetime`
    - `updated_at: datetime`
    - `updated_by: User`
    - `birth_date: date`
    """
    with open("utils/tweets.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        tweet_dict = tweet.dict()
        results.append(tweet_dict)
        f.seek(0)
        json.dump(results, f, default=str, indent=4)


# Show a tweet by ID
@tweet_router.get(path="/{tweet_id}",
                  response_model=Tweet,
                  status_code=200,
                  summary="Show a tweet")
async def show_tweet():
    pass


# Delete a tweet by ID
@tweet_router.delete(path="/{tweet_id}",
                     response_model=Tweet,
                     status_code=200,
                     summary="Delete a tweet")
async def delete_tweet():
    pass


# Update a tweet by ID
@tweet_router.put(path="/{tweet_id}",
                  response_model=Tweet,
                  status_code=200,
                  summary="Update a tweet")
async def update_tweet():
    pass
