from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'egressus_app/index.html')

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(cpf='46681423019', username='testuser', email='test@example.com', password='password123')

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'egressus_app/login.html')

    def test_login_view_post_success(self):
        response = self.client.post(reverse('login'), {'cpf': '46681423019', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"Bem vindo {self.user.first_name}")

    def test_login_view_post_failure(self):
        response = self.client.post(reverse('login'), {'cpf': '12345678910', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Erro de login") ##Alterar após a atualização da página home @Tobias-Costa @Brenixkts

# class HomeViewTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

#     def test_home_view_redirect_if_not_logged_in(self):
#         response = self.client.get(reverse('home'))
#         self.assertRedirects(response, '/login/?next=/home/')

#     def test_home_view_status_code_if_logged_in(self):
#         self.client.login(username='testuser', password='password123')
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)
