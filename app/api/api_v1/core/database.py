from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from .settings import settings
from ..categories.models import Category


class DBHelper:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.mongodb_conn_string)
        self.database = self.client[settings.DB_NAME]

    async def init_database(self):
        await init_beanie(
            database=self.database,
            document_models=[Category],
        )

    async def close_database(self):
        self.database.close()


db_helper = DBHelper()
