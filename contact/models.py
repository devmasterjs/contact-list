from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
  code = models.CharField(_("Code"), blank=True, null=True, max_length=8)
  name = models.CharField(_("Name"), blank=False, null=False,max_length=16)
  surname = models.CharField(_("Surname"), blank=True, null=True, max_length=32)
  phone_number = models.CharField(_("Phone number"), blank=False, null=False, max_length=15)
  email = models.EmailField(_("Email"), blank=True, null=True, max_length=254)
  city = models.CharField(_("City"), blank=True, null=True, max_length=50)
  country = models.CharField(_("Country"), default="Brasil", max_length=50)
  sendMessage = models.BooleanField(_("Send message?"), default=True)
  created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
