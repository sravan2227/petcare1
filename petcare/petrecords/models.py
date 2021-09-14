from django.db import models

from petcare.petprofile.models import PetProfile
from petcare.docprofile.models import DocProfile


# Create your models here.

class MedicalRecord(models.Model):
    med_id = models.AutoField(Primarykey=True)
    pet_id = models.ForeignKey(PetProfile.pet_id, on_delete=models.CASCADE)
    type = models.IntegerField(max_length=100)
    details = models.CharField(max_length=100)
    doctor_id = models.ForeignKey(DocProfile.doctor_id, on_delete=models.CASCADE)


class MedicalRecDocs(models.Model):
    med_id = models.ForeignKey(MedicalRecord.med_id, on_delete=models.CASCADE)
    file_path = models.CharField()


class DewormingSch(models.Model):
    pet_id = models.ForeignKey(PetProfile.pet_id, on_delete=models.CASCADE)
    age = models.IntegerField(max_length=10)
    deworming_date = models.DateField()
    status = models.IntegerField()


class Vaccine(models.Model):
    pet_id = models.ForeignKey(PetProfile.pet_id, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=1000)
    vaccine_date = models.DateField()
    status = models.IntegerField()
    doctor_id = models.ForeignKey(DocProfile.doctor_id, on_delete=models.CASCADE)