from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, DegreeViewSet, ExperienceViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'degrees', DegreeViewSet)
router.register(r'experiences', ExperienceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
