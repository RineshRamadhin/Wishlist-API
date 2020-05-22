from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings

from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        if (
                "X-temporary-token" in request.headers
                and request.headers["X-temporary-token"] == settings.DJANGO_TEMPORARY_TOKEN
        ):
            return super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False)
    def latest(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).order_by("-created_at")[:25]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
