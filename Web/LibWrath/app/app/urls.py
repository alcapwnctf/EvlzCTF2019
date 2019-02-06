"""
    app URL Configuration
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from api import views
from api.models import Device

admin.autodiscover()
admin.site.register(Device)

router = DefaultRouter()
router.register(r'devices', views.DeviceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
