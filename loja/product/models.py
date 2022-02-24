# -*- coding: utf-8 -*-
import sys
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from PIL import Image


class Product(models.Model):

    product_name = models.CharField(max_length=100)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    slug = models.SlugField(max_length=30, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promo_price = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(
        default="V",
        max_length=1,
        choices=(
            ("V", "Variable"),
            ("S", "Simple"),
        ),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Produtos"
        verbose_name = "Produto"

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        max_image_size = 800
        if self.image:
            self.image = self.resize_image(self.image, max_image_size)
        super().save(*args, **kwargs)

    @staticmethod
    def resize_image(image, max_image_size=800):
        img_pil = Image.open(image)
        original_width, original_height = img_pil.size
        if original_width <= max_image_size:
            return

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promo_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ("-price",)
        verbose_name_plural = "Variações"
        verbose_name = "Variação"

    def __str__(self):
        return self.name or self.product.product_name

    def get_price(self):
        if self.promo_price > 0:
            return self.promo_price
        else:
            return self.price
