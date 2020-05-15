from django_filters import rest_framework as filters

from entries.models import Entry


class BaseEntryFilter(filters.FilterSet):
    ENTRY_NAME = 'entry__'

    client = filters.NumberFilter(field_name=ENTRY_NAME + 'client', lookup_expr='exact')
    free = filters.BooleanFilter(field_name=ENTRY_NAME + 'client', lookup_expr='isnull')
    executor = filters.NumberFilter(field_name=ENTRY_NAME + 'executor', lookup_expr='exact')
    entry_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = None
        fields = (
            'client',
            'free',
            'executor',
            'entry_at'
        )


class EntryFilter(BaseEntryFilter):
    """
        Для базовой записи нужно переопределять поля, в которых встречается `field_name`
    """
    client = filters.NumberFilter(field_name='client', lookup_expr='exact')
    free = filters.BooleanFilter(field_name='client', lookup_expr='isnull')
    executor = filters.NumberFilter(field_name='executor', lookup_expr='exact')

    class Meta(BaseEntryFilter.Meta):
        model = Entry
