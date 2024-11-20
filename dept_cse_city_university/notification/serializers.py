from rest_framework import serializers
from .models import AuthorityAnnouncement

class AuthorityAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorityAnnouncement
        fields = ['id', 'title', 'pdf_file', 'created_at', 'updated_at']
