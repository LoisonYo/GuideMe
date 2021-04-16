from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'create', 'auth']:
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False

class ActivityPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'create', 'area', 'ratings', 'types']:
            return True
        if view.action in ['user']:
            return request.user.is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return obj.creator == request.user or request.user.is_staff
        else:
            return False

class TypePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list']:
            return True
        elif view.action in ['create']:
            return request.user.is_staff
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_staff
        else:
            return False

class RatingPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'create']:
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return obj.creator == request.user or request.user.is_staff
        else:
            return False