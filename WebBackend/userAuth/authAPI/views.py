from authAPI.serializers import UserSerializer,LoginSerializer,SignupSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from authAPI.permissions import IsOwnerOrReadonly
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import UserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

"""
to list all users
permissions for only authenticated users
"""
class UserList(generics.ListAPIView):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

"""
to list a user or update loggedin user
read permission to all authenticated users
read write permission on current user's object
"""
class UserInfoDetail(generics.RetrieveUpdateAPIView):
	permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadonly,)
    	queryset = User.objects.all()
    	serializer_class = UserSerializer

"""
register user
accessable for all
"""
class SignupUser(generics.CreateAPIView):
    serializer_class=SignupSerializer
    def create(self,serializer):
        if self.request.user.is_authenticated():
            return HttpResponseRedirect('/user/')
        username = self.request.POST.get('username', None)
        password = self.request.POST.get('password', None)
        email = self.request.POST.get('email', None)
        first_name = self.request.POST.get('first_name', None)
        last_name = self.request.POST.get('last_name', None)
        #validate recieved data
        if not username or not password:
            return Response(data={'result':'fail','cause':'username or password empty'},status=status.HTTP_400_BAD_REQUEST)
        if email:
            try:
                validate_email(email)
            except ValidationError:
                return Response(data={'result':'fail','cause':'invalid email'},status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=username)
        if user:
            return Response(data={'result':'fail','cause':'username already exists'},status=status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(username=self.request.POST['username'],email=self.request.POST['email'],password=self.request.POST['password'])
        return Response(data={'result':'success'},status=status.HTTP_200_OK);

"""
login a user
accessable for all
"""
class Login(generics.CreateAPIView):
    serializer_class=LoginSerializer
    def create(self,serializer):
        if self.request.user.is_authenticated():
			return HttpResponseRedirect('/user/')
        username = self.request.POST.get('username', None)
        password = self.request.POST.get('password', None)
        if not username or not password:
            return Response(data={'result':'fail','cause':'username or password empty'},status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=self.request.POST['username'], password=self.request.POST['password'])
        if user is not None:
			login(self.request, user)
			return Response(data={'result':'success'},status=status.HTTP_200_OK);
        else:
			return Response(data={'result':'success'},status=status.HTTP_200_OK);
"""
logout user
"""
def Logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')

	
