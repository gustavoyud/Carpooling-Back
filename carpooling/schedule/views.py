from django.shortcuts import render

from django.db.models import Q
from .models import Schedule
from .serializers import scheduleSerializer, scheduleCreateSerializer

from rest_framework import  generics, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

class scheduleAPIView(generics.ListAPIView):
    lookup_field           = 'schedule_pk'
    serializer_class       = scheduleSerializer

    def get_queryset(self):
        qs = Schedule.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(property_user__id__iexact=query)).distinct()
        return qs

class scheduleRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field           = 'schedule_pk'
    serializer_class       = scheduleCreateSerializer

    def get_queryset(self):
        return Schedule.objects.all()

class scheduleCreateAPIView(generics.CreateAPIView):
    serializer_class       = scheduleCreateSerializer

    def get_queryset(self):
        qs = Schedule.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(property_user__id__iexact=query)).distinct()
        return qs