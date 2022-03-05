from django.contrib import admin
from workouts.models import Workout, Exercises
from users.models import UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Workout)
admin.site.register(Exercises)


