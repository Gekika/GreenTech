from django.urls import path
from .views import ProductListView, AddStockView, RecordSaleView, ReportView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('add-stock/', AddStockView.as_view(), name='add-stock'),
    path('record-sale/', RecordSaleView.as_view(), name='record-sale'),
    path('reports/', ReportView.as_view(), name='reports'),
]