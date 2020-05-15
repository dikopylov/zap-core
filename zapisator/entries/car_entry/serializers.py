from rest_framework import serializers

from entries.car_entry.models import CarEntry
from entries.models import Entry
from entries.serializers import EntrySerializer


class CarEntrySerializer(serializers.ModelSerializer):
    entry = EntrySerializer()

    class Meta:
        model = CarEntry
        fields = ['entry']

    def create(self, validated_data):
        car_entry = None
        entry_data = validated_data.pop('entry', None)

        if entry_data is not None:
            entry = Entry.objects.create(**entry_data)
            car_entry = CarEntry.objects.create(entry=entry, **validated_data)

        return car_entry
