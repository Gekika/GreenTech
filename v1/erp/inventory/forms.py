from django import forms
from .models import StockEntry, Sale

class StockEntryForm(forms.ModelForm):
    class Meta:
        model = StockEntry
        fields = ['product', 'supplier_name', 'batch_number', 'quantity']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'quantity_sold', 'batch_number']
