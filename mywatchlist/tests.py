from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class WatchlistTestCase(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_by_destination_html(self):
        res = self.client.get('/mywatchlist/html/')
        self.assertEqual(res.status_code, 200)

    def test_get_by_destination_xml(self):
        res = self.client.get('/mywatchlist/xml/')
        self.assertEqual(res.status_code, 200)

    def test_get_by_destination_json(self):
        res = self.client.get('/mywatchlist/json/')
        self.assertEqual(res.status_code, 200)

    def test_get_html(self):
        res = self.client.get(reverse('mywatchlist:show_mywatchlist'))
        self.assertEqual(res.status_code, 200)

    def test_get_xml(self):
        res = self.client.get(reverse('mywatchlist:show_mywatchlist_xml'))
        self.assertEqual(res.status_code, 200)

    def test_get_json(self):
        res = self.client.get(reverse('mywatchlist:show_mywatchlist_json'))
        self.assertEqual(res.status_code, 200)
