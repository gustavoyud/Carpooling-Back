# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from django.db.models import Q
from .models import userSchedule
from schedule.models import Schedule
from cars.models import User
from schedule.serializers import scheduleSerializerGet


class userScheduleSerializerGet(serializers.HyperlinkedModelSerializer):
    schedule_id     = scheduleSerializerGet(many=False, read_only=True)
    user_id         = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = userSchedule
        fields = ('user_schedule_pk', 'schedule_id', 'user_id')

class userScheduleSerializer(serializers.HyperlinkedModelSerializer):
    schedule_id     = serializers.PrimaryKeyRelatedField(queryset=Schedule.objects.all())
    user_id         = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = userSchedule
        fields = ('user_schedule_pk', 'schedule_id', 'user_id')

    def validate(self, data):
        user_id = data["user_id"]
        schedule_id = data["schedule_id"]

        if schedule_id.property_user.user.id == user_id.id:
            raise serializers.ValidationError("Um motorista não pode entrar na sua propria carona")

        user = userSchedule.objects.filter(Q(user_id=user_id) & Q(schedule_id=schedule_id)).distinct()
        if user.exists() and user.count() != 0:
            raise serializers.ValidationError("Um usuário não pode pegar 2 vezes a mesma carona")

        count = userSchedule.objects.filter(Q(schedule_id=schedule_id)).distinct()
        if count.exists() and count.count() == schedule_id.cars.capacity: 
            raise serializers.ValidationError("O Carro está em sua capacidade máxima")
         
        return data