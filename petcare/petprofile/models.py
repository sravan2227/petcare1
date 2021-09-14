from django.db import models


# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(Primarykey=True)
    category_name = models.CharField(max_length=100)
    is_parent = models.BooleanField(default=True)


class PetOwner(models.Model):
    pet_owner_id = models.AutoField(Primarykey=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField()
    address = models.CharField()


class PetProfile(models.Model):
    pet_id = models.AutoField(Primarykey=True)
    cat_id = models.ForeignKey(Category.cat_id, on_delete=models.CASCADE)
    breed_type = models.ForeignKey(Category.cat_id, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50)
    pet_owner_id = models.ForeignKey(PetOwner.pet_owner_id, on_delete=models.CASCADE)
    micro_chip_number = models.CharField()
    uuid = models.UUIDField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)
