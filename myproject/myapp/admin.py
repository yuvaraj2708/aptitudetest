from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import UserProfile,UserAnswer
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
    
User = get_user_model()




class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ('department', 'role', 'topic','question','answeroption','a','b','c','d')
admin.site.register(UserProfile, UserProfileAdmin)

# Register the Question model in the admin site

admin.site.register(UserAnswer)