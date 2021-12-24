from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length = 60)
    password = models.CharField(max_length = 12)

    def __str__(self):
        return self.email

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField(default = 0)

    def __str__(self):
        return self.name, self.type

class VaccinationCard(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vaccination = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.id, Pet.name

class Vet(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.id

