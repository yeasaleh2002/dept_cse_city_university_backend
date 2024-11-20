from django.contrib import admin

# Register your models here.
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'rating', 'created_at')
    search_fields = ('student__username', 'teacher__name', 'feedback_text')
    ordering = ('-created_at',)

admin.site.register(Feedback,FeedbackAdmin)