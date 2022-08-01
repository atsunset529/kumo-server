from hashlib import md5
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from accounts.models import User, CustomerUser, ShopUser
# Create your models here.
class UserQr(models.Model):
    user = models.ImageField(upload_to='qrcode', null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    level = models.IntegerField(default=0 ,blank=True)
    shopname = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    coupon_num = models.IntegerField(default=0 ,blank=True)
    used_at = models.DateTimeField(auto_now_add=True)

class Stamp(models.Model):
    shopname = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    stamp_num = models.IntegerField(default=0, blank=True)
    
    def __init__(self):
        self.stamp_num += 1

class Bookmark(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shopname = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name='bookmark')
    bookmark_set = models.ManyToManyField(ShopUser, blank=True)

class CustomerQna(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)

class CustomerQuestion(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)