from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """metadata."""
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "last_login",
            "date_joined",
        )
        read_only_fields = (
            "id",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
        )
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
