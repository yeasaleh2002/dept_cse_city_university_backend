from django.db import models

# Create your models here.
from django.conf import settings
from teacher.models import Teacher

class Feedback(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to the logged-in student (User model)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Link to the Teacher model
    feedback_text = models.TextField()
    rating = models.PositiveIntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])  # Rating from 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback from {self.student.username} to {self.teacher.name}"
