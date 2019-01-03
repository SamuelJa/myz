from django.db import models

# Create your models here.
class PorteCarte(models.Model):
    titre = models.CharField(max_length=25)
    description = models.TextField(max_length=100)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    images = models.ImageField(default="static/images/pp.jpg", upload_to='static/images/')

class TehudaZehut(models.Model):
    titre = models.CharField(max_length=25)
    description = models.TextField(max_length=100)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    images = models.ImageField(default="static/images/pp.jpg", upload_to='static/images/')

class Passeport(models.Model):
    titre = models.CharField(max_length=25)
    description = models.TextField(max_length=100)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    images = models.ImageField(default="static/images/pp.jpg", upload_to='static/images/')

