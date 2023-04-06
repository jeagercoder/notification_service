from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .serializers import NotificationEmailSerializer


class NotificationViewSet(GenericViewSet):
    serializer_class = NotificationEmailSerializer

    @action(methods=['POST'], detail=False)
    def email(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
