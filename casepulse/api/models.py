from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import AbstractUser,User



# Create your models here.
Active = 'A'
Inactive = 'I'
Active_InActive = [
    (Active, 'Active'),
    (Inactive, 'Inactive'),
]

class Case(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250, blank=True, null=True)
  status = models.CharField(max_length=1, choices=Active_InActive, default=Active)
  clientCPR = models.CharField(max_length=9)
  clientEmail = models.EmailField()
  case_start_date = models.DateTimeField(auto_now_add=True)
  case_end_date = models.DateTimeField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('case_details', kwargs={'case_id': self.id})

# User Model
class Lawyer(AbstractUser):
  first_name = models.CharField(max_length=100, blank=False, null=False)
  last_name = models.CharField(max_length=100,blank=False, null=False)
  # userName = models.CharField(max_length=100, unique=True)
  phone_number = models.CharField(max_length=20, blank=False, null=False)
  email_address = models.EmailField(blank=False, null=False)
  avatar = models.ImageField(upload_to='api/static/uploads', default="api/static/uploads/default.png")
  cases = models.ManyToManyField(Case)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS  = ['phoneNumber', 'email', 'firstName', 'email_address']
  def __str__(self):
    return self.username

class Reminder(models.Model):
  case_id = models.ForeignKey(Case, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250, blank=True, null=True)
  datetime = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title



class Document(models.Model):
  case_id = models.ForeignKey(Case, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250, blank=True, null=True)
  file_path = models.FileField(upload_to='api/static/documents/')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('reminder_details', kwargs={'reminder_id': self.id})
