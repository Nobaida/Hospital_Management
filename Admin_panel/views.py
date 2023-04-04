import os
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView
from Admin_panel.models import Appointment, Bill
from django.contrib import messages
from django.db.models import Q
# from .models import Appointment, Patient, Doctor
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
        symptoms = request.POST.get('symptoms')
        Appointment = Appointment(name=name, email=email, symptoms=symptoms)
        Appointment.save()
        return redirect('loginpage')
    return render(request,'get_appointment.html')

def read_more(request):
    return render(request,'read_more.html')

def read_moreone(request):
    return render(request,'read_moreone.html')

def read_moretwo(request):
    return render(request,'read_moretwo.html')
    
    
@login_required(login_url='login') # login required decorator
def admin_panel(request):
    pass
    # # If user is not superuser, redirect to home page
    # if not request.user.is_superuser:
    #     return redirect('home')
    # # Get all appointments
    # appointments = Appointment.objects.all()
    # # Get all patients
    # patients = Patient.objects.all()
    # # Get all doctors
    # doctors = Doctor.objects.all()
    # # Get all bills
    # bills = Bill.objects.all()
    # # Get pending, approved and declined appointments
    # pending_appointments = Appointment.objects.filter(status='pending')
    # approved_appointments = Appointment.objects.filter(status='approved')
    # declined_appointments = Appointment.objects.filter(status='declined')
    # # Get pending, approved and declined bills
    # pending_bills = Bill.objects.filter(status='pending')
    # approved_bills = Bill.objects.filter(status='approved')
    # declined_bills = Bill.objects.filter(status='declined')
    # # Render admin panel page with data
    # return render(request, 'admin_panel.html', {'appointments': appointments,
    #                                             'patients': patients,
    #                                             'doctors': doctors,
    #                                             'bills': bills,
    #                                             'pending_appointments': pending_appointments,
    #                                             'approved_appointments': approved_appointments,
    #                                             'declined_appointments': declined_appointments,
    #                                             'pending_bills': pending_bills,
    #                                             'approved_bills': approved_bills,
    #                                             'declined_bills': declined_bills})
    
    
    
    
    
    
    


    