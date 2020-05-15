from rest_framework import serializers

from suppliers.executors.human_executors.models import HumanExecutor
from suppliers.executors.models import Executor
from suppliers.executors.serializers import ExecutorSerializer


class HumanExecutorSerializer(serializers.ModelSerializer):
    executor = ExecutorSerializer()

    class Meta:
        model = HumanExecutor
        fields = '__all__'
        ordering = ['-id']

    def create(self, validated_data):
        executor_data = validated_data.pop('executor', None)
        executor_services = executor_data.pop('services', None)

        executor = Executor.objects.create(**executor_data)

        for service in executor_services:
            executor.services.add(service)

        executor.save()

        human_executor = HumanExecutor.objects.create(executor=executor, **validated_data)

        return human_executor
