from rest_framework import serializers
from .models import Semester, Batch, SSCInfo, HSCInfo, Student, Routine, Subject, Registration, Result, Announcement


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['id', 'name', 'start_date', 'end_date', 'year']


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['id', 'name']


class SSCInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSCInfo
        fields = ['id', 'roll', 'reg', 'passing_year', 'result', 'school', 'board', 'group']


class HSCInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HSCInfo
        fields = ['id', 'roll', 'reg', 'passing_year', 'result', 'college', 'board', 'group']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id', 'user', 'phone', 'date_of_birth', 'address', 'batch', 'father_name', 'mother_name', 'gender', 
            'photo', 'ssc', 'hsc', 'student_id', 'is_approved', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}


class RoutineSerializer(serializers.ModelSerializer):
    batch_name = serializers.CharField(source='batch.name', read_only=True) 
    class Meta:
        model = Routine
        fields = ['id', 'batch', 'batch_name', 'file']




class SubjectSerializer(serializers.ModelSerializer):
    total_fee = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'course_title', 'course_code', 'credit', 'credit_fee', 'total_fee']


class RegistrationSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    semester = serializers.PrimaryKeyRelatedField(queryset=Semester.objects.all())
    courses = serializers.PrimaryKeyRelatedField(many=True, queryset=Subject.objects.all())
    total_fee = serializers.DecimalField(max_digits=8, decimal_places=2, read_only=True)

    class Meta:
        model = Registration
        fields = ['id', 'student', 'semester', 'courses', 'semester_fee', 'total_fee', 'time']

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = [
            'id', 'subject', 'batch', 'marks', 'exam_type', 'teacher', 'student', 'semester'
        ]


class AnnouncementSerializer(serializers.ModelSerializer):
    batch_name = serializers.CharField(source='batch.name', read_only=True)

    class Meta:
        model = Announcement
        fields = ['id', 'title', 'batch', 'batch_name', 'file']




