from fastapi import HTTPException, status

from models.users import users_db
from utils.user_basemodel import User, LoginInUserInfo


class CurrentUser:
    """

    This will give information about logged in user
    """

    def __init__(self, request, token):
        self.request = request
        self.token = token

    @staticmethod
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return User(**user_dict)

    def get_current_user(self):
        username = self.request.cookies.get(self.token, None)

        if username:
            user = CurrentUser.get_user(users_db, username)
            if user:
                return user
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

    @staticmethod
    def get_user_info(username: str):
        if username in users_db:
            user_dict = users_db[username]
            return LoginInUserInfo(**user_dict)

    @staticmethod
    def get_all_user_info():
        users = [LoginInUserInfo(**users_db[user]) for user in users_db]
        return users


    @staticmethod
    def check_valid_user(username):
        if username:
            user = CurrentUser.get_user(users_db, username)
            if user:
                return True
        return False
