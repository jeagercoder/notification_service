from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template import Template, Context
from django.core.mail import get_connection

from notification.models import Notification

class EmailSender:

    def __init__(self, notification_uuid):
        self.notification = Notification.objects.get(uuid=notification_uuid)

    def __get_connection(self):
        if self.notification.template.email_sender == settings.GENERIC_EMAIL_HOST_USER:
            return get_connection(
                username=settings.GENERIC_EMAIL_HOST_USER,
                password=settings.GENERIC_EMAIL_HOST_PASSWORD,
                fail_silently=True
            )

    def __get_body(self):
        return Template(self.notification.template.content).render(Context(self.notification.context))

    def send(self):
        body = self.__get_body()
        connection = self.__get_connection()
        email = EmailMultiAlternatives(
            subject=self.notification.subject,
            body=body,
            from_email=self.notification.template.email_sender,
            to=[self.notification.user_email],
            connection=connection
        )
        email.attach_alternative(body, 'text/html')
        if email.send() == 1:
            self.notification.status = 1
            self.notification.save()



