
from django.urls import path
from Admin_panel.views import loginpage,index,about,doctor,depatments,blog,contact,get_appointment,read_more,read_moreone,read_moretwo

urlpatterns = [
    path('loginpage',loginpage,name='loginpage'),
    path('about/',about, name='about'),
    path('',index, name='index'),
    path('doctor/',doctor, name='doctor'),
    path('depatments/',depatments, name='depatments'),
    path('blog/',blog, name='blog'),
    path('contact/',contact, name='contact'),
    path("get_appointment/",get_appointment, name='get_appointment'),
    path("read_more/",read_more, name='read_more'),
    path("read_moreone/",read_moreone, name='read_moreone'),
    path("read_moretwo/",read_moretwo, name='read_moretwo'),
    
]


