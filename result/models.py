from django.db import models

# Create your models here.
class csepresidentres(models.Model):
    cid = models.CharField(max_length = 1)

class csevicepresidentres(models.Model):
    cid = models.CharField(max_length = 1)
    
class csesecretoryres(models.Model):
    cid = models.CharField(max_length = 1)
