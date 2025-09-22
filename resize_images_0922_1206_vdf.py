# 代码生成时间: 2025-09-22 12:06:27
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse
from PIL import Image
# 扩展功能模块
import os
from io import BytesIO
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageResizer:
# 添加错误处理
    """Class to resize images in a Django application."""
    def __init__(self, size=(100, 100), quality=85):
        self.size = size
        self.quality = quality

    def resize_image(self, image_path):
        """Resize the image at the given path."""
        with Image.open(image_path) as img:
            img.thumbnail(self.size)
            resized_img = BytesIO()
            img.save(resized_img, format='JPEG', quality=self.quality)
            resized_img.seek(0)
            return ImageFile(resized_img, name=os.path.basename(image_path))

    @staticmethod
    def save_resized_image(resized_image, storage=default_storage):
        """Save the resized image to the storage."""
        storage.save(resized_image.name, ContentFile(resized_image.read()))
# 优化算法效率
        return resized_image.name
# 添加错误处理


@require_http_methods(['POST'])
# 添加错误处理
@csrf_exempt
def resize_images_view(request):
    "