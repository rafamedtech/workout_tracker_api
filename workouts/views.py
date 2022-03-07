from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from workouts.models import Workout, Exercises
from users.models import UserProfile
from .serializers import WorkoutSerializer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser


class WorkoutView(APIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    
    def get(self, request, *args, **kwargs):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        exercises = data['exercises']
        owner = UserProfile.objects.get(id=request.user.id)

        workout = Workout.objects.create(name=data['name'], type=data['type'], owner=owner)

        for exercise in exercises:
            newExercise = Exercises.objects.create(workout=workout, **exercise)
            workout.exercises.add(newExercise)

        serializer = self.serializer_class(workout)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SingleWorkoutView(APIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def get_workout_by_id(self, pk):
        try:
            workout = Workout.objects.get(id=pk)
            return workout
        except:
            return Response({'error': 'Workout not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, *args, **kwargs):
        workout = self.get_workout_by_id(pk)
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        workout = self.get_workout_by_id(pk)
        data = request.data
        exercises = data['exercises']
        workout.name = data['name']
        workout.type = data['type']

        for exercise in exercises:
            if 'id' in exercise:
                newExercise = Exercises.objects.get(id=exercise['id'])
                if workout.type == 'strength':
                    newExercise.strength_type = exercise['strength_type']
                    newExercise.reps = exercise['reps']
                    newExercise.sets = exercise['sets']
                    newExercise.weight = exercise['weight']
                else: 
                    newExercise.cardio_type = exercise['cardio_type']
                    newExercise.distance = exercise['distance']
                    newExercise.duration = exercise['duration']
                    newExercise.pace = exercise['pace']
            if 'id' not in exercise:
                newExercise = Exercises.objects.create(workout=workout, **exercise)
                workout.exercises.add(newExercise)
            newExercise.save()

        workout.save()
        serializer = self.serializer_class(workout)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        workout = self.get_workout_by_id(pk)
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  