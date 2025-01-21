from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Subcategory, Product, StockEntry, Sale, Report

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'subcategory', 'unit_price', 'stock_quantity', 'minimum_stock_level')

@admin.register(StockEntry)
class StockEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'batch_number', 'quantity', 'date_added', 'supplier_name')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity_sold', 'sale_date', 'batch_number')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_date', 'data')
