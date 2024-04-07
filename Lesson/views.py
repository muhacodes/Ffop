from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Lesson
from .serializers import LessonSerializer

# Create your views here.
class LessonnViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer