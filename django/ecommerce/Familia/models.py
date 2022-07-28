from django.db import models

# Create your models here.

class Familiares(models.Model):
    name = models.CharField(max_length=150)
    num = models.FloatField()
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
