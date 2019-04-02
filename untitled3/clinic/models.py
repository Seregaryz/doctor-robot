from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.db import models


class Result(models.Model):
    title = models.CharField(max_length=50)

class Person(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    birth_date = models.DateTimeField('BirthDate')




