from rest_framework import serializers

from suppliers.executors.models import Executor
from suppliers.executors.schedules.models import LunchBreak, Schedule


class LunchBreakSerializer(serializers.ModelSerializer):
    schedule = serializers.PrimaryKeyRelatedField(queryset=Schedule.objects.all())

    class Meta:
        model = LunchBreak
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    lunch_breaks = LunchBreakSerializer(many=True, read_only=True)
    executor = serializers.PrimaryKeyRelatedField(queryset=Executor.objects.all())

    class Meta:
        model = Schedule
        fields = '__all__'
