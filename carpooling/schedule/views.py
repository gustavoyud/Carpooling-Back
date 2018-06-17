from django.shortcuts import render
from itertools import chain
from django.db.models import Q
from .models import Schedule
from .serializers import scheduleSerializer, scheduleCreateSerializer, scheduleSerializerGet
from user_schedule.models import userSchedule
from user_schedule.serializers import userScheduleSerializer
from rest_framework import  generics, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class scheduleAPIView(generics.ListAPIView):
    lookup_field           = 'schedule_pk'
    serializer_class       = scheduleSerializerGet
    
    def get_queryset(self):
        qs = Schedule.objects.all().order_by('-dateTime')

        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(property_user__user__id__iexact=query)).order_by('-dateTime').distinct()

        id = self.request.GET.get('user_id')
        if id is not None:
            qs = qs.exclude(property_user__user_id__id=id).order_by('-dateTime').distinct()

        return qs
    
class scheduleRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field           = 'schedule_pk'
    serializer_class       = scheduleCreateSerializer

    def get_queryset(self):
        return Schedule.objects.all()

class scheduleCreateAPIView(generics.CreateAPIView):
    serializer_class       = scheduleCreateSerializer

    def get_queryset(self):
        qs = Schedule.objects.all().order_by('-dateTime')
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(property_user__user__id__iexact=query)).order_by('-dateTime').distinct()
        return qs