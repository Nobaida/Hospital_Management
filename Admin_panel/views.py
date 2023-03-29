from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
# from Admin_panel.models import
import os 
User = get_user_model()


# from .models import Admin, Patient, Doctor, Appointment, Bill
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
                return redirect(my_dasbordpage)
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
    
    
  
  
  
  
  
  
  
  
  

def my_dasbordpage(request):
    return render(request,'my_dasbordpage.html')

def about_us(request):
    return render(request, 'about_us.html')

def Contact_us(request):
    return render(request, 'Contact_us.html')


def admin_page(request):
    return render(request, 'admin_page.html')

def contacet_page(request):
    return render(request, 'contacet_page.html')


# @login_required
# def dashboard(request):
#     admin = Admin.objects.get(user=request.user)
#     patients_approved = Patient.objects.filter(approved=True).count()
#     patients_pending = Patient.objects.filter(approved=False).count()
#     patients_declined = Patient.objects.filter(declined=True).count()
#     doctors = Doctor.objects.all()
#     appointments = Appointment.objects.all()
#     bills = Bill.objects.all()
#     context = {
#         'admin': admin,
#         'patients_approved': patients_approved,
#         'patients_pending': patients_pending,
#         'patients_declined': patients_declined,
#         'doctors': doctors,
#         'appointments': appointments,
#         'bills': bills
#     }
#     return render(request, 'admin/dashboard.html', context)

# @login_required
# def appointment(request, appointment_id):
#     appointment = Appointment.objects.get(id=appointment_id)
#     if request.method == 'POST':
#         appointment.status = request.POST.get('status')
#         appointment.save()
#         return redirect('admin_dashboard')
#     context = {
#         'appointment': appointment
#     }
#     return render(request, 'admin/appointment.html', context)

# @login_required
# def discharge(request, patient_id):
#     patient = Patient.objects.get(id=patient_id)
#     if request.method == 'POST':
#         patient.discharged = True
#         patient.save()
#         return redirect('admin_dashboard')
#     context = {
#         'patient': patient
#     }
#     return render(request, 'admin/discharge.html', context)

# @login_required
# def billing(request, patient_id):
#     patient = Patient.objects.get(id=patient_id)
#     if request.method == 'POST':
#         room_charges = request.POST.get('room_charges')
#         doctor_fees = request.POST.get('doctor_fees')
#         medicine_charges = request.POST.get('medicine_charges')
#         other_charges = request.POST.get('other_charges')
#         total = int(room_charges) + int(doctor_fees) + int(medicine_charges) + int(other_charges)
#         bill = Bill(patient=patient, room_charges=room_charges, doctor_fees=doctor_fees, medicine_charges=medicine_charges, other_charges=other_charges, total=total)
#         bill.save()
#         return redirect('admin_dashboard')
#     context = {
#         'patient': patient
#     }
#     return render(request, 'admin/billing.html', context)
