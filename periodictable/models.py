from django.db import models

class ChemElement(models.Model):
    atomic_number = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=2, unique=True)
    period = models.IntegerField(default=0)
    group = models.IntegerField(default=0)
    phase = models.CharField(max_length=100,default="")
    elem_type = models.CharField(max_length=200,default="")
    de_name = models.CharField(max_length=200,default="")
    en_name = models.CharField(max_length=200,default="")
    es_name = models.CharField(max_length=200,default="")
    fr_name = models.CharField(max_length=200,default="")
    it_name = models.CharField(max_length=200,default="")
    pt_name = models.CharField(max_length=200,default="")
