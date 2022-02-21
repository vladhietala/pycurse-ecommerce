import os
from pickletools import optimize
from PIL import Image
from io import BytesIO
import sys
from django.conf import settings
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(max_length=30, unique=True)
    mktg_price = models.DecimalField(max_digits=6, decimal_places=2)
    promo_mktg_price = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variable'),
            ('S', 'Simple'),
        )
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @staticmethod
    def resize_image(self, max_image_size=800):
        img_pil = Image.open(self.image)
        original_width, original_height = img_pil.size
        if original_width <= max_image_size:
            print('Image width is smaller than max image size')
            return

        output = BytesIO()
        new_height = round(original_height * max_image_size / original_width)
        resized_img = img_pil.resize((max_image_size, new_height), Image.LANCZOS)
        resized_img.save(
            output,
            format=img_pil.format,
            optimize=True,
            quality=80
        )
        output.seek(0)
        self.image = InMemoryUploadedFile(
            output,
            'ImageField',
            self.image.name,
            img_pil.format,
            sys.getsizeof(output),
            None
        )
        print('Image resized')

    def save(self, *args, **kwargs):
        max_image_size = 800
        if self.image:
            self.resize_image(max_image_size)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
