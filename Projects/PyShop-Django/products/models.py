from django.db import models


class Product(models.Model):
    class Meta:
        db_table = "Products"


    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    class Meta:
        db_table = "Offer"


    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()