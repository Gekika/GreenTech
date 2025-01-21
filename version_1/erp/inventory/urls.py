from django.urls import path
from . import views

urlpatterns = [
    path('add_stock/', views.add_stock_entry, name='add_stock_entry'),
    path('dashboard/', views.stock_dashboard, name='stock_dashboard'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_dashboard, name='inventory_dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-stock-entry/', views.add_stock_entry, name='add_stock_entry'),
    path('add-sale/', views.add_sale, name='add_sale'),
]
