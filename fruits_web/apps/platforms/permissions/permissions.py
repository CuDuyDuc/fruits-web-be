from fruits_web.apps.platforms.permissions import permissions,UserRole

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool( request.user.is_authenticated and request.user.role == UserRole.ADMIN.value )

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role in [UserRole.USER.value, UserRole.ADMIN.value])

class IsShop(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool( request.user.is_authenticated and request.user.role in [UserRole.SHOP.value, UserRole.ADMIN.value])

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool( request.user.is_authenticated)
    