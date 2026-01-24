from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # To control which fields are listed, we use list_display
    list_display = [
        "email",
        "username",
        "age",
        "is_staff"
    ]
    # To edit new custom fields, like age, we must add fieldsets
    fieldsets = UserAdmin.fieldsets +  ((None, {"fields": ("age",)}),)
    # To include a new custom field in the section for creating a new user we rely on add_fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)

    '''
    There are many ways to customize the user admin, 
    and some developers like to add additional options such as 
    list_filter, search_fields, and ordering.
    '''

admin.site.register(CustomUser, CustomUserAdmin)