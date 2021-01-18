from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class MyAccountManager(BaseUserManager):
	def create_user(self, email,username,phonenumber,password):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		user = self.model(
			email=self.normalize_email(email),
			username=username,
            phonenumber=phonenumber
		)
		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self,email,username,phonenumber,password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
            phonenumber=phonenumber,
            username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
    email                   = models.EmailField(verbose_name="email", max_length=35, unique=True) 
    password                = models.CharField(max_length=256)
    username                 = models.CharField(max_length=15)
    phonenumber             = models.CharField(max_length=15)
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username','phonenumber']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
class Student(models.Model):
    studentId               =models.OneToOneField(Account,on_delete=models.CASCADE)
    email                   = models.EmailField(verbose_name="email", max_length=35, unique=True)
    kidname                 = models.CharField(max_length=25)
    country                 = models.CharField(max_length=15)
    kid_age                 = models.CharField(max_length=15)
    phonenumber             = models.CharField(max_length=15)
    lapptop_availability    = models.CharField(max_length=3)
    
class Parent(models.Model):
    parentId               =models.OneToOneField(Account,on_delete=models.CASCADE)
    email                   = models.EmailField(verbose_name="email", max_length=35, unique=True)
    kidname                 = models.CharField(max_length=25,blank=True)
    parent_name              = models.CharField(max_length=25,blank=True)
    country                 = models.CharField(max_length=15,blank=True)
    kid_age                 = models.CharField(max_length=15,blank=True)
    phonenumber             = models.CharField(max_length=15,blank=True)
    lapptop_availability    = models.CharField(max_length=3,blank=True)

class Trainer(models.Model):
    TrainerId               =models.OneToOneField(Account,on_delete=models.CASCADE)
    email                   = models.EmailField(verbose_name="email", max_length=35, unique=True)
    Trainername             = models.CharField(max_length=25,blank=True)
    teachingCourse          = models.CharField(max_length=25,blank=True)
    course_age              = models.CharField(max_length=15,blank=True)
    phonenumber             = models.CharField(max_length=15,blank=True)
    timing_availability     = models.CharField(max_length=50,blank=True)
    status                  = models.CharField(max_length=50,blank=True,default='Free')

class PhoneOTP(models.Model):
    # phone_regex = RegexValidator( regex = r'^\+?1?\d{9,10}$', message ="Phone number must be entered in the format +919999999999. Up to 14 digits allowed.")
    phone       = models.CharField(max_length=15)
    otp         = models.CharField(max_length=9, blank = True, null=True)
    count       = models.IntegerField(default=0, help_text = 'Number of otp_sent')
    kid_age       = models.CharField(max_length=10)
    kidname    = models.CharField(max_length=20)
    country    = models.CharField(max_length=20)
    category    = models.CharField(max_length=20)
    parentName    = models.CharField(max_length=20)
    kid_Aim    = models.CharField(max_length=20)
    lapptop_availability= models.CharField(max_length=20 )
    email       = models.CharField(max_length=50, null = True, blank = True, default = None) 
    password    = models.CharField(max_length=100, null = True, blank = True, default = None)       
    date    = models.DateTimeField(default=None)

    def __str__(self):
        return str(self.phone) + ' is sent ' + str(self.otp)

class Forgot_otp(models.Model):
    phonenumber=models.CharField(max_length=15)
    otp        =models.CharField(max_length=6)
    date       = models.DateTimeField(default=None)