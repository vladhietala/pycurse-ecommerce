# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = "product"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),
    path("<slug>", views.ProductDetailView.as_view(), name="detail"),
    path("add-to-cart/", views.AddToCart.as_view(), name="addtocart"),
    path("remove-from-cart/", views.RemoveFromCart.as_view(), name="removefromcart"),
    path("cart/", views.Cart.as_view(), name="cart"),
    path("checkout/", views.Checkout.as_view(), name="checkout"),
]
