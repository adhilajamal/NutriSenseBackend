from django.contrib import admin
from .models import Doctor , Patient ,Appointment

# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = [ 'id','user_name','email']
class DoctorAdmin(admin.ModelAdmin):
    fields = ('user_name','age','gender','contact','email','pwd','about','address','district','workingtime','qualification','proof','doctorverify','profile')
admin.site.register(Doctor,DoctorAdmin)
class PatientAdmin(admin.ModelAdmin):
    fields = ('user_name','age','gender','contact','email','pwd','profile')
admin.site.register(Patient,PatientAdmin)
class AppointmentAdmin(admin.ModelAdmin):
    fields = ('dr_name','patient_name','date','time','place','contact_no','patient_email')
admin.site.register(Appointment,AppointmentAdmin)