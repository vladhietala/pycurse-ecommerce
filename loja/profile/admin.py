# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

    class Media:
        js = (
            "js/site.js",
            "//code.jquery.com/jquery-3.6.0.js",
            "//cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.16/jquery.mask.js",
        )
