from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class MyProfile(models.Model):
	g = [('M',"Male"),('F','Female')]
	age = models.IntegerField(default=10)
	gender = models.CharField(max_length=10,choices=g)
	uid = models.OneToOneField(User,on_delete=models.CASCADE)

class ComplaintBox(models.Model):
	p_name=models.CharField(max_length=100)
	p_email=models.EmailField(max_length=100)
	p_complaint=models.CharField(max_length=1000)

@receiver(post_save,sender=User)
def createpf(sender,instance,created,**kwargs):
	if created:
		MyProfile.objects.create(uid=instance)

		 
class contact(models.Model):
	Name=models.CharField(max_length=20)
	email=models.EmailField(max_length=100)
	Description=models.CharField(max_length=1000)
