from django.db import models

# Create your models here.
class IceCream(models.Model):
    manufacturer = models.CharField('Производитель', max_length=20)
    flavor = models.CharField('Вкус', max_length=20)

    def __str__(self):
        return self.manufacturer
