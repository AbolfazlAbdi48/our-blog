from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import (
    User
)

# Register your models here


UserAdmin.fieldsets[1][1]['fields'] = (
    'first_name', 'last_name', 'email', 'avatar'
)
UserAdmin.list_display = ("username", "get_avatar", "email", "first_name", "last_name", "is_staff")

admin.site.register(User, UserAdmin)
