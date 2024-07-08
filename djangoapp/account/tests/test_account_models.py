from django.test import TestCase
from account.models import Account

class AccountModelTest(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            password='password123',
            first_name='Test',
            last_name='User',
            date_of_birth='1990-12-01'
        )

    def test_user_creation(self):
        self.assertIsInstance(self.user, Account)
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.get_full_name(), 'Test User')
        self.assertEqual(self.user.get_short_name(), 'Test')
        self.assertTrue(self.user.check_password('password123'))

    def test_superuser_creation(self):
        admin_user = Account.objects.create_superuser(
            email='admin@example.com',
            username='admin',
            password='adminpassword'
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
