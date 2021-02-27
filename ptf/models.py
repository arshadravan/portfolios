from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Service(models.Model):
    service_id=models.AutoField
    service_name=models.CharField(max_length=50)
    aboutservice=models.CharField(max_length=5000)
    image = models.ImageField(upload_to="ptf/images", default="")


    def __str__(self):
        return self.service_name

class Contact(models.Model):
    contact_id = models.AutoField
    firstname = models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    msg = models.CharField(max_length=500, default="")



    def __str__(self):
        return self.firstname

class Aboutm(models.Model):
    about_id = models.AutoField
    image = models.ImageField(upload_to="ptf/images", default="")
    brief = models.CharField(max_length=5000)
    education = models.CharField(max_length=50)

class Postcmnt(models.Model):
    msg_id = models.AutoField
    msg = models.CharField(max_length=500, default="")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)






