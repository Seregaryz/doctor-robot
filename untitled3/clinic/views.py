from django.http import Http404

from clinic.models import UserProfile,Result,DoctorUser
from django.shortcuts import render, redirect,get_object_or_404
from django.db import IntegrityError


def index(request):
    return render(request, 'clinic/main.html', {})
dict = (
    ('M', 'Man'),
    ('W', 'Women'),
)
def area(request,user_id):

    try:
        user_profile = UserProfile.objects.get(pk=user_id)
    except UserProfile.DoesNotExist:
        raise Http404("Question does not exist")
    сontext = {'name': user_profile.user.first_name,
               'id':user_id,
              'last_name': user_profile.user.last_name,
              'middle_name': user_profile.middle_name,
               'for_header': user_profile.user.first_name + ' ' + user_profile.middle_name + ' ' + user_profile.user.last_name,
                'gender':user_profile.gender,
               'birth_day':user_profile.birth_date,
               'phone_number':user_profile.phone_number,
               }
    return render(request,'clinic/personalArea.html',сontext)