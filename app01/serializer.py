import re

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from app01.models import *

# 访客模式
class VisitorSerializer(serializers.ModelSerializer):
    pass


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, error_messages={
        "required": "请输入用户名",
        "blank": "用户名不能为空"
    })

    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email")
        extra_kwargs = {"password": {"write_only": True},
                        "email": {"required": True}}

    def validate_username(self, username):
        if User.objects.filter(username=username).count():
            raise serializers.ValidationError('用户名已经存在，请查询')
        return username

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(validated_data["password"])
        user.save()
        return user
