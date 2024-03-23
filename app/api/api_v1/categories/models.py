from beanie import Document
from beanie import Indexed
import pymongo


class Category(Document):
    category_name: Indexed(str, pymongo.ASCENDING)

    class Settings:
        name = "categories"
        schema_extra = {"category_name": "Category"}
