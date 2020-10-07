from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Country(models.Model):
    seq = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=20, verbose_name="국가명")

    def __str__(self):
        return self.country_name



class Customer(models.Model):
    seq = models.AutoField(primary_key=True)
    age = models.IntegerField(verbose_name="나이")
    sex = models.CharField(max_length=6, verbose_name="성별")
    name = models.CharField(max_length=10, verbose_name="이름")
    nation = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

