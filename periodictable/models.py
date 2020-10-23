from django.db import models

# Create your models here.
class ChemElement(models.Model):
    atomic_number = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=2, unique=True)
    period = models.IntegerField(default=0)
    group = models.IntegerField(default=0)
    phase = models.CharField(max_length=100,default="")
    elem_type = models.CharField(max_length=200,default="")

class Language(models.Model):
    iso_code = models.CharField(max_length=2)
    native_name = models.CharField(max_length=200, unique=True)

class ChemElementAltName(models.Model):
    chem_element = models.ForeignKey(ChemElement, on_delete=models.CASCADE, to_field="symbol")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, to_field="native_name")
    alt_name = models.CharField(max_length=200)
