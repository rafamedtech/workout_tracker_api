from django.urls import path
from .views import RegisterUserView, LogoutUserView, GetUserView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', GetUserView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('logout/', LogoutUserView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]