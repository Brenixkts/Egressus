from django.test import SimpleTestCase
from django.urls import reverse, resolve
from egressus_app.views import index, login_authentication

class UrlsTest(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_authentication)
