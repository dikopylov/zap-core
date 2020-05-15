from rest_framework import serializers

from clients.models import Client
from entries.models import Entry
from services.models import Service
from suppliers.executors.models import Executor


class EntrySerializer(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
    executor = serializers.PrimaryKeyRelatedField(queryset=Executor.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=False)

    class Meta:
        model = Entry
        fields = '__all__'
        ordering = ['-id']
