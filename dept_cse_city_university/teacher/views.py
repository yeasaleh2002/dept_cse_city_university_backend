from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Teacher, Degree, Experience
from .serializers import TeacherSerializer, DegreeSerializer, ExperienceSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
   


class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
   


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer