from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SemesterViewSet, 
    BatchViewSet,  
    StudentViewSet, 
    RoutineViewSet, 
    SubjectViewSet, 
    RegistrationViewSet, 
    ResultViewSet, 
    AnnouncementViewSet,
    LoginAPIView,
)

# Create router and register viewsets
router = DefaultRouter()
router.register(r'semesters', SemesterViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'students', StudentViewSet)
router.register(r'routines', RoutineViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'results', ResultViewSet)
router.register(r'announcements', AnnouncementViewSet)

# Include router and standalone paths
urlpatterns = [
    path('', include(router.urls)),  # Routes for viewsets
    path('login/', LoginAPIView.as_view(), name='login'),  # Standalone login endpoint
]
