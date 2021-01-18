from rest_framework import serializers
from home.models import *
from account.models import Account
from trainer.models import *
from home.models import *
from django.contrib.auth import authenticate, logout

class login_details_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields ='__all__'
class loginSerializer(serializers.Serializer):
	
	email = serializers.EmailField()
	password = serializers.CharField(max_length=256)
	def validate(self, data):
		user = authenticate(**data)
		if user and user.is_active:
			if user.is_staff:
				return user
			raise serializers.ValidationError("You Are Not A Trainer")
		raise serializers.ValidationError("Email Or Password Is Does Not Match")
class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Courses
		fields ='__all__'
class TaskSerializer_info(serializers.ModelSerializer):
	class Meta:
		model = Course_info
		fields ='__all__'
class TrainercourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trainercourse
		fields ='__all__'
class discussionSerializer(serializers.ModelSerializer):
	class Meta:
		model = discussion
		fields =('TrainerId','Course_RandomId','Text')

class CoursecontentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course_page
		fields ='__all__'