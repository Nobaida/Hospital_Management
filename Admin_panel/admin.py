from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()
from Admin_panel.models import Appointment
 # yor code here..................   
 
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name','email','password','symptoms','approved']
admin.site.register(Appointment,AppointmentAdmin)


    