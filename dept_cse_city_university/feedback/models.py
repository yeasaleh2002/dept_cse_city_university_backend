from django.db import models

# Create your models here.
from django.conf import settings
from teacher.models import Teacher

class Feedback(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Link to the Teacher model
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback from {self.student.username} to {self.teacher.name}"
