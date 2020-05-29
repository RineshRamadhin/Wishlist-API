from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        """
        metadata
        """
        model = Link
        fields = (
            "id",
            "created_at",
            "link",
        )
        read_only_fields = (
            "id",
            "created_at",
        )

