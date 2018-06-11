from django.db.models import Q
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from .models import Users
from car.serializers import UserSerializer, UserLoginSerializer, APIUserSerializer, UsersSerializer
from rest_framework import  generics, mixins

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

#Django User

#Create
class UserView(generics.CreateAPIView):
    serializer_class    = APIUserSerializer
    queryset            = User.objects.all()
    permission_classes  = [AllowAny]

#Login
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

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


# Login Check
class UserLoginCheckAPIView(APIView):
    def get(self, request, format=None):
        """
            Check Actual Token
        """
        if request.user.is_authenticated:
            return Response({'success':'logged'}, status=HTTP_200_OK)
 
        return Response({'error':'Not logged'}, status=HTTP_403_FORBIDDEN)
        

# Car pooling User
class UserAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field           = 'user_pk'
    serializer_class       = UsersSerializer

    def get_queryset(self):
        qs = Users.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(user__username__iexact=query)).distinct()
        return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field           = 'user_pk'
    serializer_class       = UsersSerializer

    def get_queryset(self):
        return Users.objects.all()
