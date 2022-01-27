from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.method in permissions.SAFE_METHODS:
            return True
        return account.author == request.user