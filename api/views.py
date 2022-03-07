from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class getRoutes(APIView):
    def get(self, request):

        routes = [
            { 'GET': '/api/workouts/' },
            { 'GET': '/api/workouts/<id>/' },
            { 'POST': '/api/workouts/' },
            { 'PUT': '/api/workouts/<id>/' },
            { 'DELETE': '/api/workouts/<id>/' },

        ]

        return Response(routes)