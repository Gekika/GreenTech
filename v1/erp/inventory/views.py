from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product, StockEntry, Sale, AuditLog
from .serializers import ProductSerializer, StockEntrySerializer, SaleSerializer

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class AddStockView(APIView):
    def post(self, request):
        serializer = StockEntrySerializer(data=request.data)
        if serializer.is_valid():
            stock_entry = serializer.save()
            product = stock_entry.product
            product.stock_quantity += stock_entry.quantity
            product.save()
            AuditLog.objects.create(
                action="Added stock",
                product=product,
                new_value=f"Stock added: {stock_entry.quantity}",
                performed_by=request.user
            )
            return Response({"message": "Stock added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecordSaleView(APIView):
    def post(self, request):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            sale = serializer.save()
            product = sale.product
            if product.stock_quantity >= sale.quantity_sold:
                product.stock_quantity -= sale.quantity_sold
                product.save()
                AuditLog.objects.create(
                    action="Sale recorded",
                    product=product,
                    new_value=f"Sale: {sale.quantity_sold}",
                    performed_by=request.user
                )
                return Response({"message": "Sale recorded successfully"}, status=status.HTTP_201_CREATED)
            return Response({"error": "Insufficient stock"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportView(APIView):
    def get(self, request):
        # Logic for generating weekly and monthly reports
        # This could involve aggregating data from StockEntry and Sale
        pass
