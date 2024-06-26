from django.urls import path ,include
from .api import Members
from .api import Appointments
from .api.Members import DoctorRegistration , PatientRegistration,logoutUser
from .api.Appointments import get_all_doctors,DoctorDetails,MakeAppointment,appointmentDetails,doctorsAppoitment
from .api.profile import PatientProfile,patientChangePassword,DoctorProfile,doctorChangePassword,updatePatientProfile,updateDoctorProfile
urlpatterns = [
    
    # path('login', views.login, name='first'),
    path('loginUser',Members.loginUser),
    path('logoutUser',logoutUser),
    path('DoctorRegistration', DoctorRegistration), 
    path('PatientRegistration', PatientRegistration), 
    path('get_all_doctors',get_all_doctors),
    path('DoctorDetails',DoctorDetails),
    path('MakeAppointment',MakeAppointment),
    path('PatientProfile',PatientProfile),
    path('patientChangePassword',patientChangePassword),
    path('DoctorProfile',DoctorProfile),
    path('doctorChangePassword',doctorChangePassword),
    path('updatePatientProfile',updatePatientProfile),
    path('updateDoctorProfile',updateDoctorProfile),
    path('appointmentDetails',appointmentDetails),
    path('doctorsAppoitment',doctorsAppoitment),
    # path('get_all_patients',get_all_patients),
    # path('DoctorProfile',DoctorProfile),
]