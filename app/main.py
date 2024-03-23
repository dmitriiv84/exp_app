from fastapi import FastAPI

from app.api.api_v1.core.database import db_helper
from app.api.api_v1.categories.router import router as categories_router

app = FastAPI()
app.include_router(categories_router)


@app.on_event("startup")
async def startup_event():
    await db_helper.init_database()


@app.on_event("shutdown")
async def shutdown_event():
    await db_helper.close_database()
