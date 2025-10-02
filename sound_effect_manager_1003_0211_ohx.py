# 代码生成时间: 2025-10-03 02:11:28
from django.db import models
from django.http import JsonResponse
# TODO: 优化性能
from django.views import View
from django.urls import path
# 改进用户体验
from django.core.exceptions import ObjectDoesNotExist
# FIXME: 处理边界情况
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# 扩展功能模块
from django.shortcuts import render, get_object_or_404
import json
import os

# Models
class SoundEffect(models.Model):
    """
    Model representing a sound effect.
    """
    name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# NOTE: 重要实现细节

    def __str__(self):
        return self.name

# Views
class SoundEffectList(View):
    """
    View to handle listing and searching sound effects.
    """
    def get(self, request):
# TODO: 优化性能
        """
        Returns a list of all sound effects.
        """
        sound_effects = SoundEffect.objects.all()
        return JsonResponse(list(sound_effects.values()), safe=False)

    def post(self, request):
        """
        Creates a new sound effect.
        """
        data = json.loads(request.body)
# NOTE: 重要实现细节
        SoundEffect.objects.create(
            name=data['name'],
            file_path=data['file_path']
        )
# 扩展功能模块
        return JsonResponse({'message': 'Sound effect created successfully'}, status=201)

class SoundEffectDetail(View):
    """
    View to handle getting, updating, and deleting a sound effect.
    """
    def get_object(self, id):
        """
        Attempts to retrieve a sound effect by ID.
        """
        try:
            return SoundEffect.objects.get(pk=id)
        except ObjectDoesNotExist:
            return None

    def get(self, request, id):
# 改进用户体验
        """
        Returns the details of a specific sound effect.
# 增强安全性
        """
        sound_effect = self.get_object(id)
        if sound_effect is not None:
            return JsonResponse(sound_effect.values(), safe=False)
        else:
            return JsonResponse({'error': 'Sound effect not found'}, status=404)

    @method_decorator(csrf_exempt, name='dispatch')
    def put(self, request, id):
# 优化算法效率
        """
        Updates an existing sound effect.
# TODO: 优化性能
        """
        sound_effect = self.get_object(id)
        if sound_effect is not None:
            data = json.loads(request.body)
            sound_effect.name = data.get('name', sound_effect.name)
            sound_effect.file_path = data.get('file_path', sound_effect.file_path)
            sound_effect.save()
            return JsonResponse(sound_effect.values(), safe=False)
        else:
            return JsonResponse({'error': 'Sound effect not found'}, status=404)

    @method_decorator(csrf_exempt, name='dispatch')
# 添加错误处理
    def delete(self, request, id):
        """
        Deletes a sound effect.
        """
        sound_effect = self.get_object(id)
        if sound_effect is not None:
            sound_effect.delete()
            return JsonResponse({'message': 'Sound effect deleted successfully'}, status=204)
        else:
            return JsonResponse({'error': 'Sound effect not found'}, status=404)

# URLs
urlpatterns = [
    path('sound-effects/', SoundEffectList.as_view(), name='sound-effect-list'),
    path('sound-effects/<int:id>/', SoundEffectDetail.as_view(), name='sound-effect-detail'),
]

# Note: Make sure to include this application in your Django project's settings.py file.
# Also, don't forget to create migrations and migrate your database after adding or modifying models.
# Additionally, ensure that your Django app is properly configured in urls.py.