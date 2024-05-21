from fastapi import FastAPI

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel


fake_token = "faslkfjlskf8989lkjsad2"


fake_users_db = {
    "johndoe": {
        "id": 1,
        "username": "johndoe",
        "firstname": "john",
        "lastname": "doe",
        "password": "hello@123",
        "email": "johndoe@mailinator.com",
        "active": True,
        "created_at": "2022-11-25"
    },
}

app = FastAPI()


class Login(BaseModel):
    username: str
    password: str


class Logout(BaseModel):
    token: str


@app.post("/login", response_model=Login)
async def login(login: Login):
    if login.username not in fake_users_db.get('johndoe').get('username'):
        raise HTTPException(status_code=401, detail="Incorrect username")
    if login.password not in fake_users_db.get('johndoe').get('password'):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return {'username': login.username, 'password': login.password}


@app.post("/logout", response_model=Logout)
async def logout(logout: Logout):
    if logout.token != fake_token:
        raise HTTPException(status_code=401, detail="Authentication required")
    return {"token": ""}
