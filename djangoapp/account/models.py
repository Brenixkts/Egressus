from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError

def validate_cpf(cpf):
        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            raise ValidationError(f'{cpf} não é um CPF válido.')
        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            raise ValidationError(f'{cpf} não é um CPF válido.')

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            raise ValidationError(f'{cpf} não é um CPF válido.')

class MyAccountManager(BaseUserManager):
    """
    Gerenciador personalizado para o modelo de usuário customizado.
    """
           
    def create_user(self, cpf, email, username, password=None, **extra_fields):
        """
        Cria e salva um usuário com o email, username, first_name, last_name, date_of_birth e senha fornecidos.
        """
        if not cpf:
            raise ValueError('O CPF é obrigatório para criar um usuário')
        if not email:
            raise ValueError('O email é obrigatório para criar um usuário')
        if not username:
            raise ValueError('O username é obrigatório para criar um usuário')

        email = self.normalize_email(email)
        user = self.model(cpf=cpf, email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, email, username, password, **extra_fields):
        """
        Cria e salva um superusuário com o email, username, first_name, last_name, date_of_birth e senha fornecidos.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        

        return self.create_user(cpf, email, username, password, **extra_fields)


class Account(AbstractBaseUser):
    """
    Modelo customizado de usuário que utiliza email como identificador único.
    """
    cpf = models.CharField(max_length=11,verbose_name="CPF", unique=True, validators=[validate_cpf])
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(verbose_name="Primeiro Nome", max_length=30, blank=True)
    last_name = models.CharField(verbose_name="Último Nome", max_length=30, blank=True)
    date_of_birth = models.DateField(verbose_name="Data de Nascimento", blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='Data de Cadastro', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Último Login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'cpf'  # Define o campo de identificação único como o email
    REQUIRED_FIELDS = ['email', 'username']  # Campos necessários ao criar um usuário via createsuperuser

    objects = MyAccountManager()  # Define o gerenciador personalizado para este modelo

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username

    def get_full_name(self):
        """
        Retorna o nome completo do usuário.
        """
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """
        Retorna o primeiro nome do usuário.
        """
        return self.first_name

    def has_perm(self, perm, obj=None):
        """
        Verifica se o usuário possui a permissão específica.
        No exemplo, todos os superusuários possuem todas as permissões.
        """
        return self.is_superuser

    def has_module_perms(self, app_label):
        """
        Verifica se o usuário tem permissões para acessar um módulo específico.
        No exemplo, todos os superusuários têm permissão para todos os módulos.
        """
        return True
    