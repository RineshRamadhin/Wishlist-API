import uuid
from django.db import models


class Link(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=255)

    class Meta:
        db_table = "link"
