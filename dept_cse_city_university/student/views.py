from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters  # Import Django Filter

from .models import Semester, Batch, SSCInfo, HSCInfo, Student, Routine, Subject, Registration, Result, Announcement
from .serializers import SemesterSerializer, BatchSerializer, SSCInfoSerializer, HSCInfoSerializer, StudentSerializer, RoutineSerializer, SubjectSerializer, RegistrationSerializer, ResultSerializer, AnnouncementSerializer

class SemesterFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="start_date", lookup_expr='gte')  
    end_date = filters.DateFilter(field_name="end_date", lookup_expr='lte')  
    year = filters.NumberFilter(field_name="year", lookup_expr='exact') 

    class Meta:
        model = Semester
        fields = ['start_date', 'end_date', 'year']

class StudentFilter(filters.FilterSet):
    batch_name = filters.CharFilter(field_name="batch__name", lookup_expr='icontains')  
    student_id = filters.CharFilter(field_name="student_id", lookup_expr='exact')  

    class Meta:
        model = Student
        fields = ['batch_name', 'student_id']

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    filter_backends = (SearchFilter, OrderingFilter, filters.DjangoFilterBackend)  
    filterset_class = SemesterFilter 
    search_fields = ['name', 'year']  
    ordering_fields = ['start_date', 'end_date', 'year']  
    ordering = ['start_date'] 

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    filter_backends = (SearchFilter, OrderingFilter, filters.DjangoFilterBackend)
    filterset_fields = ['name']  
    search_fields = ['name'] 
    ordering_fields = ['name']
    ordering = ['name']

class SSCInfoViewSet(viewsets.ModelViewSet):
    queryset = SSCInfo.objects.all()
    serializer_class = SSCInfoSerializer
    filter_backends = (SearchFilter, OrderingFilter, filters.DjangoFilterBackend)
    filterset_fields = ['roll', 'school', 'board', 'result']  
    search_fields = ['roll', 'school', 'board', 'result']  
    ordering_fields = ['passing_year', 'result']
    ordering = ['passing_year']

class HSCInfoViewSet(viewsets.ModelViewSet):
    queryset = HSCInfo.objects.all()
    serializer_class = HSCInfoSerializer
    filter_backends = (SearchFilter, OrderingFilter, filters.DjangoFilterBackend)
    filterset_fields = ['roll', 'college', 'board', 'result']
    search_fields = ['roll', 'college', 'board', 'result']
    ordering_fields = ['passing_year', 'result']
    ordering = ['passing_year']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (SearchFilter, OrderingFilter, filters.DjangoFilterBackend)
    filterset_class = StudentFilter  
    search_fields = ['user__first_name', 'user__last_name', 'student_id', 'phone', 'batch__name']  
    ordering_fields = ['student_id', 'date_of_birth', 'is_approved']
    ordering = ['student_id']

class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    filter_backends = (SearchFilter, OrderingFilter, filters.DjangoFilterBackend)
    filterset_fields = ['batch__name']  
    search_fields = ['batch__name']  
    ordering_fields = ['batch__name']
    ordering = ['batch__name']

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = (SearchFilter, OrderingFilter, filters.DjangoFilterBackend)
    filterset_fields = ['course_title', 'course_code']  
    search_fields = ['course_title', 'course_code']  
    ordering_fields = ['course_title', 'credit']
    ordering = ['course_title']

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    filter_backends = (SearchFilter, OrderingFilter, filters.DjangoFilterBackend)
    filterset_fields = ['student__student_id', 'semester__name'] 
    search_fields = ['student__user__first_name', 'student__user__last_name', 'semester__name']
    ordering_fields = ['semester__start_date', 'total_fee']
    ordering = ['semester__start_date']

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    filter_backends = (SearchFilter, OrderingFilter, filters.DjangoFilterBackend)
    filterset_fields = ['subject__course_title', 'exam_type'] 
    search_fields = ['subject__course_title', 'student__user__first_name', 'exam_type']
    ordering_fields = ['marks', 'exam_type']
    ordering = ['marks']

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    filter_backends = (SearchFilter, OrderingFilter, filters.DjangoFilterBackend)
    filterset_fields = ['title', 'batch__name']  
    search_fields = ['title', 'batch__name']
    ordering_fields = ['title', 'batch__name']
    ordering = ['title']
