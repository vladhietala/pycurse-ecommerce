# -*- coding: utf-8 -*-
from django.contrib import admin

from .forms import ProfileForm
from .models import Profile


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    form = ProfileForm

    class Media:

        js = (
            "js/site.js",
            "//code.jquery.com/jquery-3.6.0.js",
            "//cdnjs.cloudflare.com/ajax/libs/jquery.inputmask/5.0.7/jquery.inputmask.min.js",  # noqa
        )
