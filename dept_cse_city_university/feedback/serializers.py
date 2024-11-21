from rest_framework import serializers
from .models import Feedback
from teacher.models import Teacher
from django.contrib.auth import get_user_model

class FeedbackSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(queryset=Teacher.objects.all(), slug_field='name')

    class Meta:
        model = Feedback
        fields = ['id','teacher', 'feedback_text','created_at']
        read_only_fields = ['created_at']
    
    def create(self, validated_data):
        # Automatically set the student field to the current logged-in user
        user = self.context['request'].user
        validated_data['student'] = user
        return super().create(validated_data)
