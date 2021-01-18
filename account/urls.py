from django.contrib import admin
from django.urls import path
from account import views
from .views import *
urlpatterns = [
    # path('',views.index,name='index'),
    path('account/login',views.login,name='login'),
    path('Signup/<str:name>',views.phoneotp,name='login'),
    
    # path('SSignup',views.sudent,name='login'),
    # path('PSignup',views.perant,name='login'),
    path('number/opt',views.opt,name='login'),
    path('resend_count/opt',views.resend_otp,name='login'),
    path('forgot/password/number',views.forgot_password_number,name='forgot_password_number'),
    path('forgot/password/otp',views.forgot_password_otp,name='forgot_password_otp'),
    path('forgot/password',views.forgot_password,name='forgot_password'),
    path('forgot/forgot_resend/opt',views.forgot_resend,name='forgot_password'),
    path('logout',views.logout_view,name='signup')
]