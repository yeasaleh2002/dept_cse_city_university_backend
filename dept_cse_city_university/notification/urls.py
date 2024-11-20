from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorityAnnouncementViewSet

router = DefaultRouter()
router.register('announcements', AuthorityAnnouncementViewSet, basename='announcement')

urlpatterns = [
    path('', include(router.urls)),
]
