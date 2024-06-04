from django.db import models

# Create your models here.
class addAuto(models.Model):
    price = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    count = models.IntegerField()
    year = models.DateField(format('%YY'))
    image = models.ImageField(upload_to='image/')
