from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(customer)
class ProfileAdmin(admin.ModelAdmin):
    search_fields=['userId']
    list_display=['userId','state']
    
admin.site.register(Profile,ProfileAdmin)

class CourseAdmin(admin.ModelAdmin):
    search_fields=['courseName','from_age']
    list_display=['id','courseName','from_age','category']
    ordering =['id','from_age']
    list_filter = ['current_Demandofcourse','from_age','rating']
    list_per_page=10
    
class info(admin.ModelAdmin):
    search_fields=['coursesId','classesCount']
    list_display=['coursesId','classesCount']
    
class PurchaseAdmin(admin.ModelAdmin):
    search_fields=['userid','coursesId']
    list_display=['userid','coursesId','status']
    ordering =['paymentDate']
    list_filter = ['status','paymentDate']
    list_per_page=10
    
class DemoclassAdmin(admin.ModelAdmin):
    search_fields=['coursesId','email']
    list_display=['coursesId','email']
    list_per_page=10
class Course_pageAdimn(admin.ModelAdmin):
    search_fields=['courseId','sectionName']
    list_display=['courseId','sectionName']
    list_per_page=10
admin.site.register(Course_info,info)
admin.site.register(Courses,CourseAdmin)
admin.site.register(Democlass,DemoclassAdmin)
admin.site.register(Democlass_otp)
admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(Career)
admin.site.register(Course_page,Course_pageAdimn)