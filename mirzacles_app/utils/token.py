import uuid

from utils.user import CurrentUser


class Token:
    """
    Token class is used to generate token and verify token
    """
    @staticmethod
    def get_token():
        return uuid.uuid4().hex

    @staticmethod
    def check_token(request, token):
        username = request.cookies.get(token, None)
        return CurrentUser.check_valid_user(username)
