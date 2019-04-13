from django.contrib import admin

from clinic.models import Result, UserProfile, DoctorUser

admin.site.register(Result)
admin.site.register(UserProfile)
admin.site.register(DoctorUser)



