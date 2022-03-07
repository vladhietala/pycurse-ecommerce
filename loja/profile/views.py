# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView

from .models import Profile

# Create your views here.


def index(request):
    return render(request, "index.html")


class ProfileCreateView(CreateView):
    model = Profile
    template_name = ".html"


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = ".html"


class LoginView(View):
    pass


class LogoutView(View):
    pass
