from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Only the post author can update or delete.
    Others can read only
    """
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS: GET, HEAD, OPTIONS => always allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        # PUT/PATCH/DELETE => only author
        return obj.author == request.user
