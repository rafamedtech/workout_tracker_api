from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from workouts.models import Workout, Exercises
from .serializers import WorkoutSerializer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.decorators import permission_classes, parser_classes


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

        workout = Workout.objects.create(name=data['name'], type=data['type'])
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
        workout.exercises.clear()
        workout.save()
        for exercise in exercises:
            newExercise = Exercises.objects.create(workout=workout, **exercise)
            workout.exercises.add(newExercise)
        serializer = self.serializer_class(workout)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        workout = self.get_workout_by_id(pk)
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)