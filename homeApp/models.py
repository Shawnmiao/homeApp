

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

    def __str__(self):
        return f"{self.fname} {self.lname} - {self.position}"
