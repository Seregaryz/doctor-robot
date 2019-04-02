from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.db import models


class Result(models.Model):
    title = models.CharField(max_length=50)


dict = (
    ('M', 'Man'),
    ('W', 'Women'),
)


class Person(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    middleName = models.CharField(max_length=200)

    sex = models.CharField(max_length=1,
                           choices=dict,
                           default='M')
    birth_date = models.DateTimeField('BirthDate')
    results = models.ManyToManyField(Result)
