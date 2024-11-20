from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('id',)

  
# Register the User model with the custom ModelAdmin
admin.site.register(User, UserAdmin)
