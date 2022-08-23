from fastapi import APIRouter

inicial_routes = APIRouter(
    prefix="/home",
    tags=["Home"],
)


@inicial_routes.get("/")
async def home():
    return {"Twitter API": "Working - Index"}
