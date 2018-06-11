# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from rest_framework import reverse

# Created By: Gustavo Yud

# Users Model
class Users(models.Model):
    user_pk         = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=30)
    geral_register  = models.IntegerField()
    address         = models.CharField(max_length=100)
    complement      = models.CharField(max_length=200)
    ZIP             = models.IntegerField()
    neighborhood    = models.CharField(max_length=50)
    city            = models.CharField(max_length=50)
    federal_unit    = models.CharField(max_length = 3)
    phone           = models.IntegerField()
    celphone        = models.IntegerField()
    user            = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'user'
        verbose_name_plural = u'users'
    
    def __str__(self):
        return str(self.user)
    
    @property
    def owner(self):
        return self.user
    