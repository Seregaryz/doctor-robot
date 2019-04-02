from django.db import models
from django import forms
from clinic.models import Person, Result


class NameForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'lastName ', 'birth_date']
