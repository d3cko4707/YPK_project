from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    """
   A member is inserted into a website but has no rights.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.username + " (" + self.user.first_name + " " + self.user.last_name + ")"

class Register(models.Model):
    """
        An Register to hold Members information
        """
    client = models.ForeignKey(Member, on_delete=models.CASCADE)
    MISTER = 'MR'
    MISS = 'MISS'
    MISSES = 'MRS'
    GENDER = (
        (MISTER, 'MR'),
        (MISS, 'Miss'),
        (MISSES, 'Mrs'),
    )
    gender = models.CharField(max_length=4, choices=GENDER, default=MISTER)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    county = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    mobilephone = models.CharField(max_length=10, blank=True)
    fax = models.CharField(max_length=10, blank=True)
    workphone = models.CharField(max_length=10, blank=True)


class Events(models.Model):
    " this is a class that handles Events of the party when created "
    name = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=250)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Pictures(models.Model):

    " A class to handle pictures "

    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    image = models.ImageField()




