# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from .models import Schedule
from cars.models import Cars
from destiny.models import Destiny
from car.models import User
from destiny.serializers import destinySerializer
from cars.serializers import carSerializer

class scheduleSerializer(serializers.HyperlinkedModelSerializer):
    # cars = serializers.PrimaryKeyRelatedField(queryset=Cars.objects.all())
    # final_destiny = serializers.PrimaryKeyRelatedField(queryset=Destiny.objects.all())
    # cars = serializers.SlugRelatedField(many=False, read_only=True, slug_field='model')
    # final_destiny = serializers.SlugRelatedField(many=False, read_only=True, slug_field='address')
    final_destiny = destinySerializer(many=False, read_only=True)    
    cars = carSerializer(many=False, read_only=True)
    property_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Schedule
        fields = ['schedule_pk', 'dateTime', 'cars', 'final_destiny', 'property_user']


class scheduleCreateSerializer(serializers.HyperlinkedModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(queryset=Cars.objects.all())
    final_destiny = serializers.PrimaryKeyRelatedField(queryset=Destiny.objects.all())
    property_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Schedule
        fields = ['schedule_pk', 'dateTime', 'cars', 'final_destiny', 'property_user'] 