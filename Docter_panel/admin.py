from django.contrib import admin
from django.contrib.auth import get_user_model
from Docter_panel.models import Doctor,Patient,Docter_Appointment
User = get_user_model()
 # yor code here..................   
 
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user','approved']
admin.site.register(Doctor,DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display = ['user','doctor']
admin.site.register(Patient,PatientAdmin)

class Docter_AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient','doctor','date','time']
admin.site.register(Docter_Appointment,Docter_AppointmentAdmin)

    
    
    