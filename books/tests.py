from django.test import TestCase, Client
from django.urls import reverse

class IELTSBooksViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cambridge IELTS Books')

    def test_book_reader_status(self):
        response = self.client.get('/book/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Online Book Reader')

    def test_robots_txt(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/plain')
        self.assertIn(b'User-agent', response.content)

    def test_sitemap_xml(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')
        self.assertIn(b'<urlset', response.content)

    def test_health_check(self):
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'healthy', 'service': 'ielts-books-django'})

    def test_404_handler(self):
        response = self.client.get('/non-existent-page-url/')
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Page not found', status_code=404)
