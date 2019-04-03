from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'clinic'

urlpatterns = [
	path('patient_office/<String:patient_id>',views.patient_office,name = 'patient_office'),
	path('doctor_office/<String:doctor_id>',views.doctor_office,name = 'doctor_office'),
	path('home_page',views.home_page,name = 'home_page'),

]