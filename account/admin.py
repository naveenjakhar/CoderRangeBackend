from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *

from .models import PhoneOTP,Student
admin.site.register(PhoneOTP)

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display=('id','username','is_admin')
    list_filter = ['is_admin','date_joined','is_staff']
    list_per_page = 10
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['studentId','email']
    list_display=['studentId','email','phonenumber']
    list_per_page=10
class ParentAdmin(admin.ModelAdmin):
    search_fields = ['parentId','email']
    list_display=['parentId','email','phonenumber']
    list_per_page=10
class TrainerAdmin(admin.ModelAdmin):
    search_fields = ['TrainerId','email']
    list_display=['Trainername','TrainerId','email','phonenumber','teachingCourse','course_age']
    list_filter=['teachingCourse','course_age']
    list_per_page=10
admin.site.register(Account,UserAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Parent,ParentAdmin)
admin.site.register(Trainer,TrainerAdmin)
admin.site.register(Forgot_otp)
