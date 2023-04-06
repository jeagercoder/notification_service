from django.db import models

import uuid

from .choices import (
    NotificationVia
)



class Template(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    email_sender = models.EmailField()
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    notification_via = models.CharField(max_length=50, choices=NotificationVia.choices, default=NotificationVia.EMAIL)
    status = models.IntegerField(default=0)

    user_uuid = models.UUIDField()
    user_email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=100)
    context = models.JSONField()

    template = models.ForeignKey(Template, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
