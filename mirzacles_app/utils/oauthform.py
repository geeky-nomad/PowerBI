from fastapi import Form
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import SecretStr


class CustomOAuth2PasswordRequestForm(OAuth2PasswordRequestForm):
    """
    This class overrides the OAuth2PasswordRequestForm class and keep only username and password
    """

    def __init__(self,  username: str = Form(...), password: SecretStr = Form(...)):
        super().__init__(grant_type="", username=username,
                         password=password, scope="", client_id="", client_secret="")
