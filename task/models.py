from django.db import models
from django.contrib.auth.models import User
from django.db import models
import random as rnd
from django.db import models
import math
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyAccountManager(BaseUserManager):
    
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users must have an email address.")

        if not username:
            raise ValueError("Users must have a username.")

        user =self.model(
            email=self.normalize_email(email),
            username=username
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



def get_profile_image_filepath(self,filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "img/avatar.png"
class Account(AbstractBaseUser):
    email =models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255,upload_to=get_profile_image_filepath,null=True,blank=True,default=get_default_profile_image)
    objects = MyAccountManager()

    USERNAME_FIELD ="email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/{self.pk}/')]

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_Label):
        return True   




class App(models.Model):
    logo = models.ImageField()
    name = models.CharField(max_length=255)
    app_link = models.URLField()
    app_cat = models.CharField(max_length=255)
    app_subcat = models.CharField(max_length=255)
    point = models.IntegerField()
    
    
    def __str__(self):
        return self.name


class Task(models.Model):
    app = models.ForeignKey(App,on_delete=models.CASCADE)
    img = models.ImageField()
    created = models.ForeignKey(Account,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.created.username} task" 
        
def get_total_point(user):
    points = 0
    tasks = Task.objects.filter(created=user)
    for task in tasks:
        if task.completed:
            points += task.app.point
    return points


        
