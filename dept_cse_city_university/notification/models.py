from django.db import models

# Create your models here.

class AuthorityAnnouncement(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='announcements/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
