from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from account.models import Account


class AccountAdmin(UserAdmin):
    """
    Admin personalizado para o modelo Account.
    """
    # Define qual modelo será utilizado pelo admin personalizado
    model = Account
    
    # Define os campos que serão exibidos na lista de objetos no admin
    list_display = ('cpf', 'username', 'email', 'first_name', 'last_name', 'date_of_birth', 'date_joined', 'last_login', 'is_staff', 'is_superuser')
    
    # Define os campos que poderão ser utilizados para pesquisa no admin
    search_fields = ('cpf', 'username', 'email', 'first_name', 'last_name')
    
    # Define os campos que serão somente leitura no admin
    readonly_fields = ('id', 'date_joined', 'last_login')

    # Define a disposição dos campos nos formulários de visualização/edição
    fieldsets = (
        (None, {'fields': ('cpf', 'username', 'email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'date_of_birth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Define a disposição dos campos no formulário de adição de um novo objeto
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'username', 'email', 'password1', 'password2'),
        }),
    )

    # Define campos de filtro horizontal (não utilizado aqui)
    filter_horizontal = ()

    # Define os filtros disponíveis na barra lateral do admin
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    # Define a ordenação padrão dos objetos na lista
    ordering = ('cpf',)

# Registra o modelo Account e seu admin personalizado no site do admin
admin.site.register(Account, AccountAdmin)
