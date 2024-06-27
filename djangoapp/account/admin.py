from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from account.models import Account


class AccountAdmin(UserAdmin):
    """
    Admin personalizado para o modelo Account.
    """
    model = Account
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_of_birth', 'date_joined', 'last_login', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('id', 'date_joined', 'last_login')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'date_of_birth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ()
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('email',)


admin.site.register(Account, AccountAdmin)
