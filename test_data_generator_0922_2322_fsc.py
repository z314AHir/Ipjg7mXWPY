# 代码生成时间: 2025-09-22 23:22:52
from django.db import models
from django.views import View
from django.http import JsonResponse
from django.urls import path
from faker import Faker
import random
import string

# 定义一个模型用于存储测试数据
class TestItem(models.Model):
    """Model representing a test item."""
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# 创建一个视图用于生成测试数据
class TestDataGenerator(View):
    """View to generate test data for the TestItem model."""
    def get(self, request, *args, **kwargs):
        """Handle GET request to generate test data."""
        try:
            # 设置要生成的测试数据的数量
            num_items = int(request.GET.get('num', 10))
            # 实例化Faker对象
            fake = Faker()
            # 循环生成测试数据
            for _ in range(num_items):
                TestItem.objects.create(
                    name=fake.name(),
                    description=fake.text()
                )
            return JsonResponse({'message': 'Test data generated successfully!'}, status=200)
        except Exception as e:
            # 错误处理
            return JsonResponse({'error': str(e)}, status=400)

# URL配置
urlpatterns = [
    path('generate/', TestDataGenerator.as_view(), name='generate_test_data'),
]
