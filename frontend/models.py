from django.db import models

class prddb(models.Model):
    pname=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    size=models.IntegerField(null=True,blank=True)
    color=models.CharField(max_length=50,null=True,blank=True)
    status=models.CharField(max_length=50,null=True,blank=True)

# Create your models here.
