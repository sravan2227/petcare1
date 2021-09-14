from django.contrib import admin
from .models import Category, PetProfile, PetOwner

# Register your models here.

admin.site.register(Category)
admin.site.register(PetProfile)
admin.site.register(PetOwner)
