from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet

from files.models import UserFile
from files.serializers import UserFileSerializer


class UserFileViewSet(ModelViewSet):
    queryset = UserFile.objects.all()
    serializer_class = UserFileSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                        file=self.request.data.get('file'))
