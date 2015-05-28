from rest_framework import serializers
from authAPI.models import UserInfo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	about = serializers.PrimaryKeyRelatedField(many=True, queryset=UserInfo.objects.all())
	class Meta:
		model=User
		fields = ('id','username','email','about')

class UserInfoSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model=UserInfo
		fields=('id','owner','about')
