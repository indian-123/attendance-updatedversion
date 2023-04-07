from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.

class college(models.Model):
    username  = models.TextField( )
    password = models.TextField( )
    name=models.TextField()
    logo = models.ImageField( upload_to="pics")

class Student(models.Model):
    name = models.TextField()
    reg = models.TextField()
    s_mobile = models.TextField()
    p_mobile = models.TextField()
    # date_field = models.DateField(default=timezone.now)
    attendance = models.BooleanField(default=False)
    # def save(self, *args, **kwargs):
    #     self.attendance = True if self.date_field.date() == datetime.today().date() else False
    #     super(Student, self).save(*args, **kwargs)

    # def __str__(self):
    #     return f"MyModel object (id: {self.name})"
    clg = models.TextField()
    department = models.TextField()
    year = models.TextField()

class Staff(models.Model):
    staffName=models.TextField()
    staffDep=models.TextField()
    staffCollege = models.TextField()
    staffPosition=models.TextField()
    staffUsername=models.TextField()
    staffPassword=models.TextField()

class Attendance(models.Model):
    Roll= models.TextField()
    Date_field = models.TextField()
    morning_attendance=models.BooleanField(default=True)
    afternoon_attendance=models.TextField(default=True)
    College_Name=models.TextField()
