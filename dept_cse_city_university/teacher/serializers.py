from rest_framework import serializers
from .models import Teacher, Degree, Experience


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ['id', 'teacher', 'name', 'year', 'result', 'university']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id','teacher', 'institution_name', 'designation', 'starting_date', 'ending_date']


class TeacherSerializer(serializers.ModelSerializer):
    degrees = DegreeSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)


    class Meta:
        model = Teacher
        fields = [
            'id', 'role', 'name', 'designation', 'email', 'phone', 'gender', 'photo',
            'description', 'research', 'publication', 'date_of_birth', 'address',
            'degrees', 'experiences'
        ]
