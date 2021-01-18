from django.test import TestCase
from account.models import *
# Create your tests here.

class Account_test(TestCase):
    def setUp(self):
        print("creating table info..")
        Account.objects.create(
            email="mahesh@gmail.com",
            password="mahi1432",
            username="mahesh",
            phonenumber=9490064206
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=Account.objects.all()
        self.assertEqual(items.count(),1)
        item=Account.objects.filter(username="mahesh")
        self.assertEqual(item[0].phonenumber,'9490064206')
        
        
class Parent_test(TestCase):
    def setUp(self):
        print("creating table info..")
        user=Account.objects.create(
            email="mahesh@gmail.com",
            password="mahi1432",
            phonenumber=9490064206
        )
        Parent.objects.create(
            parentId_id=user.id,
            email="mahesh@gmail.com",
            kidname="mahesh",
            parent_name="mahesh",
            kid_age=5,
            lapptop_availability="yes",
            country="india",
            phonenumber=9490064206
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=Parent.objects.all()
        self.assertEqual(items.count(),1)
        item=Parent.objects.filter(kidname="mahesh")
        self.assertEqual(item[0].phonenumber,'9490064206')
        
        
class Student_test(TestCase):
    def setUp(self):
        print("creating table info..")
        user=Account.objects.create(
            email="mahesh@gmail.com",
            password="mahi1432",
            phonenumber=9490064206
        )
        Student.objects.create(
            studentId_id=user.id,
            email="mahesh@gmail.com",
            kidname="mahesh",
            kid_age=5,
            lapptop_availability="yes",
            country="india",
            phonenumber=9490064206
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=Student.objects.all()
        self.assertEqual(items.count(),1)
        item=Student.objects.filter(kidname="mahesh")
        self.assertEqual(item[0].phonenumber,'9490064206')
        
        
class Trainer_test(TestCase):
    def setUp(self):
        print("creating table info..")
        user=Account.objects.create(
            email="mahesh@gmail.com",
            password="mahi1432",
            phonenumber=9490064206
        )
        Trainer.objects.create(
            TrainerId_id=user.id,
            email="mahesh@gmail.com",
            Trainername="mahesh",
            teachingCourse="python",
            course_age=5,
            timing_availability="yes",
            status="Free",
            phonenumber=9490064206
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=Trainer.objects.all()
        self.assertEqual(items.count(),1)
        item=Trainer.objects.filter(Trainername="mahesh")
        self.assertEqual(item[0].phonenumber,'9490064206')
        
        
class PhoneOTP_test(TestCase):
    def setUp(self):
        print("creating table info..")
        PhoneOTP.objects.create(
            email="mahesh@gmail.com",
            kidname="mahesh",
            parentName="mahi",
            country="india",
            kid_Aim='us',
            category="student",
            kid_age=5,
            lapptop_availability="yes",
            phone=9490064206,
            otp='123456',
            count=1,
            password="mahi1432",
            date='1999-01-01'
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=PhoneOTP.objects.all()
        self.assertEqual(items.count(),1)
        item=PhoneOTP.objects.filter(email="mahesh@gmail.com")
        self.assertEqual(item[0].phone,'9490064206')
        
        