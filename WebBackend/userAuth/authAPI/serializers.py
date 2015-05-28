from rest_framework import serializers
from django.contrib.auth.models import User
from authAPI.models import UserProfile

"""
serilizer of listing users
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields = ('id','email','username','first_name','last_name','locality','budget')

"""
serializer for login form
"""
class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserProfile
		fields=('username','password')

"""
serializer for register form
"""
class SignupSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserProfile
		fields=('username','email','password','first_name','last_name')
