from django.contrib import admin
from django.contrib.auth import get_user_model

from Admin_panel.models import Appointment,Bill,Management_Appointment,Request,Record,Discharge,Admins
 # yor code here..................   

User = get_user_model()
 
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name','email','symptoms','approved']
admin.site.register(Appointment,AppointmentAdmin)

class BillAdmin(admin.ModelAdmin):
    list_display = ['appointment','room_charge','doctor_fee','medicine_charge','other_charge','total']
admin.site.register(Bill,BillAdmin)


class Management_AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient','doctor','date','time']
admin.site.register(Management_Appointment,Management_AppointmentAdmin)


class RequestAdmin(admin.ModelAdmin):
    list_display = ['date','time','message','status']
admin.site.register(Request,RequestAdmin)


class RecordAdmin(admin.ModelAdmin):
    list_display = ['date','time','note']
admin.site.register(Record,RecordAdmin)


class DischargeAdmin(admin.ModelAdmin):
    list_display = ['appointment','data_andtime']
admin.site.register(Discharge,DischargeAdmin)


class AdminsAdmin(admin.ModelAdmin):
    list_display = ['user']
admin.site.register(Admins,AdminsAdmin)

    

