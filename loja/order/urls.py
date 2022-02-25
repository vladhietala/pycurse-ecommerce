# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = "order"

urlpatterns = [
    path("", views.PaymentView.as_view(), name="create"),
    path("closeorder/", views.CloseOrderView.as_view(), name="closeorder"),
    path("detail/", views.OrderDetailView.as_view(), name="detail"),
]
