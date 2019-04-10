from django.contrib.auth.models import User
from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.db import models



dict = (
    ('M', 'Man'),
    ('W', 'Women'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,
        primary_key=True)
    middle_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1,
                           choices=dict,
                           default='M')
    birth_date = models.DateTimeField('BirthDate')
    phone_number = models.CharField(max_length=12)

    def is_member(self,gr):
        return self.groups.filter(name=gr).exists()
class DoctorUser(models.Model):
    doctor = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Доктор', related_name="rates_from",default="")
    patient = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Пациент', related_name="rates_to", default="")

class Result(models.Model):
    Res = models.IntegerField()
    Patient = models.OneToOneField(UserProfile,on_delete=models.CASCADE,
        primary_key=True)



