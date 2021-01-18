from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from account.models import Account
####Customer details#####


class Profile(models.Model):
    userId = models.ForeignKey(Account, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='pics', default=False, null=True, blank=True)
    address = models.CharField(max_length=15, null=True, blank=True)
    kid_age = models.CharField(max_length=15, null=True, blank=True)
    town = models.CharField(max_length=15, null=True, blank=True)
    state = models.CharField(max_length=15, null=True, blank=True)
    dist = models.CharField(max_length=15, null=True, blank=True)
    pincode = models.CharField(max_length=7, null=True, blank=True)
    schoolName = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=15, null=True, blank=True)


class UserProjects(models.Model):
    userId = models.ForeignKey(Account, on_delete=models.CASCADE)
    projectname = models.CharField(max_length=50)
    projectabout = models.CharField(max_length=200)
    demo_img = models.ImageField(upload_to='pics')
    files = models.FileField(upload_to='files')
    rating = models.IntegerField(default=0)


class Projectviews(models.Model):
    userId = models.ForeignKey(Account, on_delete=models.CASCADE)
    projectId = models.ForeignKey(UserProjects, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

# courses according to ages and locations


class Courses(models.Model):
    courseName = models.CharField(max_length=50)
    titleName = models.CharField(max_length=200)
    tags = models.CharField(max_length=50)
    price = models.IntegerField()
    pricePerClass = models.IntegerField()
    color1 = models.CharField(max_length=10)
    color2 = models.CharField(max_length=10)
    from_age = models.IntegerField()
    to_age = models.IntegerField()
    category = models.CharField(max_length=20)
    course_Aim = models.CharField(max_length=20)
    current_Demandofcourse = models.CharField(max_length=20)
    projectscount = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.courseName

#####course stages###


class Course_info(models.Model):
    coursesId = models.OneToOneField(Courses, on_delete=models.CASCADE)
    courseContent = models.TextField()
    classesCount = models.IntegerField()
    prerequisites = models.TextField()
    benifits = models.TextField()


class Course_page(models.Model):
    courseId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    sectionName = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/', null=True)
    video = models.FileField(upload_to='video/', null=True)
    content = RichTextField(blank=True, null=True)


class Democlass(models.Model):
    coursesId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="email", max_length=35)
    kidName = models.CharField(max_length=25)
    kid_Age = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=15)
    lapptop_availability = models.CharField(max_length=3)
    date = models.CharField(max_length=15)
    timezone = models.CharField(max_length=9)

    def __str__(self):
        return self.kidName


class Democlass_otp(models.Model):
    otp = models.CharField(max_length=6)
    email = models.EmailField(verbose_name="email", max_length=35, unique=True)
    kidName = models.CharField(max_length=25)
    kid_Age = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=15)
    lapptop_availability = models.CharField(max_length=3)
    validate = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)


class Batchtype(models.Model):
    userId = models.ForeignKey(Account, on_delete=models.CASCADE)
    coursesId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    classtype = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
####### Offers each course according to ages#####


class Coupons(models.Model):
    course_name = models.CharField(max_length=100)
    kid_fromage = models.IntegerField()
    kid_toage = models.IntegerField()
    coupon = models.CharField(max_length=50)
    couponstart_date = models.DateField()
    couponExpired_date = models.DateField()


class Certification(models.Model):
    userId = models.ForeignKey(Account, on_delete=models.CASCADE)
    coursesId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    certificate = models.FileField(upload_to='files')

# REVIEWS


class Review(models.Model):
    userId = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='pics')
    comments = models.CharField(max_length=1000)
    rating = models.IntegerField()

# In payment gateway we only get transaction id and Tocken(success or failed)


class Purchase(models.Model):
    userid = models.ForeignKey(Account, on_delete=models.CASCADE)
    coursesId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    paymentDate = models.DateField()
    ammount = models.IntegerField()
    transactionid = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

# class Payment(models.Model):
#     userid                  =models.ForeignKey(Account,on_delete=models.CASCADE)
#     coursesId               =models.ForeignKey(Courses,on_delete=models.CASCADE)
#     paymentDate             =models.DateField()
#     ammount                 =models.IntegerField()
#     transactionid           =models.CharField(max_length=50)
#     paymentStatus           =models.CharField(max_length=50,default='pending')


class Refund(models.Model):
    userid = models.ForeignKey(Account, on_delete=models.CASCADE)
    coursesId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    refund_requestDate = models.DateField()
    refundDate = models.DateField()
    ammount = models.IntegerField()
    reason = models.CharField(max_length=100)
    transactionid = models.CharField(max_length=50)
    paymentStatus = models.CharField(max_length=50, default='pending')


class Helpdesk(models.Model):
    userId = models.ForeignKey(Account, on_delete=models.CASCADE)
    coursesId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    paymentid = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    query = models.CharField(max_length=500)
    img = models.ImageField(upload_to='pics')
    mobile_Number = models.IntegerField()
    status = models.CharField(max_length=50)


class Solutiondesk(models.Model):
    instructedBy = models.ForeignKey(Account, on_delete=models.CASCADE)
    queryId = models.ForeignKey(Helpdesk, on_delete=models.CASCADE)
    solution = models.CharField(max_length=500)
    status = models.CharField(max_length=50)


class Career(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    linkdin = models.URLField(max_length=200)
