from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Suggestion(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    suggestion=models.TextField()

    def __str__(self):
        return self.email

class UserRegistration(models.Model):

    firstName=models.CharField(max_length=15)
    lastName=models.CharField(max_length=15)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    address=models.TextField()
    gender=models.CharField(max_length=15)
    dob=models.DateField()
    email=models.EmailField()
    mobileNumber=models.CharField(max_length=10)
    occupation=models.CharField(max_length=20)

    def __str__(self):
        return self.email

