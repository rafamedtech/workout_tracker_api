from django.db import models
from users.models import UserProfile
import uuid

# Create your models here.
class Exercises(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    strength_type = models.CharField(max_length=100, blank=True, null=True)
    sets = models.IntegerField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    cardio_type = models.CharField(max_length=100, blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    pace = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.strength_type:
            return self.strength_type
        else:
            return self.cardio_type


class Workout(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercises)

    def __str__(self):
        return self.name