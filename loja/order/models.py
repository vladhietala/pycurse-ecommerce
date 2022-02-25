# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    CREATED = 1
    APROVED = 2
    REJECTED = 3
    PENDING = 4
    SENT = 5
    FINISHED = 6
    STATUS = (
        (CREATED, _("Created")),
        (APROVED, _("Aproved")),
        (REJECTED, _("Rejected")),
        (PENDING, _("Pending")),
        (SENT, _("Sent")),
        (FINISHED, _("Finished")),
    )

    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    total = models.DecimalField(_("total"), max_digits=6, decimal_places=2)
    status = models.PositiveSmallIntegerField(
        _("status"), choices=STATUS, default=CREATED
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ("-created_at",)

    def __str__(self):
        return f"Pedido nº {self.pk}"

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.CASCADE)
    product = models.CharField(_("product"), max_length=100)
    product_id = models.PositiveIntegerField(_("product_id"))
    variation = models.CharField(_("variation"), max_length=100)
    variation_id = models.PositiveIntegerField(_("variation_id"))
    price = models.DecimalField(_("price"), max_digits=6, decimal_places=2)
    promotional_price = models.DecimalField(
        _("promotional_price"), max_digits=6, decimal_places=2
    )
    quantity = models.PositiveIntegerField(_("quantity"))
    image = models.CharField(_("image"), max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Order item")
        verbose_name_plural = _("Order items")
        ordering = ("-created_at",)

    def __str__(self):
        return f"Item do {self.order}"

    def save(self, *args, **kwargs):
        super.save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("OrderItem_detail", kwargs={"pk": self.pk})
