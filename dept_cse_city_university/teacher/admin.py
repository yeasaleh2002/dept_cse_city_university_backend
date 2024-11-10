from django.contrib import admin
from .models import Teacher
from .models import Degree
from .models import Experience

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Degree)
admin.site.register(Experience)