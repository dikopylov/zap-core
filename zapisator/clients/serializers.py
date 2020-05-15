from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from clients.models import Client
from users.serializers import UserSerializer


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_password = make_password(validated_data.pop('password'))
        user_model = get_user_model().objects.create(password=user_password, **user_data)

        return Client.objects.create(user=user_model, **validated_data)

    class Meta:
        model = Client
        fields = ['user']
