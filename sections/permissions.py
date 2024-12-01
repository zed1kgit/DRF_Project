from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = 'You are not a moderator'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsSuperuser(BasePermission):
    message = 'You are not a superuser'

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
