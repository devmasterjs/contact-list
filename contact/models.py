from django.db import models
from django.utils.translation import pgettext_lazy as _


class Contact(models.Model):
  code = models.CharField(_("code"), max_length=50)
  created_at = models.DateTimeField(_("created at"), auto_now_add=True)
  updated_at = models.DateTimeField(_("updated at"), auto_now=True)
