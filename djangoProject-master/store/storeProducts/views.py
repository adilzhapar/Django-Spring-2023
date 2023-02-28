from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage

def index(request):
    context = {
        'title': 'storeApp',
        'username': 'Adil Zhapar',
        'is_promotion': True
    }
    return render(request, 'storeProducts/index.html', context)


def products(request, category_id=None):
    if category_id:
        category = ProductCategory.objects.get(id = category_id)
        products = Product.objects.filter(category = category)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 3)
    page = request.GET.get('page', None)
    if page == None or page == "":
        page = 1

    try:
        products = paginator.page(page)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'title' : 'storeApp',
        'products' : products,
        'categories' : ProductCategory.objects.all(),
        'page': page
    }
    return render(request, 'storeProducts/products.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)
    
    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])