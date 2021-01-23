from django.db import models
from django.contrib import admin

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to='photos/')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class People(models.Model):
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

class PeopleAdmin(admin.ModelAdmin):
    list_display = ['designation']


