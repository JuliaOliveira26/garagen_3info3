from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100)
    nacioinalidade = models.CharField(max_length=50, null=True, blank=True)
 

    def __str__(self):
        return self.nome.upper() 