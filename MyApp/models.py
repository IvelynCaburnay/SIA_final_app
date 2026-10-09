from django.db import models


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    health_status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pet_name} ({self.pet_type})"