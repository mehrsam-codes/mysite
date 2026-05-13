from django.db import models

# Create your models here.
class Post(models.Model): #table name 
    title   = models.CharField (max_length=255)
    content =  models.TextField()#column
    image = models.CharField()
    category = models.CharField()
    tag = models.CharField()
    author = models.CharField()
    counted_view = models.IntegerField()
    status = models.BooleanField()
    published_date = models.DateTimeField()
    created_date = models.DateTimeField
    updated_date = models.DateTimeField()

# class  Mehrta(models.Model):
#     name = models.CharField(max_length=250) 
