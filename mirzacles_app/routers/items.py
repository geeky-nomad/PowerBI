from fastapi import APIRouter, Depends, HTTPException, status, Request, Header

from models.items import items_db
from utils.items import Items


router = APIRouter(
    prefix="/items",
    tags=["Items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/all")
async def get_items(request: Request, token: str = Header()):
    """
    This api is used to return all items if user has access token
    and required permission
    """
    return Items.get_all_Item_info()


@router.get("/{item_id}")
async def get_item(request: Request, item_id: int, token: str = Header()):
    """
    This api is used to return specific item if user has access token
    and required permission
    """
    item_dict = items_db.get(item_id)
    if not item_dict:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item_dict
