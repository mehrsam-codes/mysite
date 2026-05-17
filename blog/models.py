from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)
    def __str__(self):
        return self.name 
class Post(models.Model): #table name 
    image = models.ImageField(upload_to= 'blog/' , default='blog/defualt.jpg')
    author = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    title   = models.CharField (max_length=255)
    content =  models.TextField()#column

    category = models.ManyToManyField(Category)
    # tag = models.IntegerField()

    counted_view = models.IntegerField(default=0)#default=0
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True )
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =  ['created_date']
    def __str__(self):
        return "title :{} | id : {} ".format(self.title , self.id)
    def snippet(self):
        return self.content[:100] + '...'
    
# class User(models.Model):
#     username = models.CharField()
#     firstname = models.CharField()
#     lastname = models.CharField()
#     email = models.CharField()
#     active = models.BooleanField()
#     superuser = models.BooleanField()
#     staff = models.BooleanField()

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
