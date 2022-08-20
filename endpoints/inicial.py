from multiprocessing.spawn import import_main_path
from fastapi import APIRouter

inicial = APIRouter(
    prefix="/home",
    tags=["home"],
)

@inicial.get("/")
async def home():
    return {"message": "Hello World"}

