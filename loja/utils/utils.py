# -*- coding: utf-8 -*-
from django.contrib.humanize.templatetags import humanize


def currency(val, currency_sign="R$"):
    if val:
        str = humanize.intcomma(val)
        return f"{currency_sign} {str}"
    return ""


def total_items(cart):
    return sum([i["quantity"] for i in cart.values()])
