from __future__ import unicode_literals
from django.db import models
from datetime import time
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


############################################################################
############################################################################
############################################################################
class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(
            email=self.normalize_email(email),
            is_Customer=True,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.model(
            email=email,
            is_superuser=True,
            is_staff=True,
            is_active=True,
            is_admin=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom Users
    """
    USERNAME_FIELD = 'email'

    email = models.EmailField(unique=True)
    fname = models.CharField(max_length=120, null=True, blank=True)
    lname = models.CharField(max_length=120, null=True, blank=True)

    is_Customer = models.BooleanField(default=False)
    is_ShopOwner = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def get_full_name(self):
        return self.fname +" "+ self.lname

    def get_short_name(self):
        return self.fname 


    object = MyUserManager()

############################################################################
############################################################################
############################################################################


class Shop(models.Model):
    sname = models.CharField(max_length=120, null=True, blank=True)
    sid = models.ForeignKey(MyUser)
    is_active = models.BooleanField(default=True)

class Category(models.Model):
    cname = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return cname


class Product(models.Model):
    is_active = models.BooleanField(default=True)
    cid = models.ForeignKey(Category)
    owner = models.ForeignKey(MyUser)
    pname = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    dateadded = models.DateTimeField(default=timezone.now())


# class Cart(models.Model)
#     cuid = models.ForeignKey(Customer)
#     prid = models.ForeignKey(Product)
