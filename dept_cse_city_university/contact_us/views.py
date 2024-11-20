from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import ContactUs
from .serializers import ContactUsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all().order_by('-created_at')
    serializer_class = ContactUsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_resolved']
    search_fields = ['name', 'email', 'subject', 'message']
    
