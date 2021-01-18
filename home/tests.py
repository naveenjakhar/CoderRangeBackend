from django.test import TestCase
from home.models import *
from account.models import Account

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)
class ViewsTestCaseCommunity(TestCase):
    def test_Community_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/Jvt/welcome/Community')
        self.assertEqual(response.status_code, 200)
class ViewsTestCasevision(TestCase):
    def test_vision_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/jvt/vision')
        self.assertEqual(response.status_code, 200)
class ViewsTestCaseCareers(TestCase):
    def test_Careers_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/Jvt/Careers')
        self.assertEqual(response.status_code, 200)

class Courses_test(TestCase):
    def setUp(self):
        print("creating table info..")
        Courses.objects.create(
            courseName              ="python",
            titleName               ="this is python",
            tags                    ="data structure",
            price                   =20000,
            pricePerClass           =500,
            color1                  ="white",
            color2                  ="black",
            from_age                =15,
            to_age                  =21,
            category                ="framework",
            course_Aim              ="us",
            current_Demandofcourse  ="indemand",
            projectscount           =2,
            rating                  =5,
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=Courses.objects.all()
        self.assertEqual(items.count(),1)
        item=Courses.objects.filter(courseName="python")
        self.assertEqual(item[0].rating,5)
        
        
class Course_info_test(TestCase):
    def setUp(self):
        print("creating table info..")
        course=Courses.objects.create(
            courseName              ="python",
            titleName               ="this is python",
            tags                    ="data structure",
            price                   =20000,
            pricePerClass           =500,
            color1                  ="white",
            color2                  ="black",
            from_age                =15,
            to_age                  =21,
            category                ="framework",
            course_Aim              ="us",
            current_Demandofcourse  ="indemand",
            projectscount           =2,
            rating                  =5,
        )
        Course_info.objects.create(
            coursesId_id    =course.id,
            courseContent   ="data,structure",
            classesCount    =25,
            prerequisites   ="ntg",
            benifits        ="ntg",
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=Course_info.objects.all()
        self.assertEqual(items.count(),1)
        item=Course_info.objects.filter(coursesId=1)
        self.assertEqual(item[0].classesCount,25)
        
        
class Democlasstest(TestCase):
    def setUp(self):
        print("creating table info..")
        course=Courses.objects.create(
            courseName              ="python",
            titleName               ="this is python",
            tags                    ="data structure",
            price                   =20000,
            pricePerClass           =500,
            color1                  ="white",
            color2                  ="black",
            from_age                =15,
            to_age                  =21,
            category                ="framework",
            course_Aim              ="us",
            current_Demandofcourse  ="indemand",
            projectscount           =2,
            rating                  =5,
        )
        Democlass.objects.create(
            coursesId_id         =course.id,
            email                ="mahi@gmail.com",
            kid_Age              =25,
            phonenumber          ="ntg",
            lapptop_availability ="ntg",
            date                 ="07-01-1999",
            timezone             ="7pm"
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=Democlass.objects.all()
        self.assertEqual(items.count(),1)
        item1=Democlass.objects.filter(email="mahi@gmail.com")
        self.assertEqual(item1[0].kid_Age,25)
        
        
class Democlass_otp_test(TestCase):
    def setUp(self):
        print("creating table info..")
        Democlass_otp.objects.create(
            otp                  ='101210',
            email                ="mahesh@gmail.com",
            kid_Age              =25,
            kidName              ="mahi",
            phonenumber          ="ntg",
            lapptop_availability ="ntg",
            date                 ="2017-09-27T16:19:24+0000",
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=Democlass_otp.objects.all()
        self.assertEqual(items.count(),1)
        item=Democlass_otp.objects.filter(email="mahesh@gmail.com")
        self.assertEqual(item[0].kid_Age,25)
        
        
class Coupons_test(TestCase):
    def setUp(self):
        print("creating table info..")
        Coupons.objects.create(
            course_name        ='python',
            kid_fromage        =15,
            kid_toage          =21,
            coupon             ="mahi",
            couponstart_date   ="2017-09-27",
            couponExpired_date ="2017-09-27",
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=Coupons.objects.all()
        self.assertEqual(items.count(),1)
        item=Coupons.objects.filter(course_name='python')
        self.assertEqual(item[0].kid_toage,21)
        
        
class Review_test(TestCase):
    def setUp(self):
        print("creating table info..")
        user=Account.objects.create(
            email="mahesh@gmail.com",
            password="mahi1432",
            username="mahesh",
            phonenumber=9490064206
        )
        Review.objects.create(
            userId_id        =user.id,
            name             ="mahi",
            photo   ="media\pics\1-removebg_3FKGn5y.png",
            comments ="very nice",
            rating=5
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=Review.objects.all()
        self.assertEqual(items.count(),1)
        item=Review.objects.filter(name="mahi")
        self.assertEqual(item[0].rating,5)
        
        
class Career_test(TestCase):
    def setUp(self):
        print("creating table info..")
        Career.objects.create(
            name             ="mahi",
            email            ="mahesh@gmail.com",
            phonenumber      =9490064206,
            linkdin          ="https://www.linkedin.com/in/maheswar-reddy-007/"
        )
        
    def test_course_info(self):
        print('testing courses..')
        items=Career.objects.all()
        self.assertEqual(items.count(),1)
        item=Career.objects.filter(name="mahi")
        self.assertEqual(item[0].email,"mahesh@gmail.com")
        
        