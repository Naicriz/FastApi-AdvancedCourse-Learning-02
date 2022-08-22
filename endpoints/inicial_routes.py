from fastapi import APIRouter

inicial = APIRouter(
    prefix="/home",
    tags=["Home"],
)


@inicial.get("/")
async def home():
    return {"Twitter API": "Working - Index"}
