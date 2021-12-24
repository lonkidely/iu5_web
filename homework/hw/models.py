from django.db import models


# Create your models here.
class Langs(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    descr = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'langs'


class Opers(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    count_cycles = models.IntegerField(blank=True, null=True)
    lang = models.ForeignKey(Langs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opers'
