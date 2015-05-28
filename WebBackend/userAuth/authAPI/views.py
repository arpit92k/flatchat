from authAPI.serializers import UserSerializer,LoginSerializer,SignupSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from authAPI.permissions import IsOwnerOrReadonly
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import UserManager

#to list all users
class UserList(generics.ListAPIView):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

#to list a user or update loggedin user
class UserInfoDetail(generics.RetrieveUpdateAPIView):
	permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadonly,)
    	queryset = User.objects.all()
    	serializer_class = UserSerializer

#to register user
class SignupUser(generics.CreateAPIView):
	serializer_class=SignupSerializer
        def create(self,serializer):
		if self.request.user.is_authenticated():
                        return HttpResponseRedirect('/user/')
		User.objects.create_user(username=self.request.POST['username'],email=self.request.POST['email'],password=self.request.POST['password'])
		return HttpResponseRedirect('/login/')

#login a user
class Login(generics.CreateAPIView):
	serializer_class=LoginSerializer
	def create(self,serializer):
		if self.request.user.is_authenticated():
			return HttpResponseRedirect('/user/')
		user = authenticate(username=self.request.POST['username'], password=self.request.POST['password'])
		if user is not None:
			login(self.request, user)
			return HttpResponseRedirect('/user/')
		else:
			return HttpResponseRedirect('/login/')

#logout user
def Logout(request):
	logout(request)
	return HttpResponseRedirect('/login/')

	

		
"""
@api_view(['POST'])
def login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST["username"],password=request.POST["password"])
                if user is not None:
                        return HttpResponseRedirect("/user/")
                else:
                        return HttpResponseRedirect("/login/")
	if request.method == 'PGET':
		return render(request, 'login.html')
		
"""
