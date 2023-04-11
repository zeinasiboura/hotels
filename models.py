from django.db import models

# Create your models here.


class Hotels(models.Model):
    address = models.CharField(max_length=255)
    categores = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=255)
    postalcode = models.IntegerField()
    province = models.CharField(max_length=255)
    reviews = models.DateTimeField(auto_now=True)
    reviewss = models.IntegerField()
