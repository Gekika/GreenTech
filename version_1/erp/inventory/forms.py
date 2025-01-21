# toy_store/forms.py
from django import forms
from .models import StockEntry, Product

from django import forms
from .models import Category, Subcategory, Product, StockEntry, Sale

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['category', 'name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'product_name', 'unit_price', 'stock_quantity', 'minimum_stock_level']

class StockEntryForm(forms.ModelForm):
    class Meta:
        model = StockEntry
        fields = ['product', 'batch_number', 'lot_number', 'quantity', 'supplier_name']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'quantity_sold', 'batch_number']
