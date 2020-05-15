from rest_framework import viewsets

from suppliers.executors.schedules.models import Schedule, LunchBreak
from suppliers.executors.schedules.serializers import ScheduleSerializer, LunchBreakSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class LunchBreakViewSet(viewsets.ModelViewSet):
    queryset = LunchBreak.objects.all()
    serializer_class = LunchBreakSerializer
