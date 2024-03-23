from fastapi import HTTPException

from app.api.api_v1.categories.models import Category
from app.api.api_v1.categories.schemas import CategoryCreate, CategoryRead
from beanie import WriteRules
from beanie.odm.fields import PydanticObjectId


class CategoryService:
    @classmethod
    async def insert_document(cls, category_create: CategoryCreate):
        category = Category(**category_create.model_dump(mode="json"))
        await category.insert(link_rule=WriteRules.WRITE)
        print(type(category))
        return category

    @classmethod
    async def get_all(cls) -> list[CategoryRead]:
        return await Category.find_all().to_list()

    @classmethod
    async def delete_category(cls, category_id: PydanticObjectId):
        record = await cls.get_category_by_id(category_id)

        if not record:
            raise HTTPException(status_code=404, detail="Category record not found!")

        await record.delete()
        return {"message": "Record deleted successfully"}

    @classmethod
    async def get_category_by_id(cls, category_id: PydanticObjectId):
        category = await Category.get(category_id)
        return category

    @classmethod
    async def update_category(
        cls, category_id: PydanticObjectId, category: CategoryRead
    ):
        category = {k: v for k, v in category.dict().items() if v is not None}
        update_query = {"$set": {field: value for field, value in category.items()}}
        cat = await cls.get_category_by_id(category_id)
        if not cat:
            raise HTTPException(status_code=404, detail="Category record not found!")
        await cat.update(update_query)
