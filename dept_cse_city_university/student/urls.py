from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SemesterViewSet, 
    BatchViewSet, 
    SSCInfoViewSet, 
    HSCInfoViewSet, 
    StudentViewSet, 
    RoutineViewSet, 
    SubjectViewSet, 
    RegistrationViewSet, 
    ResultViewSet, 
    AnnouncementViewSet
)

router = DefaultRouter()
router.register(r'semesters', SemesterViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'sscinfo', SSCInfoViewSet)
router.register(r'hscinfo', HSCInfoViewSet)
router.register(r'students', StudentViewSet)
router.register(r'routines', RoutineViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'results', ResultViewSet)
router.register(r'announcements', AnnouncementViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]
