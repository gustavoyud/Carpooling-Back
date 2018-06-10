from django.db.models import Q
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from .models import Users
from car.serializers import UserSerializer, UserLoginSerializer, APIUserSerializer
from rest_framework import  generics, mixins

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

#Django User

#Create
class UserView(generics.CreateAPIView):
    serializer_class    = APIUserSerializer
    queryset            = User.objects.all()
    permission_classes  = [AllowAny]
#Check
class UserLoginApiView(APIView):
    permission_classes  = [AllowAny]
    serializer_class    = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data        = request.data
        serializer  = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.erros, status=HTTP_400_BAD_REQUEST)


# Car pooling User
class UserAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field           = 'user_pk'
    serializer_class       = UserSerializer

    def get_queryset(self):
        qs = Users.objects.all()
        query = self.request.GET.get('username')
        if query is not None:
            qs = qs.filter(Q(username__icontains=query)).distinct()
        return qs
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field           = 'user_pk'
    serializer_class       = UserSerializer
    permission_classes     = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Users.objects.all()

