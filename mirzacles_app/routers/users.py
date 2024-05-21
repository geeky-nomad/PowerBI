from fastapi import Depends, HTTPException, APIRouter, status, Request, Header

from utils.user import CurrentUser


router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/me")
async def user_me(request: Request, token: str = Header()):
    """
    This api is used to return current user information from the record
    if user has required permission
    """
    user = CurrentUser(request, token)
    current_user = user.get_current_user()
    if not current_user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")
    return CurrentUser.get_user_info(current_user.username)


@router.get("/all")
async def get_users(request: Request, token: str = Header()):
    """
    This api is used to return all user details from the record
    if user has required permission
    """
    return CurrentUser.get_all_user_info()
