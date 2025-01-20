from fastapi import FastAPI
from src.routes.items_routes import items_router


app = FastAPI()

app.include_router(items_router, prefix="/api")