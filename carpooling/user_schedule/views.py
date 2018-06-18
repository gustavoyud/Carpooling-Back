from django.shortcuts import render

from django.db.models import Q
from .models import userSchedule
from .serializers import userScheduleSerializer, userScheduleSerializerGet

from rest_framework import  generics, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from rest_framework.views import APIView

class userScheduleAPIView(generics.ListAPIView):
    lookup_field           = 'user_schedule_pk'
    serializer_class       = userScheduleSerializer

    def get_queryset(self):
        qs = userSchedule.objects.all()
        query = self.request.GET.get('user')
        if query is not None:
            qs = qs.filter(Q(user_id__id__iexact=query)).distinct()
        return qs

class userScheduleRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field           = 'user_schedule_pk'
    serializer_class       = userScheduleSerializer

    def get_queryset(self):
        return userSchedule.objects.all()

class userScheduleCreateAPIView(generics.CreateAPIView):
    serializer_class       = userScheduleSerializer

    def get_queryset(self):
        qs = userSchedule.objects.all()
        query = self.request.GET.get('user')
        if query is not None:
            qs = qs.filter(Q(user_id__id__iexact=query)).distinct()
        return qs

class isScheduledCheck(APIView):
    def get(self, request, format=None):
        user_id = self.request.GET.get('user_id')
        schedule_id = self.request.GET.get('schedule_id')
        count = userSchedule.objects.filter(Q(schedule_id=schedule_id)).distinct()  
        qs = userSchedule.objects.filter(Q(user_id=user_id) & Q(schedule_id=schedule_id)).distinct()
        if qs.count() > 0:
            count = count.count()
            qs = qs.first()
            return Response({'scheduled':'true', 'count': count, 'pk': qs.user_schedule_pk }, status=HTTP_200_OK)
        
        return Response({'scheduled':'false'}, status=HTTP_400_BAD_REQUEST)
