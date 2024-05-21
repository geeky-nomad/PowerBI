from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from middleware.auth_middleware import AuthenticationMiddleware
from routers import users, items, auth


app = FastAPI()

auth_middleware = AuthenticationMiddleware()
app.add_middleware(BaseHTTPMiddleware, dispatch=auth_middleware)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)
