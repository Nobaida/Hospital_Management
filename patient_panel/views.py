from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient

# @login_required
# def dashboard(request):
#     patient = Patient.objects.get(email=request.user.email)
#     appointments = patient.appointment_set.all()
#     bills = patient.bill_set.all()
#     context = {
#         'patient': patient,
#         'appointments': appointments,
#         'bills': bills
#     }
#     return render(request, 'patient/dashboard.html', context)

# def register(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         symptoms = request.POST.get('symptoms')
#         patient = Patient(name=name, email=email, password=password, symptoms=symptoms)
#         patient.save()
#         return redirect('login')
#     return render(request, 'patient/register.html')
