from fastapi import FastAPI

from endpoints.inicial import inicial

app = FastAPI()

app.include_router(inicial)