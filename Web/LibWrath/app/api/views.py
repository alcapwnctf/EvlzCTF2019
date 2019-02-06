"""
    Views for:
        - Device API
"""

from django.http import Http404

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from api.serializers import DeviceSerializer
from api.models import Device

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class DeviceViewSet(viewsets.ModelViewSet):
    """
        Device CRUD View Set
    """
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
        elif self.action == 'list':
            permission_classes = [IsAdminUser, TokenHasReadWriteScope]
        else:
            permission_classes = [IsAdminUser, TokenHasReadWriteScope]
        
        return [permission() for permission in permission_classes]

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'uuid'