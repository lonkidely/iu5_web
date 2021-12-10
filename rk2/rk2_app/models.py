from django.db import models


# Create your models here.
class Langs(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название ЯП')
    descr = models.CharField(max_length=200, verbose_name='Описание')

    class Meta:
        managed = False
        db_table = 'langs'


class Opers(models.Model):
    title = models.CharField(max_length=10, verbose_name='Название оператора')
    lang = models.ForeignKey(Langs, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'opers'
