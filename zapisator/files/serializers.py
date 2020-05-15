from rest_framework import serializers

from files.models import UserFile


class UserFileSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = UserFile
        fields = '__all__'
