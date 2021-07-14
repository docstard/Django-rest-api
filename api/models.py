from django.db import models
from django.db.models.base import Model
# from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField


# Create your models here.

class User_api(models.Model):
    fname = models.CharField(max_length=200, null=False, blank=False)
    lname = models.CharField(max_length=200, null=False, blank=False)
    Email = models.CharField(max_length=200, null=False, blank=False)
    age = models.IntegerField(max_length=2, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    def __str__(self):
        return self.fname
