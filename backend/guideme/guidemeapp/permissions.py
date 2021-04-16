from rest_framework import permissions

# Accessibilité User :
#       All   : list, create, auth, retrieve
#       Owner : update, partial_update,
#       Staff : update, partial_update, destroy
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

# Accessibilité Activity :
#       All           : list, area, ratings, types, retrieve
#       Authenticated : user, create
#       Owner         : update, partial_update, destroy
#       Staff         : update, partial_update, destroy
class ActivityPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'area', 'ratings', 'types']:
            return True
        elif view.action in ['user', 'create']:
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

# Accessibilité Type :
#       All           : list, retrieve
#       Staff         : create, update, partial_update, destroy
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

# Accessibilité Rating :
#       All           : list, retrieve
#       Authenticated : create
#       Owner         : update, partial_update, destroy
#       Staff         : update, partial_update, destroy
class RatingPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list']:
            return True
        elif view.action in ['create']:
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