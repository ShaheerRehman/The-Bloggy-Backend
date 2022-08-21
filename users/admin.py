from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users.models import New


class UserAdminConfig(UserAdmin):
    model = New
    search_fields = ('email', 'username', 'first_name',)
    list_filter = ('email', 'username', 'first_name', 'is_active', 'is_staff',)
    ordering = ('-date_joined',)
    list_display = ('email', 'id', 'username', 'first_name', 'is_active', 'is_staff',)


admin.site.register(New, UserAdminConfig)