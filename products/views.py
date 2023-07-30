from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'Ara Shop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Ara Shop - Каталог',
    }
    return render(request, 'products/products.html', context)
