from django.db import models
from django.utils.translation import gettext_lazy as _


class NotificationVia(models.TextChoices):
    EMAIL = 'EMAIL', _('Email')
