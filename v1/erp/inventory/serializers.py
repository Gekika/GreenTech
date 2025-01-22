from rest_framework import serializers
from .models import Product, StockEntry, Sale, AuditLog

class ProductSerializer(serializers.ModelSerializer):
    low_stock = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'stock_quantity', 'minimum_stock_level', 'low_stock']

    def get_low_stock(self, obj):
        return obj.is_low_stock()

class StockEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockEntry
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
