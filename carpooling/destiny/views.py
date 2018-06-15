from django.shortcuts import render

# Create your views here.

from django.db.models import Q
from .models import Destiny
from .serializers import destinySerializer

from rest_framework import  generics, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

class destinyAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field           = 'destiny_pk'
    serializer_class       = destinySerializer

    def get_queryset(self):
        qs = Destiny.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(address__icontains=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class destinyRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field           = 'destiny_pk'
    serializer_class       = destinySerializer

    def get_queryset(self):
        return Destiny.objects.all()
