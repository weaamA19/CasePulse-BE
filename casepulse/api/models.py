from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

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
  clientCPR = models.IntegerField(default=000000000)
  clientEmail = models.EmailField(default='example@example.com')
  case_start_date = models.DateTimeField(auto_now_add=True)
  case_end_date = models.DateTimeField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('case_details', kwargs={'case_id': self.id})

class Lawyer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phoneNumber = models.TextField(max_length=250)
  avatar = models.ImageField(upload_to='api/static/uploads', default="default.png")
  cases = models.ManyToManyField(Case)

  def get_absolute_url(self):
    return reverse('lawyer_details', kwargs={'lawyer_id': self.id})
  

class Reminder(models.Model):
  case_id = models.ForeignKey(Case, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250, blank=True, null=True)
  date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('reminder_details', kwargs={'reminder_id': self.id})


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
