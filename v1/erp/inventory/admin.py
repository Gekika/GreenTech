from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Subcategory, Product, StockEntry, Sale, AuditLog

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(StockEntry)
admin.site.register(Sale)
admin.site.register(AuditLog)
