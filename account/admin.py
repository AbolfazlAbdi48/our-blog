from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import (
    User,
    Ticket
)

# Register your models here


UserAdmin.fieldsets[1][1]['fields'] = (
    'first_name', 'last_name', 'email', 'avatar'
)
UserAdmin.list_display = ("username", "get_avatar",
                          "email", "first_name", "last_name", "is_staff")

admin.site.register(User, UserAdmin)


class TicketAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('subject', 'message')
    list_display = ('subject', 'user', 'created')
    list_filter = ('created',)

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Ticket, TicketAdmin)
