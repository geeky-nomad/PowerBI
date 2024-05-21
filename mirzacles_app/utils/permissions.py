from fastapi import HTTPException, status

from models.users import permissions_db
from utils.user import CurrentUser


class Permission:
    """
    The permission class is used the check the permission of user for the different route groups
    """

    def __init__(self, router=None, request=None, token=None):
        self.router = router
        self.request = request
        self.token = token

    def get_permissions(self):
        user = CurrentUser(self.request, self.token)
        current_user = user.get_current_user()
        for permissions in permissions_db:
            permission = permissions_db[permissions]
            if permission.get('user_id', None) == current_user.id:
                return permission.get('permissions', None)
        return []

    def check_permission(self):
        permissions = self.get_permissions()
        if self.router not in permissions:
            return False
        return True
