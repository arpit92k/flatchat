from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields = ('id','email','username','first_name','last_name')

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('username','password')

class SignupSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('username','email','password','first_name','last_name')
