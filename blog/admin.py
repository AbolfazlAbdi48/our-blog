from django.contrib import admin
from .models import (
    IPAddress,
    Category
)

# Register your models here.


# IPAddress model admin
class IPAddressAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# category model admin
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(IPAddress, IPAddressAdmin)  # registering IPAddress model
admin.site.register(Category, CategoryAdmin)  # registering Category model
