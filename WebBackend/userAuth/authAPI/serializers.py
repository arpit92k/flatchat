from rest_framework import serializers
from django.contrib.auth.models import User

#serilizer of listing users
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields = ('id','email','username','first_name','last_name')

#serializer for login form
class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('username','password')

#serializer for register form
class SignupSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('username','email','password','first_name','last_name')
