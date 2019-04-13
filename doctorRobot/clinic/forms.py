from django.db import models
from django import forms
from clinic.models import  Result,UserProfile


class NameForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'lastName', 'birth_date', 'middle_name', 'gender',
                  'phone_number', 'birth_date']
