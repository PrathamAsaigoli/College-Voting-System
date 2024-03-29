from django.db import models

# Create your models here.
class Csepresident(models.Model):
   
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length= 255)
    image = models.FileField(upload_to="csepresident",max_length=250,null=True,default=None)
    
class Csevicepresident(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length= 255)
    image = models.FileField(upload_to="csevicepresident",max_length=250,null=True,default=None)    

class Csesecretory(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length= 255)
    image = models.FileField(upload_to="csesecretory",max_length=250,null=True,default=None)