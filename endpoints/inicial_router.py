from fastapi import APIRouter

inicial_router = APIRouter(
    prefix="/home",
    tags=["Home"],
)


@inicial_router.get("/")
async def home():
    return {"Twitter API": "Working - Index"}
