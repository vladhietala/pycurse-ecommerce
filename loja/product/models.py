# -*- coding: utf-8 -*-
import sys
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image


class Product(models.Model):
    VARIABLE = 1
    SIMPLE = 2
    TYPE = ((VARIABLE, _("Variable")), (SIMPLE, _("Simple")))

    product_name = models.CharField(_("product name"), max_length=100)
    short_description = models.TextField(_("short description"), max_length=255)
    long_description = models.TextField(_("long description"))
    image = models.ImageField(
        _("image"), upload_to="images/products/", blank=True, null=True
    )
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    price = models.DecimalField(_("price"), max_digits=6, decimal_places=2)
    promo_price = models.DecimalField(
        _("promotional price"), max_digits=6, decimal_places=2
    )
    type = models.PositiveSmallIntegerField(_("type"), choices=TYPE, default=SIMPLE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ("-created_at",)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        max_image_size = 800
        if self.image:
            self.image = self.resize_image(self.image, max_image_size)

        if not self.slug:
            self.slug = slugify(self.product_name)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product", kwargs={"pk": self.pk})

    @staticmethod
    def resize_image(image, max_image_size=800):
        img_pil = Image.open(image)
        original_width, original_height = img_pil.size
        if original_width <= max_image_size:
            return image

        output = BytesIO()
        new_height = round(original_height * max_image_size / original_width)
        resized_img = img_pil.resize((max_image_size, new_height), Image.LANCZOS)
        resized_img.save(output, format=img_pil.format, optimize=True, quality=80)
        output.seek(0)
        return InMemoryUploadedFile(
            output,
            "ImageField",
            image.name,
            img_pil.format,
            sys.getsizeof(output),
            None,
        )


class Variation(models.Model):
    product = models.ForeignKey(
        verbose_name=_("product"),
        to=Product,
        on_delete=models.CASCADE,
    )
    variation_name = models.CharField(_("name"), max_length=50, blank=True, null=True)
    price = models.DecimalField(_("price"), max_digits=6, decimal_places=2)
    promo_price = models.DecimalField(
        _("promotional price"), max_digits=6, decimal_places=2, blank=True, null=True
    )
    stock = models.PositiveIntegerField(_("stock"), default=0)

    class Meta:
        ordering = ("-price",)
        verbose_name_plural = _("variations")
        verbose_name = _("variation")

    def __str__(self):
        return self.variation_name or self.product.product_name

    def get_price(self):
        if self.promo_price > 0:
            return self.promo_price
        else:
            return self.price
