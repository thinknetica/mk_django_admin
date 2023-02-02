from django.db import models

# Create your models here.

from django.db.models import Model, CharField, ImageField, ForeignKey, CASCADE, DO_NOTHING, TextField

class Shop(Model):
    title = CharField(max_length=255)

class Image(Model):
#    src = ImageField('My image')
    title = CharField(max_length=255)
    product = ForeignKey('Product', on_delete=CASCADE)

class Product(Model):
    title = CharField(max_length=255)
    shop = ForeignKey('Shop', on_delete=CASCADE)
