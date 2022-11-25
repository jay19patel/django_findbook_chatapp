from pydoc import Helper
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
MultiSelectField=MultiSelectField
# Create your models here.


class Topic(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profilemodel(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    image = models.ImageField(upload_to="ProfilePics")
    bio = models.CharField(max_length=200)
    followers = models.ManyToManyField(User,related_name='followers',blank=True,null=True)
    following  = models.ManyToManyField(User,blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")
    

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    post = models.ImageField(upload_to="posts")
    caption = models.CharField(max_length=200)
    profileuser = models.ForeignKey(Profilemodel,related_name="profile",on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name="likes",blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)


class Room(models.Model):
    helper_name=models.ForeignKey(User,on_delete =models.SET_NULL,null=True)
    topic_name =models.ForeignKey(Topic,on_delete =models.SET_NULL,null=True)
    room_name=models.CharField(max_length=100)
    your_name=models.ForeignKey(Profilemodel,on_delete =models.SET_NULL,null=True)
    updated =models.DateTimeField(auto_now=True)
    created =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    user=models.ForeignKey(User,on_delete =models.CASCADE)
    room=models.ForeignKey(Room,on_delete =models.CASCADE)
    body=models.TextField()
    updated =models.DateTimeField(auto_now=True)
    created =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
