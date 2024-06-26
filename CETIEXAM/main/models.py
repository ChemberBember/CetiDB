from django.db import models


class Country(models.Model):
    CodCountry = models.IntegerField(primary_key=True)
    NameCountry = models.CharField(max_length=50)
    GovType = models.CharField(max_length=50)
    Language = models.CharField(max_length=50)
    Continent = models.CharField(max_length=50)

    def __str__(self):
        return self.NameCountry


class City(models.Model):
    CodCity = models.IntegerField(primary_key=True)
    NameCity = models.CharField(max_length=50)
    CodCountry = models.ForeignKey(Country, on_delete=models.CASCADE)
    Capital = models.BooleanField()

    def __str__(self):
        return self.NameCity