from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it
    Assumes the model instance has an 'owner' attribute
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named 'owner'
        return obj.owner == request.user


class IsTaskOwner(BasePermission):
    """
    Object-level permission to only allow owners and assignees of an object to edit it
    Assumes the model instance has 'owner' and 'assignee' attribute
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user or request.user in obj.assignee
