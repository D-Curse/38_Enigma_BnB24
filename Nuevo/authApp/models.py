from django.db import models
import uuid

# Create your models here.

class HR(models.Model):
    name = models.CharField(max_length=100, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name