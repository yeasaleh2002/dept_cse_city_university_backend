from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(required=True)