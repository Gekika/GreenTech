from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)  # Optional
    subcategory = models.ForeignKey('Subcategory', on_delete=models.SET_NULL, null=True, blank=True)  # Optional
    product_name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    minimum_stock_level = models.IntegerField()

    def __str__(self):
        return self.product_name

class StockEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=255)
    lot_number = models.CharField(max_length=255)
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    supplier_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Batch {self.batch_number} - {self.product.product_name}"

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    sale_date = models.DateField(auto_now_add=True)
    batch_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Sale of {self.quantity_sold} units of {self.product.product_name}"

class Report(models.Model):
    report_date = models.DateField(auto_now_add=True)
    data = models.TextField()

    def __str__(self):
        return f"Report on {self.report_date}"