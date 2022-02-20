from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Analytics(models.Model):
    name=name = models.TextField()
    stats= models.IntegerField(default=0)
    date= models.DateTimeField(default=timezone.now)

class Event(models.Model):
    name = models.TextField()
    username = models.TextField()
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40)
    created = models.DateTimeField(default=timezone.now)

class RegisterEvent(models.Model):
    username = models.TextField()
    created = models.DateTimeField(default=timezone.now)

class LoginEvent(models.Model):
    username = models.TextField()
    created = models.DateTimeField(default=timezone.now)

class ViewPageEvent(models.Model):
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40)
    created = models.DateTimeField(default=timezone.now)

class EditProfileEvent(models.Model):
    username = models.TextField()
    created = models.DateTimeField(default=timezone.now)

class LogoutEvent(models.Model):
    username = models.TextField()
    created = models.DateTimeField(default=timezone.now)
