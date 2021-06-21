from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=15,unique=True,blank=False,null=False)
    password = models.CharField(max_length=15,blank=False,null=False)
