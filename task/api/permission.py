from rest_framework import permissions

class ReadOnlyOrAdminPermission(permissions.BasePermission):
    """
    Custom permission to allow read-only access to all users and full access to administrators.
    """

    def has_permission(self, request, view):
        # Allow all users to perform GET requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow only administrators to perform PUT and POST requests
        return request.user and request.user.is_staff