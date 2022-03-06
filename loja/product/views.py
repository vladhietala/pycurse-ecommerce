# -*- coding: utf-8 -*-
from pprint import pprint

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.translation import gettext_lazy as _
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
            messages.error(self.request, _("Product doesn't exist"))
            return redirect(referer)
        var = get_object_or_404(Variation, id=var_id)
        var_stock = var.stock
        product = var.product
        product_id = product.id
        product_name = product.product_name
        variation_name = var.variation_name or ""
        variation_id = var.id
        unit_price = var.price
        unit_price_promo = var.promo_price
        total_price = var.price
        total_price_promo = var.promo_price
        quantity = 1
        slug = product.slug
        image = product.image

        if not self.request.session.get("cart"):
            self.request.session["cart"] = {}
            self.request.session.save()

        cart = self.request.session["cart"]

        if var.stock < 1:
            messages.error(self.request, _("Not enough stock"))
            return redirect(referer)

        if var_id in cart:
            cart_qty = cart[var_id]["quantity"]
            cart_qty += 1
            if var_stock < cart_qty:
                messages.warning(
                    self.request,
                    _(
                        f"Not enought stock for {0} {1}, added {1} itens",
                        cart_qty,
                        product_name,
                        var_stock,
                    ),
                )
                cart_qty = var_stock
            cart[var_id]["quantity"] = cart_qty
            cart[var_id]["total_price"] = cart_qty * unit_price
            cart[var_id]["total_price_promo"] = cart_qty * total_price_promo
        else:
            cart[var_id] = {
                "product_id": product_id,
                "product_name": product_name,
                "variation_name": variation_name,
                "variation_id": variation_id,
                "unit_price": unit_price,
                "unit_price_promo": unit_price_promo,
                "total_price": total_price,
                "total_price_promo": total_price_promo,
                "quantity": quantity,
                "slug ": slug,
                "image": image,
            }
        self.request.session.save()
        pprint(cart)
        messages.success(
            self.request, _(f"Product {product_name} {variation_name} added to cart")
        )
        return redirect(referer)


class RemoveFromCart(View):
    pass


class Cart(View):
    def get(self, *args, **kwargs):
        return render(self.request, "product/cart.html")


class Checkout(View):
    pass
