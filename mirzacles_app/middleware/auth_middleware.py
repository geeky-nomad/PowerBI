from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse

from utils.permissions import Permission
from utils.token import Token


class AuthenticationMiddleware:
    """
    Return the permission for a logged in user
    """

    async def __call__(self, request: Request, call_next):

        try:
            token = request.headers.get('token', None)
            request_path = request.scope['path']
            current_path = request_path.split("/")[1]
            if token and current_path != "logout":
                token_obj = Token()
                if not token_obj.check_token(request, token):
                    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                                        content={'detail': "Invalid token"})
                permission = Permission(current_path, request, token)
                check_permission = permission.check_permission()
                if not check_permission:
                    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN,
                                        content={'detail': "Permission denied"})
            response = await call_next(request)
            return response
        except HTTPException as exc:
            return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                content={'detail': "Something went wrong"})
