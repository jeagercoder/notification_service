from django.template import Template, Context
from celery import shared_task

from .utils import EmailSender


@shared_task
def send_email(notification_uuid):
    email_sender = EmailSender(notification_uuid=notification_uuid)
    email_sender.send()
