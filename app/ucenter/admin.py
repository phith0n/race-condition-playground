from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from . import models


@admin.register(models.User)
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'money')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'money', 'last_login', 'date_joined')
    readonly_fields = ('last_login', 'date_joined',)
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email', )
    ordering = ('-date_joined', )


@admin.register(models.WithdrawLog)
class WithdrawAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('amount', 'user')}),
        (_('Important dates'), {'fields': ('created_time', 'last_modify_time')}),
    )
    list_display = ('created_time', 'user', 'amount')
    readonly_fields = ('created_time', 'last_modify_time')
    ordering = ('-created_time',)
