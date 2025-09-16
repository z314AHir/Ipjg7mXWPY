# 代码生成时间: 2025-09-17 03:42:47
# authentication_app/__init__.py
# 初始化模块

# authentication_app/apps.py
from django.apps import AppConfig

class AuthenticationAppConfig(AppConfig):
    name = 'authentication_app'

# authentication_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

"""
自定义用户模型，继承自AbstractUser
"""
class CustomUser(AbstractUser):
    # 可以根据需要添加额外的字段
    pass

# authentication_app/views.py
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser

"""
用户认证视图
"""
class UserAuthenticationView(View):
    def post(self, request):
        """
        处理用户登录请求
        """
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return JsonResponse({'error': 'Both username and password are required'}, status=400)
        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
        login(request, user)
        return JsonResponse({'message': 'Login successful'}, status=200)

    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        """
        处理用户登出请求
        """
        # 这里可以添加登出逻辑，如：logout(request)
        return JsonResponse({'message': 'Logout successful'}, status=200)

# authentication_app/urls.py
from django.urls import path
from .views import UserAuthenticationView

"""
URL配置
"""
urlpatterns = [
    path('login/', UserAuthenticationView.as_view(), name='login'),
    path('logout/', UserAuthenticationView.as_view(), name='logout'),
]

# authentication_app/admin.py
from django.contrib import admin
from .models import CustomUser

"""
自定义用户模型的Admin界面
"""
admin.site.register(CustomUser)