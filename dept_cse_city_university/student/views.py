from rest_framework import viewsets,status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters 
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Student
from .serializers import StudentSerializer, StudentCreateSerializer
from django.core.mail import send_mail
from django.conf import settings 

from .models import Semester, Batch, Student, Routine, Subject, Registration, Result, Announcement
from .serializers import SemesterSerializer, BatchSerializer, StudentSerializer, RoutineSerializer, SubjectSerializer, RegistrationSerializer, ResultSerializer, AnnouncementSerializer

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

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing Student objects.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_serializer_class(self):
        """
        Use a different serializer for creating objects.
        """
        if self.action == 'create':
            return StudentCreateSerializer
        return StudentSerializer

    def perform_create(self, serializer):
        """
        Save a new student instance.
        """
        serializer.save()

    @action(detail=True, methods=['patch'])
    def approve(self, request, pk=None):
        """
        Approve a student and assign a student ID and password.
        """
        student = self.get_object()
        if not student.is_approved:
            student.is_approved = True
            student.save()
            # Send approval email
            subject = "Your Admission has been Approved"
            message = f"""
            Dear {student.user.first_name},

            Congratulations! Your admission has been approved.

            Your Student ID: {student.student_id}
            Your Password: {student.password}

            You can log in using your email and the provided password.

            Regards,
            Admission Office
            """
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [student.user.email]
            )
            return Response({"message": "Student approved successfully!"}, status=status.HTTP_200_OK)
        return Response({"message": "Student is already approved!"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def my_profile(self, request):
        """
        Retrieve the authenticated user's student profile.
        """
        student = self.queryset.filter(user=request.user).first()
        if not student:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(student)
        return Response(serializer.data)

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
