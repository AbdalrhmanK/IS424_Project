from django.db import models

# Create your models here.

class product(models.Model):
    pName = models.CharField(max_length=20)
    nameShop = models.CharField(max_length=20)
    shopContact = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    email = models.EmailField()


class Meta:
    dp_table = "product"