# -*- coding: utf-8 -*-
from django.template import Library

from loja.utils import utils

register = Library()


@register.filter
def money(val):
    return utils.money(val)
