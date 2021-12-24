from django.db import models
from django.db.models.deletion import CASCADE

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
        return self.name + self.type

class Vet(models.Model):
    name = models.CharField(max_length=100)
    patient = models.CharField(Pet.name)


    def __str__(self):
        return self.name

class Vaccination(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('Date of Vaccination')

    def __str__(self):
        return self.name + self.date

class VaccinationCard(models.Model):
    patient = models.ForeignKey(Pet, on_delete=CASCADE)
    vaccination = models.ForeignKey(Vaccination, on_delete=CASCADE)

    def __str__(self):
        return self.id

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
