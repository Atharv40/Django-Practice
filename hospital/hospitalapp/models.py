from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=100)
    hospitals = models.ManyToManyField(Hospital, related_name="doctors")

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    ailment = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Administrative(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

