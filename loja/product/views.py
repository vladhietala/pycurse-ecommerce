# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.text import format_lazy
from django.utils.translation import gettext as _
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
        # del self.request.session["cart"]
        # self.request.session.save()

        referer = self.request.META.get("HTTP_REFERER", reverse("product:list"))
        var_id = self.request.GET.get("vid")
        if not var_id:
            messages.error(self.request, _("product doesn't exist").capitalize())
            return redirect(referer)
        var = get_object_or_404(Variation, id=var_id)
        var_stock = var.stock
        product = var.product
        product_id = product.id
        product_name = product.product_name
        variation_name = var.variation_name or ""
        variation_id = var.id
        unit_price = var.price
        unit_price_promo = var.promo_price or None
        total_price = var.price
        total_price_promo = var.promo_price or None
        quantity = 1
        slug = product.slug
        image = product.image

        if not self.request.session.get("cart"):
            self.request.session["cart"] = {}
            self.request.session.save()

        cart = self.request.session["cart"]

        if var.stock < 1:
            messages.error(self.request, _("not enough stock").capitalize())
            return redirect(referer)

        if var_id in cart:
            cart_qty = cart[var_id]["quantity"]
            cart_qty += 1
            if var_stock < cart_qty:
                str1 = _("not enought stock for").capitalize()
                str2 = _("added")
                str3 = _("items")
                messages.warning(
                    self.request,
                    format_lazy(
                        "{} {} {} {}, {} {} {}",
                        str1,
                        cart_qty,
                        product_name,
                        variation_name,
                        str2,
                        var_stock,
                        str3,
                    ),
                )
            cart_qty = var_stock
            cart[var_id]["quantity"] = cart_qty
            cart[var_id]["total_price"] = cart_qty * unit_price
            cart[var_id]["total_price_promo"] = (
                unit_price_promo * cart_qty if unit_price_promo is not None else None
            )

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
                "slug": slug,
                "image": image,
            }
        self.request.session.save()
        str1 = _("product").capitalize()
        str2 = _("added to cart")
        messages.success(
            self.request,
            format_lazy("{} {} {} {}", str1, product_name, variation_name, str2),
        )
        return redirect(referer)


class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        var_id = kwargs.get("vid")
        referer = self.request.META.get("HTTP_REFERER", reverse("product:list"))
        cart = self.request.session["cart"]
        if not var_id or var_id not in cart:
            return redirect(referer)

        str1 = _("product").capitalize()
        str2 = _("removed from cart")
        messages.success(
            self.request,
            format_lazy(
                "{} {} {} {}",
                str1,
                cart[var_id]["product_name"],
                cart[var_id]["variation_name"],
                str2,
            ),
        )
        del cart[var_id]
        self.request.session.save()
        return redirect(referer)


class Cart(View):
    def get(self, *args, **kwargs):
        return render(self.request, "product/cart.html")


class Checkout(View):
    pass
