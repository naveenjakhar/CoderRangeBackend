from django.contrib import admin
from home import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Index,name='index'),
    # path('course',views.coursedemo,name='course'),
    path('course/fullCurriculum',views.full,name='full'),
    path('Your_msgs=/<int:id>',views.descussion,name='descussion'),
    path('jvt/vision',views.about,name='about'),
    path('Jvt/Careers',views.careers,name='Careers'),
    path('Jvt/welcome/Community',views.Community,name='Community'),
    path('course/Democlass/Signup',views.demo_class,name='Community'),
    path('course/Democlass/otp',views.democlass_signup,name='democlass_signup'),
    path('course/Democlass/done',views.demo_sign,name='demo_sign'),
    path('otp/resend',views.resend,name='resend'),
    path('course/calender',views.calander,name='calander'),
    path('course/Buy',views.Purchase_course,name='Purchase_course'),
    path('success',views.success,name='success'),
    path('demo/course/otp',views.democourse_otp,name='otp'),
    path('course/<int:age>',views.All_course,name='otp'),
    path('Profile/user=/<int:myid>',views.profile,name='profile'),
    path('Profile/user=/feedback/<int:myid>',views.feedback,name='feedback'),
    path('feedback/trainer',views.feedback_trainer,name='feedback_trainer'),
    path('profile/<int:myid>',views.profile_img,name='profile_img'),
    path('course/search',views.search,name='search'),
]