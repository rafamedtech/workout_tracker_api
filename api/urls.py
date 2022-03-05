from django.urls import path, include
from .views import getRoutes

urlpatterns = [
    path('', getRoutes.as_view()),
    path('workouts/', include('workouts.urls')),
    path('users/', include('users.urls')),
]