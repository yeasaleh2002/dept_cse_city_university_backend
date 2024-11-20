from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactUsViewSet

# Create a router and register the ContactUs ViewSet
router = DefaultRouter()
router.register(r'contact-us', ContactUsViewSet, basename='contact-us')

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]

