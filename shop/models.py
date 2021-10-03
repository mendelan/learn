from django.db import models
from django.db.models.fields import CharField

class Product(models.Model):
    class Category(models.TextChoices):
        SPORT = 'Sport', ('Sport')
        HIKE = 'Hike', ('Hike')
        FOR_CHILDREN = 'For_Children', ('For children')
        CARS = 'Cars', ('Cars')
    class Currency(models.TextChoices):
        DOLLAR = 'USD', ('Dollar')
        GRIVNA = 'UAH', ('Grivna')
        RUBLES = 'RUB', ('Rubles')
        EURO = 'EUR', ('Euro')
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    currency = models.CharField(
        max_length=255, 
        choices=Currency.choices,
        default=Currency.GRIVNA,
    )
    photo = models.ImageField()
    brand = models.ForeignKey(
        to = 'shop.Brand', on_delete= models.CASCADE
    )
    category = models.CharField(
        max_length=255,
        choices=Category.choices,
        default=Category.SPORT,   
    )
    def __str__(self):
        return f'ID: {self.id}, NAME: {self.name}'


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} ({ self.id })'


    