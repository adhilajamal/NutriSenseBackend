from django.urls import path ,include
from .api import Members
from .api import Appointments
from .api.Members import DoctorRegistration , PatientRegistration
from .api.Appointments import get_all_doctors,DoctorDetails,MakeAppointment
from .api.profile import PatientProfile
urlpatterns = [
    
    # path('login', views.login, name='first'),
    path('loginUser',Members.loginUser),
    path('DoctorRegistration', DoctorRegistration), 
    path('PatientRegistration', PatientRegistration), 
    path('get_all_doctors',get_all_doctors),
    path('DoctorDetails',DoctorDetails),
    path('MakeAppointment',MakeAppointment),
    path('PatientProfile',PatientProfile),
    # path('get_all_patients',get_all_patients),
    # path('DoctorProfile',DoctorProfile),
]