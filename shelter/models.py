from django.db import models
import uuid
# Create your models here.

class ShelterModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()

    def __str__(self):
        return self.name