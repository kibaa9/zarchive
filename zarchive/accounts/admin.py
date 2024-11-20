from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from zarchive.accounts.forms import AppUserChangeForm, AppUserForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    add_form = AppUserForm
    form = AppUserChangeForm

    list_display = ('username', 'email', 'is_active')

    fieldsets = (
        ('Credentials', {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (None, {'fields': ('is_active', )})
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide', ),
                'fields': ('username', 'email', 'password1', 'password2'),
            },
        ),
    )
