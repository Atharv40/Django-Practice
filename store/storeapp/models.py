from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_email = models.EmailField()
    opening_hours = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
