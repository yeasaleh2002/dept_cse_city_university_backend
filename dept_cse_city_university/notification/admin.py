from django.contrib import admin

# Register your models here.
from .models import AuthorityAnnouncement


class AuthorityAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'pdf_file', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('-created_at',)

admin.site.register(AuthorityAnnouncement, AuthorityAnnouncementAdmin)