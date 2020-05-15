from rest_framework import viewsets

from suppliers.executors.human_executors.models import HumanExecutor
from suppliers.executors.human_executors.serializers import HumanExecutorSerializer


class HumanExecutorViewSet(viewsets.ModelViewSet):
    queryset = HumanExecutor.objects.all()
    serializer_class = HumanExecutorSerializer
