import datetime
from fastapi import Depends, HTTPException, APIRouter, status, Response, Request, Header

from models.users import users_db
from utils.oauthform import CustomOAuth2PasswordRequestForm
from utils.password import Password
from utils.token import Token
from utils.user import CurrentUser


router = APIRouter(tags=["Authentication"])


@router.post("/login")
async def user_login(request: Request, response: Response, form_data: CustomOAuth2PasswordRequestForm = Depends()):
    """
    This api is used for user logged in. It accepts username and password and return token
    """
    user = CurrentUser.get_user(users_db, form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username")
    password = Password(
        str((form_data.password).get_secret_value()), user.hashed_password)
    if not password.verify_password():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect password")
    token = Token()
    access_token = token.get_token()
    for token, username in request.cookies.items():
        if username == form_data.username:
            response.delete_cookie(token)
    response.set_cookie(key=access_token, value=form_data.username)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
async def user_logout(request: Request, response: Response, token: str = Header()):
    """
    This api is used to user logging out
    """
    if not request.cookies.get(token, None):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Authentication required")
    response.delete_cookie(token)
    return {"status_code": status.HTTP_200_OK, "message": "User logged out"}
