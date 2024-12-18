from datetime import timezone
from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator

class Employee(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    MARITAL_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]

    eid = models.CharField(max_length=20, blank=False)
    ename = models.CharField(max_length=30, blank=False)
    eemail = models.EmailField(max_length=50)
    eaddress = models.CharField(max_length=40, blank=False)
    ephonenumber = models.CharField(max_length=15, unique=True)  # Make sure phone number is unique
    egender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    eMarital = models.CharField(max_length=10, choices=MARITAL_CHOICES)
    enumberofavailable = models.IntegerField(validators=[MinValueValidator(0)])
    evecationday = models.IntegerField(validators=[MinValueValidator(0)])
    eApprocedvecation = models.BooleanField()
    eSalary = models.DecimalField(max_digits=10, decimal_places=2 , validators=[MinValueValidator(3000)])
    eDateofBirth = models.DateField()

    def __str__(self)  :
        return "%s" %(self.ename) 
    
    class Meta :
        db_table = "employee"
        



class Vacation(models.Model):
    employee_id = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=100, default='submitted')

    def __str__(self)  :
        return "%s" %(self.ename) 
    
    class Meta:
        db_table = "vacation"


