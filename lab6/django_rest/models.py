from django.db import models


class Operator(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название оператора")
    count_cycles = models.IntegerField(verbose_name="Количество тактов ЦП")

    class Meta:
        managed = False
        db_table = 'Operator'


class Proglang(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название языка")

    class Meta:
        managed = False
        db_table = 'ProgLang'
