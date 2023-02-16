from django.urls import path, include

from . import views

app_name = 'storeProducts'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
]
