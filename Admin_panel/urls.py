
from django.urls import path
from Admin_panel.views import loginpage,my_dasbordpage,about_us,Contact_us,admin_page,contacet_page,index,about,doctor,depatments

urlpatterns = [
    path('',loginpage,name='loginpage'),
    path("my_dasbordpage/",my_dasbordpage, name='my_dasbordpage'),
    path('about_us/',about_us, name='about_us'),
    path('Contact_us/',Contact_us, name='Contact_us'),
    path('admin_page/',admin_page, name='admin_page'), 
    path('contacet_page/',contacet_page, name='contacet_page'),
 
    
    path('about/',about, name='about'),
    path('index/',index, name='index'),
    path('doctor/',doctor, name='doctor'),
    path('depatments/',depatments, name='depatments'),
    
    
]

