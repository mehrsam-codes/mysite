from django.db import models

# Create your models here.
class Post(models.Model): #table name 
    title   = models.CharField (max_length=255)
    content =  models.TextField()#column
    # image = models.CharField()
    # category = models.IntegerField()
    # tag = models.IntegerField()
    # author = models.IntegerField()
    counted_view = models.IntegerField(default=0)#default=0
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True )
    updated_date = models.DateTimeField(auto_now=True)
# class User(models.Model):
#     username = models.CharField()
#     firstname = models.CharField()
#     lastname = models.CharField()
#     email = models.CharField()
#     active = models.BooleanField()
#     superuser = models.BooleanField()
#     staff = models.BooleanField()

# class Category(models.Model):
#     name = models.CharField()
# class Tag(models.Model):
#     name = models.CharField()

# class Contact(models.Model):
#     name = models.CharField()
#     subject = models.CharField()
#     email = models.CharField()
#     massage = models.TextField()
#     created_date = models.DateTimeField()
#     updated_date  = models.DateTimeField()
# # class  Mehrta(models.Model):
#     name = models.CharField(max_length=250) 
