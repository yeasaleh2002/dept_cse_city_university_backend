from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all().order_by('-created_at')
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create feedback

    def perform_create(self, serializer):
        # Automatically set the student (user) while creating feedback
        serializer.save(student=self.request.user)
