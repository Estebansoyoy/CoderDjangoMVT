from django.db import models

# Create your models here.

class Distribuidor(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    email = models.EmailField()