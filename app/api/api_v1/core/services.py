class BaseService:
    model = None

    @classmethod
    async def insert_document(cls, data):
        await cls.model.insert_one(data)
