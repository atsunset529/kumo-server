from turtle import stamp
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from accounts.models import User, CustomerUser, ShopUser
# Create your models here.


class Coupon(models.Model):
    writer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name="shop_writer")
    shopname = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name="shop_shopname")
    coupon_num = models.IntegerField(default=0 ,blank=True)
    stamp_num = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # stamp 개수가 10개 이상이면 0개로 만들고, 쿠폰 개수를 1개 추가
    def save(self,*args,**kwargs):
        self.stamp_num += 1
        if self.stamp_num >= 10:
            self.coupon_num += 1
            self.stamp_num -= 10
        super().save(*args,**kwargs)



class Payment(models.Model):
    payment_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    shopname = models.ForeignKey(ShopUser, on_delete=models.CASCADE)



class Review(models.Model):
    writer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name="review_writer")
    shopname = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name="review_shopname")
    review_star = models.IntegerField(default=3)
    review_photo = models.ImageField(blank=True)
    review_caption = models.TextField(max_length=100)


    
class ShopQna(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)


class ShopQuestion(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)




