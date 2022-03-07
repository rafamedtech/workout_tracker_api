from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserProfileSerializer

class RegisterUserView(APIView):
    def post(self, request):
        user = UserProfile.objects.get(email=request.data['email'])

        if user:
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutUserView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        return Response({'message': 'Logout Sucessful'}, status=status.HTTP_200_OK)

class GetUserView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        return Response({'user': request.user.name, 'email': request.user.email}, status=status.HTTP_200_OK)