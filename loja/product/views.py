# -*- coding: utf-8 -*-
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    paginate_by = 12


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    # template_name = "product_detail.html"


class AddToCart(View):
    pass


class RemoveFromCart(View):
    pass


class Cart(View):
    pass


class Checkout(View):
    pass
