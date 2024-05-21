from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str
    active: str
    email: str
    hashed_password: str


class LoginInUserInfo(BaseModel):
    username: str
    firstname: str
    lastname: str
    email: str
    created_at: str
