

# Create your models here.
from django.db import models

class Staff(models.Model):
    objects = models.Manager()
    staffno = models.CharField(max_length=10, unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    branchno = models.CharField(max_length=10)
    dob = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()

class Branch(models.Model):
    objects = models.Manager()
    branch_no = models.CharField(max_length=10, primary_key=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.fname} {self.lname} - {self.position}"


class Client(models.Model):
    client_no = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tel_no = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    pref_type = models.CharField(max_length=5)
    max_rent = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.client_no
