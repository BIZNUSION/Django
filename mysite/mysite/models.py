from django.db import models

class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=50)
    year = models.IntegerField()
    gender = models.CharField(max_length=10)
    dob = models.DateField()
