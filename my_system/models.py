from django.db import models


# Create your models here.
class Suggestion(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    suggestion = models.TextField()

    def __str__(self):
        return self.email


class Train_Data(models.Model):
    trainName = models.CharField(max_length=50,unique=True)
    trainNumber = models.CharField(max_length=5,unique=True)
    fromStation = models.CharField(max_length=40)
    toStation = models.CharField(max_length=40)
    stoppages = models.FileField(upload_to='uploads/train_stoppages/')
    runningDays = models.CharField(max_length=16)
    capacity = models.IntegerField()
    booked = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.trainNumber, self.trainName)



class Ticket(models.Model):
    name = models.CharField(max_length=40)
    address = models.TextField()
    mobileNo = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField()
    from_station = models.CharField(max_length=40)
    to_station = models.CharField(max_length=40)
    doj = models.DateField()
    ticket_no=models.CharField(max_length=8,unique=True)
    train_no=models.CharField(max_length=5)
    train_name=models.CharField(max_length=50)


    def __str__(self):
        return "%s %s" %(self.ticket_no,self.name)


class UserRegistration(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    username = models.CharField(max_length=20)
    address = models.TextField()
    gender = models.CharField(max_length=15)
    dob = models.DateField()
    email = models.EmailField()
    mobileNumber = models.CharField(max_length=10)
    occupation = models.CharField(max_length=20)

    def __str__(self):
        return self.username
