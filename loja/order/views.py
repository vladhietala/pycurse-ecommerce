# -*- coding: utf-8 -*-
from django.views import View
from django.views.generic import CreateView, DetailView

from .models import Order


class PaymentView(CreateView):
    model = Order
    template_name = "payment.html"


class CloseOrderView(View):
    pass


class OrderDetailView(DetailView):
    model = Order
    template_name = ".html"
