from django.test import TestCase
from account.models import Account
from django.core.exceptions import ValidationError

class AccountModelTest(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            cpf='23677381061',
            email='testuser@example.com',
            username='testuser',
            password='password123',
            first_name='Test',
            last_name='User',
            date_of_birth='1990-12-01'
        )

    def test_user_creation(self):
        self.assertIsInstance(self.user, Account)
        self.assertEqual(self.user.cpf, '23677381061')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.get_full_name(), 'Test User')
        self.assertEqual(self.user.get_short_name(), 'Test')
        self.assertTrue(self.user.check_password('password123'))

    def test_superuser_creation(self):
        admin_user = Account.objects.create_superuser(
            cpf='18700603007',
            email='admin@example.com',
            username='admin',
            password='adminpassword'
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_user_without_cpf(self):
        with self.assertRaises(ValueError):
            _ = Account.objects.create_user(
                cpf=None,
                email='testusererror@example.com',
                username='testusererror',
                password='password12345',
            )

    def test_user_cpf_validation_error(self):
        with self.assertRaises(ValidationError):
            user_error = Account.objects.create_user(
                cpf='81866735037',
                email='testusererror@example.com',
                username='testusererror',
                password='password12345',
            )
            user_error.full_clean()
    
    def test_user_cpf_update_to_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.cpf = '23667381061'
            self.user.full_clean()

    def test_user_cpf_update_to_invalid_with_minus_than_11(self):
        with self.assertRaises(ValidationError):
            self.user.cpf = '2222'
            self.user.full_clean()

    def test_user_cpf_update_to_invalid_with_equal_numbers(self):
        with self.assertRaises(ValidationError):
            self.user.cpf = '22222222222'
            self.user.full_clean()
           
