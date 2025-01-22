from django.db import models

# Create your models here.

from django.contrib.auth.models import User  # For audit logs

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, unique=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    minimum_stock_level = models.IntegerField(default=10)

    def is_low_stock(self):
        return self.stock_quantity <= self.minimum_stock_level

    def __str__(self):
        return self.name


class StockEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_entries')
    supplier_name = models.CharField(max_length=255)
    batch_number = models.CharField(max_length=255, unique=True)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} units of {self.product.name} from {self.supplier_name}"


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    quantity_sold = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    batch_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity_sold} units of {self.product.name}"


class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    old_value = models.TextField(null=True, blank=True)
    new_value = models.TextField(null=True, blank=True)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_performed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Audit log: {self.action} on {self.product} by {self.performed_by}"

