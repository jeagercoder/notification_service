from django.urls import path, include


urlpatterns = [
    path('notification/', include(('notification.urls', 'notification'), namespace='notification'))
]