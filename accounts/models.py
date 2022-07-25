from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import random
# # Create your models here.
# class UserManager(BaseUserManager):    
   
#     use_in_migrations = True    
   
#     def create_user(self, phone_num, is_shop, password):        
       
#        if not phone_num:            
#            raise ValueError('must have user phone')
#        if not password:            
#            raise ValueError('must have user password')

#        user = self.model(            
#            phone_num = phone_num,
#            is_shop = is_shop   
#        )        
#        user.set_password(password)        
#        user.save(using=self._db)        
#        return user

#     def create_superuser(self, phone_num, is_shop, password):        
   
#        user = self.create_user(            
#            phone_num = phone_num,
#            is_shop = is_shop,                        
#            password=password        
#        )
#        user.is_admin = True
#        user.is_superuser = True
#        user.save(using=self._db)
#        return user 





# 통합 유저
class User(AbstractUser):
    phone_num = models.CharField(
        max_length=13,
        blank=False,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_shop = models.BooleanField(blank=False, null=True)
    image = models.ImageField(upload_to='qrcode', null=True)
    
    
    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.username)
        canvas=Image.new("RGB", (300,300),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.image.save(f'image{random.randint(0,9999)}.png',File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)



# class QRCode(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='qrcode', blank=True)

    
    
        
# 고객 유저
class CustomerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=15, blank=True)
    shop_phone_num = models.CharField(
        max_length=13,
        blank=False,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )
    bookmark_set = models.ManyToManyField('ShopUser', blank=True)



# 업주 유저
class ShopUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=15, blank=False)
    shop_phone_num = models.CharField(
        max_length=13,
        blank=False,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )
    shop_location = models.CharField(blank=False, max_length=100)
    shop_introduction = models.TextField(blank=False)
    shop_sector = models.CharField(blank=False, max_length=10)
    bookmarked_set = models.ManyToManyField('CustomerUser', blank=True)
    







