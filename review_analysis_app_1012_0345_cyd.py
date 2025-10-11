# 代码生成时间: 2025-10-12 03:45:23
from django.db import models
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.urls import path
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

# Models
class Review(models.Model):
    """Model representing a review."""
    text = models.TextField(help_text="The text of the review.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a string representation of the Review."""
        return f"Review {self.pk} ({self.text[:20]}..."

# Views
@method_decorator(csrf_protect, name='dispatch')
class ReviewAnalysis(View):
    """View handling review analysis."""
    def get(self, request, *args, **kwargs):
        """Handle GET request for review analysis."""
        reviews = Review.objects.all()
        return render(request, 'review_analysis/analysis.html', {'reviews': reviews})

    def post(self, request, *args, **kwargs):
        """Handle POST request for submitting a new review."""
        try:
            text = request.POST['text']
            review = Review(text=text)
            review.save()
            return JsonResponse({'status': 'success', 'message': 'Review submitted successfully.'}, status=201)
        except KeyError:
            return JsonResponse({'status': 'error', 'message': 'Missing review text.'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# URLs
urlpatterns = [
    path('analysis/', ReviewAnalysis.as_view(), name='review_analysis'),
]

# Templates
# review_analysis/analysis.html
# {% extends "base.html" %}
# {% block content %}
# <h1>Review Analysis</h1>
# <form method="post" action="{% url 'review_analysis' %}">
#     {% csrf_token %}
#     <textarea name="text" required></textarea>
#     <button type="submit">Submit Review</button>
# </form>
# <ul>
#     {% for review in reviews %}
#         <li>{{ review.text }}</li>
#     {% endfor %}
# </ul>
# {% endblock %}
