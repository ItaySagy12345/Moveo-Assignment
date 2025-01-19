from fastapi import FastAPI
from routes.items_routes import items_router

app = FastAPI()

app.include_router(items_router, prefix="/api")