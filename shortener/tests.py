from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from shortener.models import ShortLink


class AccountTests(APITestCase):
    def setUp(self):
        ShortLink.objects.create(link_id='aaa', url='http://example1.com', status_code=301)
        ShortLink.objects.create(link_id='bbb', url='http://example2.com', status_code=302)
        ShortLink.objects.create(link_id='ccc', url='http://example3.com', status_code=303)

    def test_create_link(self):
        data = {'url': 'http://google.com', 'status_code': 301}
        response = self.client.post('/api/links/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ShortLink.objects.count(), 4)

    def test_delete_link(self):
        self.assertEqual(ShortLink.objects.count(), 3)
        self.client.delete('/api/links/aaa/')
        self.assertEqual(ShortLink.objects.count(), 2)

    def test_change_link(self):
        link = ShortLink.objects.get(link_id='aaa')
        self.assertEqual(link.url, 'http://example1.com')
        data = {'url': 'http://new.com'}
        self.client.patch('/api/links/aaa/', data, format='json')
        link = ShortLink.objects.get(link_id='aaa')
        self.assertEqual(link.url, 'http://new.com')

    def test_redirect(self):
        response = self.client.get("/l/aaa")
        self.assertRedirects(response, 'http://example1.com', status_code=301, fetch_redirect_response=False)

    def test_404(self):
        response = self.client.get("/l/qqqq")
        self.assertEqual(response.status_code, 404)

    def test_get_all(self):
        response = self.client.get("/api/links/")
        data = response.json()
        self.assertEqual(len(data['results']), 3)