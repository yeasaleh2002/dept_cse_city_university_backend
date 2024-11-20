from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import AuthorityAnnouncement
from .serializers import AuthorityAnnouncementSerializer

class AuthorityAnnouncementViewSet(ModelViewSet):
    queryset = AuthorityAnnouncement.objects.all().order_by('-created_at')
    serializer_class = AuthorityAnnouncementSerializer
