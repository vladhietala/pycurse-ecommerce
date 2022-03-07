# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Product, Variation


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "short_description",
        "price",
        "promo_price",
    )
    inlines = [VariationInline]
    exclude = ("slug",)


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    pass
