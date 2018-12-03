from django.db import models


# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    email =models.EmailField()
    created_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class details(models.Model):
    img=models.ImageField(upload_to='media/sample_pic')
    resume=models.FileField(upload_to='media/files')
    adress=models.CharField(max_length=50)
    mobno=models.IntegerField(default=10)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.adress

class login(models.Model):
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    mobno=models.BigIntegerField(default=10)
    email=models.EmailField()