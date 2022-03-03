from django.urls import path
from .views import WorkoutView, SingleWorkoutView

urlpatterns = [
    path('', WorkoutView.as_view()),
    path('<str:pk>/', SingleWorkoutView.as_view()),
]