from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

from rest_framework import generics, permissions, serializers

from api.models import Device
from api.helpers import GenerateUUID

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                },
            }

class DeviceSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Device
        fields = ['user', 'uuid', 'status', 'last_tick']
        extra_kwargs = {
            'uuid': {
                'read_only': True
            }
        }
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['password'] = make_password(user_data['password']) # Hash Password

        uuid = GenerateUUID(user_data.get('username')) 

        user = UserSerializer.create(UserSerializer(), validated_data=user_data)

        device, created = Device.objects.update_or_create(user=user, uuid=uuid, **validated_data)

        return device