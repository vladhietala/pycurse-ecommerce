# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    paginate_by = 12


# class ProductDetailView(DetailView):
#     model = Product
#     context_object_name = "product"


class ProductDetailView(View):
    def get(self, request, *args, **kwargs):

        response = f"<p>BASE_DIR: {settings.BASE_DIR}</p>"
        response += f"<p>LOCALE_PATHS: {settings.LOCALE_PATHS}</p>"
        response += f"<p>Current language: {translation.get_language ()}</p>"
        response += "<h1>" + _("Welcome to our page") + "!</h1>"
        response += "<p>" + _("Postal Code") + "</p>"
        return HttpResponse(response)


class AddToCart(View):
    pass


class RemoveFromCart(View):
    pass


class Cart(View):
    pass


class Checkout(View):
    pass
