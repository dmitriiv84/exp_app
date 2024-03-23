from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class BaseCategory(BaseModel):
    category_name: str


class CategoryCreate(BaseCategory):
    pass


class CategoryRead(BaseCategory):
    id: PydanticObjectId = Field()
