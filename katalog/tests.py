from django.test import TestCase
from katalog.models import CatalogItem
# Create your tests here.
class KatalogTestCase(TestCase):
    def setUp(self):
        CatalogItem.objects.create(item_name="Test Item", item_price=2000000, item_stock=999, description="Test description", rating=6, item_url="https://www.tokopedia.com/")

    def test_this(self):
        test = CatalogItem.objects.get(item_name="Test Item")
        self.assertTrue(test.item_price, 2000000)