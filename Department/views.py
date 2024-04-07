from django.shortcuts import render
from .serialiers import DepartmentSerializer
from rest_framework import viewsets, status
from .models import Department
# Create your views here.


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
