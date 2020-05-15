from entries.car_entry.models import CarEntry
from entries.filters import BaseEntryFilter


class CarEntryFilter(BaseEntryFilter):
    class Meta(BaseEntryFilter.Meta):
        model = CarEntry
