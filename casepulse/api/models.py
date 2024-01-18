from django.db import models
from django.urls import reverse
from datetime import date
# from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.

class Case(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  status= models.BooleanField(default=True)
  clientCPR = models.IntegerField(default=000000000)
  clientEmail = models.EmailField(default='example@example.com')
  case_start_date = models.DateTimeField(auto_now_add=True)
  case_end_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('case_details', kwargs={'case_id': self.id})

class Lawyer(models.Model):
  firstName = models.CharField(max_length=100)
  lastName = models.CharField(max_length=100)
  userName = models.CharField(max_length=100)
  phoneNumber = models.TextField(max_length=250)
  email = models.EmailField(default='default@default.com')
  password = models.CharField(max_length=128, validators=[UnicodeUsernameValidator()])  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  cases = models.ManyToManyField(Case)
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('lawyer_details', kwargs={'lawyer_id': self.id})
  

class Reminder(models.Model):
  case_id = models.ForeignKey(Case, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('reminder_details', kwargs={'reminder_id': self.id})


class Document(models.Model):
  case_id = models.ForeignKey(Case, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  file_path = models.FileField(upload_to='api/static/documents/', default="")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('reminder_details', kwargs={'reminder_id': self.id})
