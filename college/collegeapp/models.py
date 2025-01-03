from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    contact_email = models.EmailField()
    total_student = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name

