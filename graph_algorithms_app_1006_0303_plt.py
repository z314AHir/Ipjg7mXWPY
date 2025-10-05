# 代码生成时间: 2025-10-06 03:03:32
from django.db import models
from django.http import JsonResponse
from django.views import View
from django.urls import path
import networkx as nx

# Define the Graph Algorithms model
class Graph(models.Model):
    """Model to store graph data."""
    name = models.CharField(max_length=255)
    graph_data = models.JSONField()

    def __str__(self):
        return self.name

# Define a view to handle graph algorithm requests
class GraphAlgorithmsView(View):
    """View to handle requests related to graph algorithms."""
    def post(self, request):
        """Handle POST request to compute graph algorithms."""
        data = request.POST.get('data')
        try:
            # Parse the graph data and create a NetworkX graph
            graph_data = json.loads(data)
            G = nx.Graph()
            G.add_nodes_from(graph_data.get('nodes', []))
            G.add_edges_from(graph_data.get('edges', []))

            # Example algorithm: Check if the graph is connected
            if nx.is_connected(G):
                result = {'is_connected': True}
            else:
                result = {'is_connected': False}

            # You can add more algorithms here
            # ...

            return JsonResponse(result)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# URL configuration for the Graph Algorithms View
urlpatterns = [
    path('graph_algorithms', GraphAlgorithmsView.as_view(), name='graph_algorithms'),
]
