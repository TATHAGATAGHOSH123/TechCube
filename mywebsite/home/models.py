from django.db import models


# Create your models here.
class Contact(models.Model):
     sno = models.AutoField(primary_key=True)
     fname = models.CharField(max_length=50,default="")
     lname = models.CharField(max_length=50,default="")
     phone = models.CharField(max_length=13)
     email = models.CharField(max_length=100)
     content = models.TextField()
     timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.fname + ' - ' + self.email