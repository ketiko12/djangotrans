from djang.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.transaction import ugettext_lazy as _
from .managers import 

class Product(models.Model):
    product_id= models.AutoField(primary_key=True)
    product_name= models.CharField(max_length=15)
    price= models.FloatField()

    @classmethod
    def updatedprice(cls, product_id, price):
        product= cls.objects.filter(product_id=product_id).first()
        product.price=price
        product.save()
        return product

    @classmethod
    def create(cls, product_name, price):
        product= Product(product_name=product_name, price= price)
        product.save()
        return product    