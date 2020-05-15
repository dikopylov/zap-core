from rest_framework import viewsets, mixins

from entries.filters import EntryFilter
from entries.models import Entry
from entries.serializers import EntrySerializer


class EntryViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_class = EntryFilter
