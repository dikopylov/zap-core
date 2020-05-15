from rest_framework import serializers

from services.models import Service
from suppliers.executors.models import Executor


class ExecutorSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)

    class Meta:
        model = Executor
        fields = ['id', 'title', 'services']
        ordering = ['-id']
