from django.db import models

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.drink


# Create your models here.
