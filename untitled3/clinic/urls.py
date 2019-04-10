from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'clinic'

urlpatterns = [
    path('', views.index, name='index'),
    path('aaa/<int:user_id>', views.area, name='area'),

]
