from rest_framework import mixins, viewsets

from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    authentication_classes = []
    permission_classes = []
