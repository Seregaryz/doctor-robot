from django.contrib import admin

from .models import Symptom, Disease, Specification

admin.site.register(Symptom)
admin.site.register(Disease)
admin.site.register(Specification)
