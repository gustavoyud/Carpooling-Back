# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from rest_framework import reverse

# Created By: Gustavo Yud

# Users Model
class Users(models.Model):
    user_pk         = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=30)
    email           = models.EmailField(null=True, blank=True)
    geral_register  = models.IntegerField()
    address         = models.CharField(max_length=100)
    complement      = models.CharField(max_length=200)
    ZIP             = models.IntegerField()
    neighborhood    = models.CharField(max_length=50)
    city            = models.CharField(max_length=50)
    federal_unit    = models.CharField(max_length = 3)
    phone           = models.IntegerField()
    celphone        = models.IntegerField()
    username        = models.CharField(max_length=200)

    class Meta:
        verbose_name = u'username'
        verbose_name_plural = u'usernames'
    
    def __str__(self):
        return self.username
    
    @property
    def owner(self):
        return self.username
    
    def get_api_url(self):
        return reverse("user-rud", kwargs={'user_pk': self.user_pk})