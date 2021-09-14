from django.db import models


# Create your models here.

class HospitalDetails(models.Model):
    hospital_id = models.CharField(max_length=100, Primarykey=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)


class DocProfile(models.Model):
    doctor_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    hospital_id = models.ForeignKey(HospitalDetails.hospital_id, on_delete=models.CASCADE)
