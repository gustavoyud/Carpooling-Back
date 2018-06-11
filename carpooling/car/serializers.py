# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Users 
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, EmailField, CharField
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email' ]


class APIUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {"password": {"write_only": True} }
    
    def create(self, validated_data):
        username    = validated_data['username']
        email       = validated_data['email']
        password    = validated_data['password']
        user_obj    = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserLoginSerializer(ModelSerializer):
    token       = CharField(allow_blank=True, read_only=True)
    username    = CharField(required=False, allow_blank=True)
    url         = CharField(required=False, allow_blank=True)

    class Meta:
        model   = User
        fields  = ['username', 'password', 'token', 'url']
        extra_kwargs = {"password": {"write_only": True} }

    def validate(self, data):
        user_obj    = None
        email       = data.get("email", None)
        username    = data.get("username", None)
        password    = data["password"]

        if not email and not username:
            raise serializers.ValidationError("Informe um e-mail ou um nome de usuário")

        user = User.objects.filter(Q(email=email) | Q(username=username)).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("Nome de usuário ou E-mail inválido")

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError([{'error': 'Senha Incorreta', 'field' : 'password'}])
        
        print(user_obj)
        token, created  = Token.objects.get_or_create(user=user_obj)
        data["token"]   = token.key
        data["url"]     = 'http://localhost:8000/users/detail/'+str(user_obj.id)+'/'
        return data

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Users
        fields = (
            'user_pk', 
            'name', 
            'geral_register', 
            'address', 
            'complement', 
            'ZIP', 
            'neighborhood', 
            'city', 
            'federal_unit', 
            'phone', 
            'celphone', 
            'user',
        )

    
    def validate_user(self, value):
        qs = Users.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('O nome de usário já existe')
        return value

