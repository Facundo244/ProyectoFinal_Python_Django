from django.db import models
from datetime import date

# Create your models here.


class Post(models.Model):

    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=2000)
    autor = models.CharField(max_length=50)
    fecha = models.DateField(default=date.today)

    def __str__(self):
        return f'{self.titulo} by {self.autor}'



