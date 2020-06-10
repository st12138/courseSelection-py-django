from django.db import models
from django.db import models


class Student(models.Model):
    stuName= models.CharField(max_length=5)
    stuClass = models.CharField(max_length=10)
    stuNum = models.IntegerField()
    stuPasswd = models.CharField(max_length=256)
    stuCou = models.TextField(default='')
    def __str__(self):
        return self.stuName


class Course(models.Model):
    couName = models.CharField(max_length=10)
    couTea = models.CharField(max_length=5)
    couId = models.IntegerField(default=0)
    couTime = models.CharField(max_length=30)

    couAllNum = models.IntegerField(default=0)
    couLeftNum = models.IntegerField(default=0)

    couPer = models.TextField(default='')

    def __str__(self):
        return self.couName
# Create your models here.
