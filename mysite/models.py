from django.db import models

class Car(models.Model):
    STATUS_TYPE=(('available','available'),('booked','booked'),('rented','rented'),('damaged','damaged'))
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year=models.IntegerField()
    location=models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_TYPE)
    

    def __str__(self): 
        return self.make + ' ' + self.carmodel+ ' ' +self.year+ ' ' +self.location+ ' ' +self.status

class Customer(models.Model):
     name = models.CharField(max_length=50)
     address = models.CharField(max_length=50)
     age=models.IntegerField()

     def __str__(self): 
       return self.name+' '+address+' '+age

class Employee(models.Model):
     name = models.CharField(max_length=50)
     address = models.CharField(max_length=50)
     branch=models.CharField(max_length=50)

     def __str__(self): 
       return self.name+' '+address+' '+branch