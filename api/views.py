from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class getRoutes(APIView):
    def get(self, request):

        routes = [
            { 'GET': '/api/workouts/' },
            { 'GET': '/api/workouts/<int:pk>/' },
            { 'POST': '/api/workouts/' },
            { 'PUT': '/api/workouts/<int:pk>/' },
            { 'DELETE': '/api/workouts/<int:pk>/' },

        ]

        return Response(routes)