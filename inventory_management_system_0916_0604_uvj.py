# 代码生成时间: 2025-09-16 06:04:57
from django.db import models
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.urls import path
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.validators import MinValueValidator

"""
# NOTE: 重要实现细节
库存管理系统应用组件
""""

# Models
class Product(models.Model):
    """
    产品模型
    """
    name = models.CharField(max_length=100, help_text="产品名称")
    quantity = models.IntegerField(validators=[MinValueValidator(0)], help_text="产品库存数量")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="产品价格")

    def __str__(self):
        return self.name

# Views
class ProductView(View):
    """
    产品视图
    """
    def get(self, request):
        """
        获取产品列表
        """
        products = Product.objects.all()
        return JsonResponse(list(products.values()), safe=False)

    @method_decorator(csrf_exempt, name='dispatch')
    def post(self, request):
# TODO: 优化性能
        """
        添加新产品
        """
        try:
            data = request.POST.dict()
            product = Product.objects.create(**data)
            return JsonResponse({'id': product.id, 'name': product.name}, status=201)
        except ValidationError as e:
            return HttpResponse(e.message_dict, status=400)

    @method_decorator(csrf_exempt, name='dispatch')
# 改进用户体验
    def put(self, request, pk):
# TODO: 优化性能
        """
        更新产品
        """
        try:
            product = Product.objects.get(pk=pk)
            data = request.POST.dict()
# 扩展功能模块
            for key, value in data.items():
                setattr(product, key, value)
            product.save()
            return JsonResponse({'id': product.id, 'name': product.name})
        except ObjectDoesNotExist:
            return HttpResponse("Product not found", status=404)
        except ValidationError as e:
            return HttpResponse(e.message_dict, status=400)

    @method_decorator(csrf_exempt, name='dispatch')
# FIXME: 处理边界情况
    def delete(self, request, pk):
        """
        删除产品
        """
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return HttpResponse(status=204)
        except ObjectDoesNotExist:
            return HttpResponse("Product not found", status=404)

# URLs
urlpatterns = [
    path('products/', ProductView.as_view()),
]
