from django.db import models
from ckeditor.fields import RichTextField
import uuid
from account.models import Account
from home.models import *
# Create your models here.

class Trainer_profile(models.Model):
    trainerId=models.ForeignKey(Account,on_delete=models.CASCADE)
    a_email=models.EmailField()
    a_mobileNumber=models.BigIntegerField()
    qualification=models.CharField(max_length=30)
    experience=models.IntegerField()
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    teaching_Course=models.CharField(max_length=50)
    courseAge_category=models.IntegerField()

class Trainercourse(models.Model):
    trainerId=models.ForeignKey(Account,on_delete=models.CASCADE)
    coaching_courseid=models.ForeignKey(Courses,on_delete=models.CASCADE)
    course_randId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    countOfStudent=models.IntegerField(default=0)
    time=models.IntegerField()

class Coursedetails(models.Model):
    Trainercourse=models.ForeignKey(Trainercourse,on_delete=models.CASCADE)
    studentId=models.ForeignKey(Account,on_delete=models.CASCADE)
    date_of_joined=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    # discription=models.CharField(max_length=100)

# #who is theaching and what is teaching



# ## daily task for trianer###

# class Class_activity(models.Model):
#     trainerId=models.ForeignKey(Account,on_delete=models.CASCADE)
#     coursesId=models.ForeignKey(Courses,on_delete=models.CASCADE)
#     status=models.BooleanField() ### weather completed or not 
#     teached_concepts=models.TextField()
#     today_left_concepts=models.TextField()
#     reason_for_left=models.CharField(max_length=50)

class Class_Review(models.Model):
    classid=models.ForeignKey(Trainercourse,on_delete=models.CASCADE)
    rating=models.IntegerField()
    textReview=models.TextField(default="",blank=True,null=True)
    date=models.DateField(default=timezone.now)
class discussion(models.Model):
    TrainerId=models.ForeignKey(Account,on_delete=models.CASCADE)
    Course_RandomId=models.CharField(max_length=150)
    Text=models.TextField()
    date=models.DateField(default=timezone.now)

# class Trainer_attendance(models.Model):
#     trainerId=models.ForeignKey(Account,on_delete=models.CASCADE)
#     date=models.DateField()
#     percentage=models.CharField(max_length=4,default='0%')

# class Class_attendance(models.Model):
#     trainerId=models.ForeignKey(Account,on_delete=models.CASCADE)
#     coursesId=models.ForeignKey(Courses,on_delete=models.CASCADE)
#     studentsid=models.CharField(max_length=10) # storing allattended students id's here
#     date=models.DateField()
#     strength_class=models.IntegerField()
# class Application(models.Model):
#     name=models.CharField(max_length=50)
#     email=models.EmailField()
#     mobile_Number=models.BigIntegerField()
#     qualification=models.CharField(max_length=20)