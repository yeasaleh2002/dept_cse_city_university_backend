from django.db import models
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.hashers import make_password
from user.models import User
from teacher.models import Teacher
from decimal import Decimal

from django.utils.crypto import get_random_string


class Semester(models.Model):
    SEMESTER_CHOICES = [
        ('fall', 'Fall'),
        ('spring', 'Spring'),
    ]

    name = models.CharField(max_length=100, choices=SEMESTER_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name.capitalize()} {self.year}"


class Batch(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    # User and Personal Information
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student', null=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()
    batch = models.ForeignKey('Batch', on_delete=models.CASCADE, null=True)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    student_id = models.CharField(max_length=5, unique=True, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    password = models.CharField(max_length=128, blank=True, null=True)

    # SSC Information
    ssc_roll = models.CharField(max_length=50, blank=True, null=True)
    ssc_reg = models.CharField(max_length=50, blank=True, null=True)
    ssc_passing_year = models.IntegerField(blank=True, null=True)
    ssc_result = models.CharField(max_length=10, blank=True, null=True)
    ssc_school = models.CharField(max_length=255, blank=True, null=True)
    ssc_board = models.CharField(max_length=50, blank=True, null=True)
    ssc_group = models.CharField(max_length=50, blank=True, null=True)

    # HSC Information
    hsc_roll = models.CharField(max_length=50, blank=True, null=True)
    hsc_reg = models.CharField(max_length=50, blank=True, null=True)
    hsc_passing_year = models.IntegerField(blank=True, null=True)
    hsc_result = models.CharField(max_length=10, blank=True, null=True)
    hsc_college = models.CharField(max_length=255, blank=True, null=True)
    hsc_board = models.CharField(max_length=50, blank=True, null=True)
    hsc_group = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def generate_student_id(self):
        last_student = Student.objects.all().order_by('-id').first()
        if not last_student or not last_student.student_id:
            new_id = 1
        else:
            new_id = int(last_student.student_id) + 1

        while Student.objects.filter(student_id=str(new_id).zfill(5)).exists():
            new_id += 1
        return str(new_id).zfill(5)

    def save(self, *args, **kwargs):
        # Check if the student is being approved
        if self.is_approved and not self.student_id:
            # Generate and assign student ID
            self.student_id = self.generate_student_id()
            # Generate a random password
            raw_password = get_random_string(length=8)
        
            # Hash the password before saving it to the database
            self.password = make_password(raw_password)
            send_mail(
                'Your Approval Confirmation',
                f'Congratulations {self.user.first_name},\n\n'
                f'You have been approved as a student.\n\n'
                f'Your Student ID: {self.student_id}\n'
                f'Your Password: {raw_password}\n\n'
                f'Please log in to your account and change your password for security.',
                'admin@example.com',  # Replace with your admin email
                [self.user.email],
                fail_silently=False,
            )
        super().save(*args, **kwargs)


class Routine(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    file = models.FileField(upload_to='routines/')

    def __str__(self):
        return f"Routine for {self.batch.name}"


class Subject(models.Model):
    course_title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=50)
    credit = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, null=True, blank=True)
    credit_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True, blank=True)

    def __str__(self):
        return f"{self.course_title} ({self.course_code}) - {self.credit} credits"

    @property
    def total_fee(self):
        if self.credit is not None and self.credit_fee is not None:
            return self.credit * self.credit_fee
        return Decimal("0.00")


class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Subject, related_name='registrations')
    semester_fee = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Registration of {self.student} for {self.semester}"

    @property
    def total_fee(self):
        courses_total = sum(course.total_fee for course in self.courses.all())
        return courses_total + self.semester_fee


class Result(models.Model):
    EXAM_TYPE_CHOICES = [
        ('Mid', 'Midterm'),
        ('Final', 'Final'),
        ('CT', 'Class Test'),
        ('Assignment', 'Assignment'),
        ('Attendance', 'Attendance'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f"Result for {self.student.user.first_name} {self.student.user.last_name} in {self.subject.course_title} - {self.exam_type}"


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    file = models.FileField(upload_to='announcements/', blank=True, null=True)

    def __str__(self):
        return f"Announcement: {self.title} for {self.batch.name}"
