from fastapi import FastAPI

from endpoints.inicial_routes import inicial_routes

app = FastAPI()

app.include_router(inicial_routes)
