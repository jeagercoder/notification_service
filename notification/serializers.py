from rest_framework import serializers

from .models import Notification, Template
from .tasks import send_email


class NotificationEmailSerializer(serializers.Serializer):
    template_name = serializers.CharField(write_only=True)

    user_uuid = serializers.UUIDField(write_only=True)
    user_email = serializers.EmailField(write_only=True)

    subject = serializers.CharField(write_only=True)
    context = serializers.JSONField(write_only=True)

    def create(self, validated_data):
        template = Template.objects.get(name=validated_data.get('template_name'))

        instance = Notification()
        instance.template = template
        instance.user_uuid = validated_data.get('user_uuid')
        instance.user_email = validated_data.get('user_email')
        instance.subject = validated_data.get('subject')
        instance.context = validated_data.get('context')
        instance.save()

        send_email.delay(instance.uuid)

        return instance

    def to_representation(self, instance):
        return {'success': True}




