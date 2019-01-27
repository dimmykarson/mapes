from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='report'),
    path('doctor_production/', DoctorProductionJSON.as_view(), name='json_doctor_production'),
    path('load_doctors/', load_doctors, name='load_doctors'),

 ]