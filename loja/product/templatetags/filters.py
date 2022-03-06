# -*- coding: utf-8 -*-
from django.template import Library

from loja.utils import utils

register = Library()


@register.filter
def currency(val):
    return utils.currency(val)
