from django.db import models

class patient(models.Model):
    patname = models.CharField(max_length=100)
    patemail = models.EmailField(unique=True, blank=True)
    patage= models.IntegerField(default=0)
    patdisease= models.CharField(max_length=100)