import os

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView

from Admin_panel.models import Appointment

User = get_user_model()
# Create your views here.

def loginpage(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        if User.objects.filter(email=email).exists():
            user = authenticate(email = email, password = password)
            if user:
                login(request, user)
                return redirect(index)
            else:
                msg = "Password Is Wrong please Check it and try again..."       
                return render(request, 'loginpage.html',{'msg':msg})
        msg = "User Not Found..."       
        return render(request, 'loginpage.html',{'msg':msg})
    return render(request,'loginpage.html')


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
  
def doctor(request):
    return render(request,'doctor.html')

def depatments(request):
    return render(request,'depatments.html')
    
def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def get_appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        symptoms = request.POST.get('symptoms')
        approved = request.POST.get('approved')
        Appointment = Appointment(name=name, email=email, password=password, symptoms=symptoms,approved=approved)
        Appointment.save()
        return redirect('loginpage')
    return render(request,'get_appointment.html')

def read_more(request):
    return render(request,'read_more.html')
    

def read_moreone(request):
    return render(request,'read_moreone.html')

def read_moretwo(request):
    return render(request,'read_moretwo.html')
    
    
