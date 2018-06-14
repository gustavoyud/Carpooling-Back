from django.shortcuts import render

from django.db.models import Q
from .models import Cars
from .serializers import carSerializer, UserSerializer
from car.models import User

from rest_framework import  generics, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

class carAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field           = 'car_pk'
    serializer_class       = carSerializer

    def get_queryset(self):
        qs = Cars.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(user__id__iexact=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class carRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field           = 'car_pk'
    serializer_class       = carSerializer

    def get_queryset(self):
        return Cars.objects.all()

#   FK
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)