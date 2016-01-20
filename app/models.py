from __future__ import unicode_literals
from django.db import models
from datetime import time
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from decimal import Decimal


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

    class Meta:
        ordering = ['email']

    def get_full_name(self):
        return self.fname +" "+ self.lname

    def get_short_name(self):
        return self.fname 

    object = MyUserManager()

############################################################################
############################################################################
############################################################################

class UserProf(models.Model):
    fname = models.CharField(max_length=120, default="First Name")
    lname = models.CharField(max_length=120, default="Last Name")
    # dp = models.ImageField()
    acct = models.ForeignKey(MyUser)
    is_active=models.BooleanField(default=True)

    def __unicode__(self):
        return self.fname + " " + self.lname

MyUser.profile = property(lambda u: UserProf.objects.get_or_create(acct=u)[0])

class BillingAddress(models.Model):
    postalcode = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    pnum = models.CharField(max_length=120)
    acct = models.ForeignKey(UserProf)
    is_active=models.BooleanField(default=True)
    street = models.CharField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return self.acct

class PermanentAddress(models.Model):
    postalcode = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    street = models.CharField(max_length=120, null=True, blank=True)
    pnum = models.CharField(max_length=120)
    acct = models.ForeignKey(UserProf)
    is_active=models.BooleanField(default=True)

    def __unicode__(self):
        return self.acct

class Gender(models.Model):
    gender = models.CharField(max_length=120, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.gender

class Classification(models.Model):
    classname = models.CharField(max_length=120, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.classification

class Shop(models.Model):
    sname = models.CharField(max_length=120, null=True, blank=True)
    sid = models.ForeignKey(MyUser)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.sname

class Category(models.Model):
    cname = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['cname']

    def __unicode__(self):
        return self.cname

class Product(models.Model):
    is_active = models.BooleanField(default=True)
    cid = models.ForeignKey(Category, null=True, blank=True)
    # cid = models.ManyToManyField(Category)
    owner = models.ForeignKey(MyUser)
    pname = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    dateadded = models.DateTimeField(default=timezone.now())
    sex = models.ForeignKey(Gender, null=True, blank=True)
    shop = models.ForeignKey(Shop, null=True, blank=True)

    def __unicode__(self):
        return self.pname

class Color(models.Model):
    colorname = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.colorname

class PriceRange(models.Model):
    price = models.DecimalField(max_digits=20,  decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.price

class Image(models.Model):
    img1 = models.FileField(upload_to=None)
    img2 = models.FileField(upload_to=None)
    img3 = models.FileField(upload_to=None)
    img4 = models.FileField(upload_to=None)
    img5 = models.FileField(upload_to=None)
    pid = models.ForeignKey(Product)



# class Cart(models.Model)
#     cuid = models.ForeignKey(Customer)
#     prid = models.ForeignKey(Product)
