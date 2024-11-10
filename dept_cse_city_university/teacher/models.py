from django.db import models
from user.models import User

class Degree(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='degrees')
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    result = models.CharField(max_length=50)
    university = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} from {self.university} ({self.year})"

class Experience(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='experiences')
    institution_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    starting_date = models.DateField()
    ending_date = models.DateField(null=True, blank=True)  # null if still employed

    def __str__(self):
        return f"{self.institution_name} - {self.designation}"

class Teacher(models.Model):
    role = models.ForeignKey('user.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    photo = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    research = models.TextField(blank=True, null=True)
    publication = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.designation}"
