# -*- coding: utf-8 -*-
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, reverse
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Product, Variation


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    paginate_by = 12


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    slug_url_kwarg = "slug"


class AddToCart(View):
    def get(self, *args, **kwargs):
        referer = self.request.META.get("HTTP_REFERER", reverse("product:list"))
        var_id = self.request.GET.get("vid")
        if not var_id:
            messages.error(self.request, "Produto inexistente")
            return redirect(referer)
        var = get_object_or_404(Variation, id=var_id)

        if not self.request.session.get("cart"):
            self.request.session["cart"] = {}
            self.request.session.save()

        cart = self.request.session["cart"]

        if var_id in cart:
            # TODO Varicao não existe no carrinho
            pass
        else:
            # TODO Varicao existe no carrinho
            pass
        return HttpResponse(f"{var.product} - {var.variation_name}")


class RemoveFromCart(View):
    pass


class Cart(View):
    pass


class Checkout(View):
    pass
