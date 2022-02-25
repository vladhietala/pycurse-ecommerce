# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from localflavor.br import models as br_models


class Profile(models.Model):

    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    birth_date = models.DateField(_("birth date"))
    cpf = br_models.BRCPFField(br_models.BRCPFField.description)
    address = models.CharField(_("address"), max_length=50)
    number = models.CharField(_("number"), max_length=5)
    complement = models.CharField(_("complement"), max_length=30, null=True, blank=True)
    neighborhood = models.CharField(_("neighborhood"), max_length=30)
    city = models.CharField(_("city"), max_length=30)
    state = br_models.BRStateField(_("state"))
    postalcode = br_models.BRPostalCodeField(br_models.BRPostalCodeField.description)

    class Meta:
        pass

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})

    def clean(self):
        pass
