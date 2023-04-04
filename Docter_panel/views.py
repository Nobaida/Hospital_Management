from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from Docter_panel.models import Docter_Appointment,Patient,Doctor
from Admin_panel.models import Appointment,Bill,Management_Appointment,Request,Record,Discharge,Admins


# Create your views here.

@login_required
def patient_detail(request):
    if request.method == 'POST':
        patient = request.POST.get('patient')
        patient = request.user.patient
        print(patient,'<-----------------------line no 16----------------------->')
        appointments = Appointment.objects.filter(name=patient)
        print('===========================================================',appointments)
    return render(request, 'patient_detail.html')

@staff_member_required
def doctor_approval(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        doctor = Doctor.objects.get(id=doctor_id)
        doctor.approved = True
        doctor.save()
        return render(request, 'doctor_approval.html', {'approved': True})
    else:
        doctors = Doctor.objects.filter(approved=False)
        return render(request, 'doctor_approval.html', {'doctors': doctors})

@login_required
def doctor_detail(request):
    doctor = request.user.doctor
    if not doctor.approved:
        return render(request, 'doctor_approval_pending.html')
    patients = Patient.objects.filter(doctor=doctor)
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'doctor_detail.html', {'doctor': doctor, 'patients': patients, 'appointments': appointments})

@login_required
def appointment_create(request):
    doctor = request.user.doctor
    if not doctor.approved:
        return render(request, 'doctor_approval_pending.html')
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        patient = Patient.objects.get(id=patient_id)
        date = request.POST.get('date')
        time = request.POST.get('time')
        appointment = Appointment(patient=patient, doctor=doctor, date=date, time=time)
        appointment.save()
        return render(request, 'appointment_created.html')
    else:
        patients = Patient.objects.filter(doctor=doctor)
        return render(request, 'appointment_create.html', {'patients': patients})
    
    
    
    

    