# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from .models import Schedule
from cars.models import Cars
from destiny.models import Destiny
from car.models import Users
from car.serializers import userSerializerGet
from destiny.serializers import destinySerializer
from cars.serializers import carSerializer
from user_schedule.models import userSchedule

class scheduleSerializer(serializers.ModelSerializer):
    # cars = serializers.PrimaryKeyRelatedField(queryset=Cars.objects.all())
    # final_destiny = serializers.PrimaryKeyRelatedField(queryset=Destiny.objects.all())
    # cars = serializers.SlugRelatedField(many=False, read_only=True, slug_field='model')
    # final_destiny = serializers.SlugRelatedField(many=False, read_only=True, slug_field='address')
    final_destiny = destinySerializer(many=False, read_only=True)    
    cars = carSerializer(many=False, read_only=True)
    # property_user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    property_user = userSerializerGet(many=False, read_only=True)

    class Meta:
        model = Schedule
        fields = ['schedule_pk', 'dateTime', 'cars', 'final_destiny', 'property_user']
        ordering = ['-dateTime']

class scheduleSerializerGet(serializers.ModelSerializer):
    final_destiny = destinySerializer(many=False, read_only=True)    
    cars = carSerializer(many=False, read_only=True)
    property_user = userSerializerGet(many=False, read_only=True)

    class Meta:
        model = Schedule
        fields = ('schedule_pk','dateTime', 'cars', 'final_destiny', 'property_user')
        ordering = ['-dateTime']
        
class scheduleCreateSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(queryset=Cars.objects.all())
    final_destiny = serializers.PrimaryKeyRelatedField(queryset=Destiny.objects.all())
    property_user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())

    class Meta:
        model = Schedule
        fields = ['schedule_pk', 'dateTime', 'cars', 'final_destiny', 'property_user'] 
        ordering = ['-dateTime']
        