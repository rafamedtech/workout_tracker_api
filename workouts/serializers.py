from rest_framework import serializers
from .models import Workout, Exercises
from users.models import UserProfile

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)
    owner = serializers.ReadOnlyField(source='owner.name')

    class Meta:
        model = Workout
        fields = ['id', 'name', 'type', 'exercises', 'owner', 'created_at']

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        workout = Workout.objects.create(**validated_data)
        for exercise in exercises_data:
            Exercises.objects.create(workout=workout, **exercise)
        return workout