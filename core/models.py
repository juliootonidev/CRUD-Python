from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    # outros campos...

# Create your models here.
