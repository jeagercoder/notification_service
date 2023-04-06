
from rest_framework.routers import SimpleRouter

from .views import NotificationViewSet

router = SimpleRouter(trailing_slash=False)
router.register('', NotificationViewSet, basename='notification')

urlpatterns = [] + router.urls
