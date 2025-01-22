from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Product, StockEntry, Sale

class InventoryTests(TestCase):
    def test_low_stock_alert(self):
        product = Product.objects.create(name="Test Product", stock_quantity=5, minimum_stock_level=10)
        self.assertTrue(product.is_low_stock())

    def test_stock_update_on_sale(self):
        product = Product.objects.create(name="Test Product", stock_quantity=100)
        sale = Sale.objects.create(product=product, quantity_sold=10)
        product.refresh_from_db()
        self.assertEqual(product.stock_quantity, 90)
