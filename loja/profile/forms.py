# -*- coding: utf-8 -*-
from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cpf"].widget.attrs.update({"class": "mask-cpf"})
        self.fields["birth_date"].widget.attrs.update({"class": "mask-date no-unmask"})
        self.fields["postalcode"].widget.attrs.update({"class": "mask-cep no-unmask"})
