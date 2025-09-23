# 代码生成时间: 2025-09-23 17:41:30
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import ComponentLibrary

# 定义models.py
class ComponentLibrary(models.Model):
    """存储UI组件库信息"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回组件名称"""
        return self.name

# 定义views.py
class ComponentListView(View):
    """显示所有UI组件库的视图"""
    def get(self, request):
        try:
            components = ComponentLibrary.objects.all()
            return render(request, 'components.html', {'components': components})
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=500)

class ComponentDetailView(View):
    """显示特定UI组件库详细信息的视图"""
    def get(self, request, pk):
        try:
            component = ComponentLibrary.objects.get(pk=pk)
            return render(request, 'component.html', {'component': component})
        except ComponentLibrary.DoesNotExist:
            return HttpResponse("Component not found", status=404)
        except Exception as e:
            return HttpResponse("Error: " + str(e), status=500)

# 定义urls.py
urlpatterns = [
    path('components/', ComponentListView.as_view(), name='component-list'),
    path('components/<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
]

# 定义components.html模板（存储于templates/components.html）
# {% extends "base.html" %}
# {% block content %}
#     <h2>Component Library</h2>
#     <ul>
#         {% for component in components %}
#             <li>{{ component.name }} - {{ component.description }}</li>
#         {% endfor %}
#     </ul>
# {% endblock %}

# 定义component.html模板（存储于templates/component.html）
# {% extends "base.html" %}
# {% block content %}
#     <h2>{{ component.name }}</h2>
#     <p>{{ component.description }}</p>
# {% endblock %}