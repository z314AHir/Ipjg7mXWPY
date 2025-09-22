# 代码生成时间: 2025-09-22 14:49:28
from django.db import models
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import path
from django.views import View
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

"""
Permission Management App for Django.
Handles user permissions and access control.
"""

# Models
class Permission(models.Model):
    """
    Represents a permission that can be assigned to a user.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Return a string representation of the permission.
        """
        return self.name

class UserRole(models.Model):
    """
    Represents a role with a set of permissions.
    """
    name = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField(Permission, related_name='user_roles')

    def __str__(self):
        """
        Return a string representation of the user role.
        """
        return self.name

# Views
class PermissionListView(View):
    """
    Provides a list of permissions for a user.
    """
    login_required

    def get(self, request, *args, **kwargs):
        """
        Handle GET request and return permissions list.
        """
        try:
            permissions = Permission.objects.all()
            permission_data = [{'id': perm.id, 'name': perm.name} for perm in permissions]
            return JsonResponse({'permissions': permission_data}, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class AssignPermissionView(View):
    """
    Assigns a permission to a user.
    """
    login_required

    def post(self, request, *args, **kwargs):
        """
        Handle POST request to assign a permission.
        """
        try:
            user_id = request.POST.get('user_id')
            permission_id = request.POST.get('permission_id')
            user = User.objects.get(id=user_id)
            permission = Permission.objects.get(id=permission_id)
            user.user_permissions.add(permission)
            return JsonResponse({'message': 'Permission assigned successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# URLs
urlpatterns = [
    path('permissions/', PermissionListView.as_view(), name='permission_list'),
    path('assign_permission/', AssignPermissionView.as_view(), name='assign_permission'),
]
