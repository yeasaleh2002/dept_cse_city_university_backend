from django.contrib import admin
from .models import Semester, Batch,Student, Routine, Subject, Result, Announcement,Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'semester', 'total_fee', 'time')
    list_filter = ('semester', 'time') 
    search_fields = ('student__name', 'semester__name') 
    readonly_fields = ('total_fee',)  
    filter_horizontal = ('courses',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'year')
    search_fields = ('name', 'year')
    list_filter = ('name', 'year')

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'batch', 'is_approved', 'gender', 'phone')
    list_filter = ('is_approved', 'batch', 'gender')
    search_fields = ('user__first_name', 'user__last_name', 'student_id', 'phone', 'ssc_roll', 'hsc_roll')
    readonly_fields = ('student_id', 'password')  # Make certain fields read-only
    fieldsets = (
        ('Personal Information', {
            'fields': ('user', 'photo', 'phone', 'date_of_birth', 'gender', 'address', 'father_name', 'mother_name')
        }),
        ('Batch and Status', {
            'fields': ('batch', 'is_approved', 'student_id')
        }),
        ('SSC Information', {
            'fields': ('ssc_roll', 'ssc_reg', 'ssc_passing_year', 'ssc_result', 'ssc_school', 'ssc_board', 'ssc_group')
        }),
        ('HSC Information', {
            'fields': ('hsc_roll', 'hsc_reg', 'hsc_passing_year', 'hsc_result', 'hsc_college', 'hsc_board', 'hsc_group')
        }),
        ('System Information', {
            'fields': ('password',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """
        Make `student_id` and `password` read-only after the student is created.
        """
        if obj:
            return self.readonly_fields + ('student_id', 'password')
        return self.readonly_fields


# Register the Student model with the custom admin class
admin.site.register(Student, StudentAdmin)


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('batch', 'file')
    search_fields = ('batch__name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'course_code', 'credit', 'credit_fee')
    search_fields = ('course_title', 'course_code')
    list_filter = ('credit',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks', 'exam_type', 'semester')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'subject__course_title', 'exam_type')
    list_filter = ('exam_type', 'semester', 'batch', 'subject')

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'batch', 'file')
    search_fields = ('title', 'batch__name')
