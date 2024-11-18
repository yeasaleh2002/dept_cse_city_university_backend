from rest_framework import serializers
from .models import Teacher, Degree, Experience
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from user.models import User

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ['id', 'teacher', 'name', 'year', 'result', 'university']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'teacher', 'institution_name', 'designation', 'starting_date', 'ending_date']

class TeacherSerializer(serializers.ModelSerializer):
    degrees = DegreeSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=False)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, default='teacher')

    class Meta:
        model = Teacher
        fields = [
            'id', 'role', 'name', 'designation', 'email', 'password', 'confirm_password', 'phone', 'gender', 'photo',
            'description', 'research', 'publication', 'date_of_birth', 'address',
            'degrees', 'experiences'
        ]

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        
        # Ensure the email is unique in the User table
        if User.objects.filter(email=attrs.get('email')).exists():
            raise serializers.ValidationError("A user with this email already exists.")

        return attrs

    def create(self, validated_data):
        # Remove confirm_password from validated_data after validation
        validated_data.pop('confirm_password', None)

        # Extract and hash the password
        password = validated_data.pop('password', None)
        if password:
            hashed_password = make_password(password)
        else:
            hashed_password = None

        # Create User instance for the Teacher
        role = validated_data.pop('role', 'teacher')  # Default to 'teacher' if no role is provided
        user = User(
            username=validated_data['email'],  # Using email as the username
            email=validated_data['email'],
            role=role,  # Use the role passed in the validated data (can be 'teacher', 'admin', etc.)
        )
        if hashed_password:
            user.password = hashed_password  # Set the hashed password
        user.save()

        # Create Teacher instance and associate it with the User
        teacher = Teacher.objects.create(
            user=user,
            name=validated_data['name'],
            designation=validated_data['designation'],
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            gender=validated_data['gender'],
            photo=validated_data.get('photo'),
            description=validated_data.get('description'),
            research=validated_data.get('research'),
            publication=validated_data.get('publication'),
            date_of_birth=validated_data['date_of_birth'],
            address=validated_data.get('address')
        )
        
        return teacher
