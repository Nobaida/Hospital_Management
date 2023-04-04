from email.policy import default
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
# from Docter_panel.models import Patient

# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
           raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    symptoms = models.TextField()
    approved = models.BooleanField(null=True, blank=True,default=False,)

    def __str__(self):
        return str(self.name)

class Bill(models.Model):
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='docterPatient')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    room_charge = models.DecimalField(max_digits=8, decimal_places=2)
    doctor_fee = models.DecimalField(max_digits=8, decimal_places=2)
    medicine_charge = models.DecimalField(max_digits=8, decimal_places=2)
    other_charge = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)                    
    
    def __str__(self):
        return str(self.room_charge)
    
class Management_Appointment(models.Model):
    patient = models.ForeignKey(User, related_name= "userpatient", on_delete=models.CASCADE)
    doctor = models.ForeignKey(User,related_name="userdoctor" ,on_delete=models.CASCADE)
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    
    def __str__(self):
        return str(self.date)
    
class Request(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Requestpatient')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Requestdoctor')
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    message = models.CharField(max_length=1024)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('declined', 'Declined')])
    
    def __str__(self):
        return str(self.message)

class Record(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Recordpatient')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Recorddoctor')
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    note = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.note)

class Discharge(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    data_andtime = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return str(self.data_andtime)

class Admins(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)
    
    
    
    
    