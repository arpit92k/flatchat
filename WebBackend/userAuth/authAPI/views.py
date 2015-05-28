from authAPI.models import UserInfo
from authAPI.serializers import UserInfoSerializer,UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from authAPI.permissions import IsOwnerOrReadOnly

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserInfoList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    	queryset = UserInfo.objects.all()
 	serializer_class = UserInfoSerializer
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class UserInfoDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    	queryset = UserInfo.objects.all()
    	serializer_class = UserInfoSerializer

