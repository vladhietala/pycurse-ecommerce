# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from localflavor.br import models as br_models


class Profile(models.Model):

    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    birth_date = models.DateField(_("birth_date"))
    cpf = br_models.BRCPFField()
    address = models.CharField(_("address"), max_length=50)
    address_number = models.CharField(_("number"), max_length=5)
    address_complement = models.CharField(
        _("complement"), max_length=30, null=True, blank=True
    )
    address_neighborhood = models.CharField(_("neighborhood"), max_length=30)
    address_city = models.CharField(_("city"), max_length=30)
    address_state = br_models.BRStateField()
    address_cep = br_models.BRPostalCodeField()

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})

    def clean(self):
        pass
