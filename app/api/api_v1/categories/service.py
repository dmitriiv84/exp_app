from app.api.api_v1.categories.models import Category
from app.api.api_v1.categories.schemas import CategoryCreate, CategoryRead
from beanie import WriteRules


class CategoryService:
    @classmethod
    async def insert_document(cls, category_create: CategoryCreate):
        category = Category(**category_create.model_dump(mode="json"))
        await category.insert(link_rule=WriteRules.WRITE)
        print(type(category))
        return category

    @classmethod
    async def get_all(cls):
        return await Category.find_all().to_list()


# @app.post("/person", response_model=PersonRead)
