# 代码生成时间: 2025-09-16 15:15:22
from django.db import models
from django.http import JsonResponse
from django.views import View
from django.urls import path
import psutil
import os
import sys

# models.py
class MemoryUsage(models.Model):
    """
    Model to store memory usage data.
    """
    process_id = models.IntegerField(unique=True)
    memory_info = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MemoryUsage {self.process_id}"

# views.py
def get_memory_usage(self):
    """
    Get the memory usage of the current process.
    """
    process = psutil.Process()
    memory_info = process.memory_full_info()
    return memory_info.rss  # Resident Set Size in bytes

class MemoryUsageView(View):
    """
    A view to analyze memory usage.
    """
    def get(self, request):
        """
        Return the memory usage of the current process as JSON.
        """
        try:
            memory_usage = get_memory_usage()
            return JsonResponse(
                {
                    "memory_usage": memory_usage,
                },
                safe=False,
            )
        except Exception as e:
            return JsonResponse(
                {
                    "error": str(e),
                },
                status=500,
            )

# urls.py
urlpatterns = [
    path('memory_usage/', MemoryUsageView.as_view(), name='memory_usage'),
]
