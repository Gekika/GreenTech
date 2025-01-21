from django.shortcuts import render

# Create your views here.


def show_inventory(request):
    return render(request, 'inventory/inventory.html')

# inventory/views.py
from django.shortcuts import render, redirect
from .models import StockEntry, Product
from .forms import StockEntryForm

def add_stock_entry(request):
    if request.method == 'POST':
        form = StockEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_dashboard')
    else:
        form = StockEntryForm()
    return render(request, 'toy_store/add_stock_entry.html', {'form': form})

def stock_dashboard(request):
    products = Product.objects.all()
    return render(request, 'toy_store/stock_dashboard.html', {'products': products})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, StockEntry, Sale
from .forms import ProductForm, StockEntryForm, SaleForm

def inventory_dashboard(request):
    products = Product.objects.all()
    total_stock = sum([product.stock_quantity for product in products])
    return render(request, 'inventory/dashboard.html', {
        'products': products,
        'total_stock': total_stock,
    })

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_dashboard')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def add_stock_entry(request):
    if request.method == 'POST':
        form = StockEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_dashboard')
    else:
        form = StockEntryForm()
    return render(request, 'inventory/add_stock_entry.html', {'form': form})

def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_dashboard')
    else:
        form = SaleForm()
    return render(request, 'inventory/add_sale.html', {'form': form})
