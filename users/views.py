from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutUserView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        return Response({'message': 'Logout Sucessful'}, status=status.HTTP_200_OK)

class GetUserView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        return Response({'user': request.user.name, 'email': request.user.email}, status=status.HTTP_200_OK)