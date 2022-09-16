from dataclasses import fields
from distutils.command.upload import upload
from email.policy import default
import re
from unicodedata import category
from warnings import filters
import django
from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=100)        

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})    

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Manufacturer = models.CharField(max_length=70)
    Image = models.ImageField(upload_to ='media',blank=False,max_length=100,default='default.jpg' )
    Category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,default='uncategorised',null=True)
    CPU = models.CharField(max_length=100)
    GPU = models.CharField(max_length=100,blank=True)
    OS = models.CharField(max_length=100)
    Ports = models.CharField(max_length=100)
    Screen_resolution = models.CharField(max_length=100)
    Screen_size = models.CharField(max_length=100)
    Screen_panel_type = models.CharField(max_length=100,blank=True)
    Web_camera = models.CharField(max_length=100,blank=True)
    Main_camera = models.CharField(max_length=100,blank=True)
    Front_camera = models.CharField(max_length=100,blank=True)
    Screen_refresh_rate = models.CharField(max_length=100)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10,decimal_places=2)

    

    def __str__(self):
        return self.Name


    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])