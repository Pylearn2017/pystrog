from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExerciseSerializer
from .models import Exercise

@api_view()
def exercise_list(request):
    return Response('ok')

@api_view()
def exersise_detail(request, id):
    exercise = Exercise.objects.get(pk=id)
    serializer = ExerciseSerializer(exercise)
    return Response(serializer.data)
