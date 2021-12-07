from django.db import models


class Operator(models.Model):
    name = models.CharField(max_length=30)
    count_cycles = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Operator'


class Proglang(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'ProgLang'
