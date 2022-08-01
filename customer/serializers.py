from dataclasses import field
import profile
from turtle import stamp
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Bookmark, Profile, Stamp, UserQr
from accounts.models import User, ShopUser


#class UserQrSerializer(serializers.ModelSerializer):


class ProileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "user", "level", "shopname", "coupon_num", "used_at"
        ]


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stamp
        field = [
            "shopname", "stamp_num"
            ]


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        field = [
            "shopname", "user"
            ]