
from django.urls import path
from Docter_panel.views import patient_detail

urlpatterns = [
    
    path('patient_detail/',patient_detail, name='patient_detail'),
    # path('doctor_approval/',doctor_approval, name='doctor_approval'),
    # path('doctor_detail/',doctor_detail, name='doctor_detail'),
    # path("appointment_create/",appointment_create,name='appointment_create'),
    
    
    

 
]
