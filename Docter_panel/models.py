from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='userdocter')
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.approved)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='userpatient')
    
    def __str__(self):
        return str(self.doctor)


class Docter_Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return str(self.patient)
    
    
    
    