from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'storeApp',
        'username': 'Erlan Karabaliyev',
        'is_promotion': True
    }
    return render(request, 'storeProducts/index.html', context)


def products(request):
    context = {
        'title': 'Products'
    }
    return render(request, 'storeProducts/products.html', context)