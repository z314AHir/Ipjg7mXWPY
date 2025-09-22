# 代码生成时间: 2025-09-23 01:14:22
from django.db import models
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.urls import path
from django.core.exceptions import ObjectDoesNotExist
import json

"""
A Django application component for a message notification system.
"""

class Notification(models.Model):
    """
    A model to store notifications.
# TODO: 优化性能
    """
    title = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    # Add any additional methods or properties as needed


@require_http_methods(['POST'])
def create_notification(request):
    """
    A view to create a new notification.
    """
    try:
        data = json.loads(request.body)
        title = data.get('title')
        message = data.get('message')
        recipient_id = data.get('recipient_id')
        
        if not all([title, message, recipient_id]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        
        recipient = User.objects.get(id=recipient_id)
# 优化算法效率
        notification = Notification.objects.create(title=title, message=message, recipient=recipient)
        return JsonResponse({'id': notification.id, 'title': notification.title}, status=201)
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Recipient not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
# 添加错误处理


urlpatterns = [
    path('create/', create_notification, name='create_notification'),
]

# You can add more URL patterns and views as needed
