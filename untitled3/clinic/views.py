from django.shortcuts import get_object_or_404, render

from .models import Client, Doctor


def home_page(request):
	return render()
	
	
def doctor_office(request,doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
	return render(request,'clinic/doctor_office/doctor.html', {'doctor': doctor})
	
	
def patient_office(request,patient_id):
    patient = get_object_or_404(Client, pk=patient_id)
	return render(request,'clinic/patient_office/patient.html', {'patient': patient})