from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Teacher, Degree, Experience
from .serializers import TeacherSerializer, DegreeSerializer, ExperienceSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAdminUser] 
   


class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    permission_classes = [permissions.IsAdminUser] 


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.IsAdminUser] 