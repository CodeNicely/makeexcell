from __future__ import unicode_literals

from django.db import models

class user_data(models.Model):
	user_id= models.AutoField(primary_key= True)
	user_name=models.CharField(max_length=120, blank=True,null=True)
	image= models.ImageField()


# Create your models here.
