from fastapi import APIRouter, Depends
from fastapi import HTTPException
from fastapi import status
from .schemas import CategoryCreate, CategoryRead
from .service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("")
async def add_category(category: CategoryCreate = Depends()) -> CategoryRead:
    category = await CategoryService.insert_document(category)
    if not category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return category


@router.get("")
async def get_categories() -> list[CategoryRead]:
    return await CategoryService.get_all()
