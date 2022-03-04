from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import (
    User
)

# Register your models here


UserAdmin.fieldsets[1][1]['fields'] = (
    'first_name', 'last_name', 'email', 'avatar'
)

admin.site.register(User, UserAdmin)
