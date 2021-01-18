from django.shortcuts import render,redirect
from django.utils.timezone import datetime
from django.contrib.auth.models import User,auth
from .models import *
from account.models import *
from django.contrib.auth import authenticate
from account.extrafun import *
from trainer.models import *
from .forms import *
from django.contrib import messages
from decouple import config
import razorpay
from trainer.views import Assigning_tainer
from django.views.decorators.csrf import csrf_exempt


account_sid = config('account_sid')
auth_token = config('auth_token')


def Index(request):
    '''
    returns all courses according to ages..
    Profile is nothing but user details,PO is personal object if user is not present then have to take static profile img..
    '''
    Course=Courses.objects.all().order_by('id')
    age9=[]
    age12=[]
    age15=[]
    for R in Course:
        if R.from_age==9:
            age9.append(R)
        elif R.from_age==12:
            age12.append(R)
        else:
            age15.append(R)
    myid=request.user.id
    if Profile.objects.filter(userId=myid).exists():
            profile=Profile.objects.filter(userId=myid)
            p=profile[0]
            po=1
    else:
        po=0
        p='False'
    courses={
        'course_age_9':age9,
        'course_age_12':age12,
        'course_age_15':age15,
        'profile':p,
        'po':po
    }
    return render(request,'home.html',courses)
def All_course(request,age):
    course=Courses.objects.filter(from_age=age)
    new1=Courses.objects.filter(from_age=age).order_by('-id')
    new=new1[0:5]
    myid=request.user.id
    if Profile.objects.filter(userId=myid).exists():
            profile=Profile.objects.filter(userId=myid)
            p=profile[0]
            po=1
    else:
        po=0
        p='False'
    courses={
        'profile':p,
        'po':po,
        'course':course,
        'new':new
    }
    return render(request,'allcourses.html',courses)
def search(request):
    if request.method=='POST':
        age=request.POST['Grade1']
        search=request.POST['item']
        item=Courses.objects.filter(from_age=age)
        course=[]
        for i in item:
            if search.lower() in i.courseName.lower():
                course.append(i)
        items=Courses.objects.filter(current_Demandofcourse='Future').order_by('-id')
        recom=items[0:3]
        myid=request.user.id
        if Profile.objects.filter(userId=myid).exists():
                profile=Profile.objects.filter(userId=myid)
                p=profile[0]
                po=1
        else:
            po=0
            p='False'
        courses={
            'profile':p,
            'po':po,
            'course':course,
            'recom':recom
        }
        return render(request,'searchcourse.html',courses)
def full(request):
    if request.method=="POST":
        courseid=request.POST['courseid']
        course=Courses.objects.filter(id=courseid)
        info=Course_info.objects.filter(coursesId_id=courseid)
        lists=makelist(info[0].courseContent)
        return render(request,'full.html',{'lists':lists,'course':course[0],'info':info[0]})
def about(request):
    myid=request.user.id
    if Profile.objects.filter(userId=myid).exists():
            profile=Profile.objects.filter(userId=myid)
            p=profile[0]
            po=1
    else:
        po=0
        p='False'
    courses={
        'profile':p,
        'po':po,
    }
    return render(request,'vision.html',courses)
def feedback(request,myid):
    request.session['feedback_course']=myid
    return render(request,'formpage.html')
def feedback_trainer(request):
    if request.method=='POST':
        # Class_Review
        userid=request.user.id
        courseid=request.session.get('feedback_course')
        # print(userid,courseid)
        item=Coursedetails.objects.filter(studentId=userid)
        for item in item:
            print(item.Trainercourse_id)
            course1=Trainercourse.objects.filter(coaching_courseid_id=courseid,course_randId=item.Trainercourse_id)
            if course1:
                break;
        print(course1)
        courses_id=course1[0].course_randId
        print(courses_id)
        rating=request.POST['experience']
        feedback=request.POST['comments']
        items=Class_Review(rating=int(rating),textReview=feedback)
        items.classid_id=courses_id
        items.save()
        return redirect('/Profile/user=/'+str(userid))
        
def careers(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        linkdin=request.POST['link']
        item=Career(name=name,email=email,phonenumber=phone,linkdin=linkdin)
        item.save()
        messages.info(request,'Your Details Are Submitted')
        return redirect('/Jvt/Careers')
    else:
        myid=request.user.id
        if Profile.objects.filter(userId=myid).exists():
                profile=Profile.objects.filter(userId=myid)
                p=profile[0]
                po=1
        else:
            po=0
            p='False'
        courses={
            'profile':p,
            'po':po,
        }
        return render(request,'careers.html',courses) 
def Community(request):
    myid=request.user.id
    if Profile.objects.filter(userId=myid).exists():
            profile=Profile.objects.filter(userId=myid)
            p=profile[0]
            po=1
    else:
        po=0
        p='False'
    courses={
        'profile':p,
        'po':po,
    }
    return render(request,'community.html',courses) 
def demo_class(request):
    today=datetime.today()
    month1=today.month
    h1=today.strftime('%H')
    m1=today.strftime('%M')
    day1=today.day
    items=Democlass_otp.objects.all().order_by('id')
    for items in items:
        date=items.date
        day=date.day
        month=today.month
        h=date.strftime('%H')
        m=date.strftime('%M')
        m1=int(m1)-3
        if int(month1)<int(month):
            Democlass_otp.objects.filter(phonenumber=items.phonenumber).delete()
        elif int(month1)==int(month) and int(day)<int(day1):
            Democlass_otp.objects.filter(phonenumber=items.phonenumber).delete()
        elif int(month1)==int(month) and int(day1)==int(day) and int(h)<int(h1):
            Democlass_otp.objects.filter(phonenumber=items.phonenumber).delete()
        elif int(month1)==int(month) and int(day1)==int(day) and int(h1)==int(h) and int(m)<m1:
            Democlass_otp.objects.filter(phonenumber=items.phonenumber).delete()
    if request.method=="POST":
        courseid=request.POST['courseid']
        request.session['Course_id']=courseid
        userid=request.user.id
        if userid:
            # print(userid,'mahi',courseid)
            username=Account.objects.filter(id=userid)
            student=Student.objects.filter(studentId=userid)
            parent=Parent.objects.filter(parentId=userid)
            email=username[0].email
            phone=username[0].phonenumber
            request.session['demo_phonenumber']=phone
            if Democlass.objects.filter(coursesId=courseid,phonenumber=phone):
                messages.info(request,'You Have Already Registered For This Course,ContactUs Need Any Help')
                return redirect('/')
            kidName=username[0].username
            if Democlass_otp.objects.filter(email=email).exists():
                Democlass_otp.objects.filter(email=email).delete()
            if parent:
                Kid_Age=parent[0].kid_age
                lapptop_availability=parent[0].lapptop_availability
            else:
                Kid_Age=student[0].kid_age
                lapptop_availability=student[0].lapptop_availability
            validate='True'
            date=datetime.today()
            otp=''
            item=Democlass_otp(email=email,kidName=kidName,kid_Age=Kid_Age,phonenumber=phone,lapptop_availability=lapptop_availability
            ,validate=validate,date=date,otp=otp)
            item.save()
            return redirect('/course/calender')
        return render(request,'demo_signup.html')
def democlass_signup(request):
    if request.method=="POST":
        opt1=ran_otp()
        msg_body='''
        Your otp for Demo class:)
        Your otp to verify for coderRange.com:'''
        msg_body=msg_body+opt1
        code=request.POST['code']
        today=datetime.today()
        number=request.POST['Mobile_number']
        phone=code+number
        request.session['Phonenumber']=phone
        form=Demo_Form_otp(request.POST)
        courseid1=request.session.get('Course_id')
        if Democlass.objects.filter(coursesId=courseid1,phonenumber=phone):
            messages.info(request,'You Have Already Registered For This Course,ContactUs Need Any Help')
            return redirect('/course/Democlass/Signup')
        else:
            if Democlass_otp.objects.filter(phonenumber=phone):
                Phonenumber = Democlass_otp.objects.filter(phonenumber=phone)
                if Phonenumber.exists():
                    Democlass_otp.objects.filter(phonenumber=phone).update(otp=opt1)
                    send_sms(account_sid,auth_token,msg_body,'+18434080524',phone)
                    return redirect('/demo/course/otp')
            else:
                if form.is_valid():
                    instance=form.save(commit=False)
                    instance.phonenumber=phone
                    instance.otp=opt1
                    instance.date=today
                    instance.save()
                    send_sms(account_sid,auth_token,msg_body,'+18434080524',phone)
                    return redirect('/demo/course/otp')
def resend(request):
    opt1=ran_otp()
    msg_body='''
    Your otp for Demo class:)
    Your otp to verify for coderRange.com:'''
    msg_body=msg_body+opt1
    number=request.session.get('Phonenumber')
    if Democlass_otp.objects.filter(phonenumber=number):
        Phonenumber = Democlass_otp.objects.filter(phonenumber=number)
            # Resendotp
        if Phonenumber.exists():
            Democlass_otp.objects.filter(phonenumber=number).update(otp=opt1)
            send_sms(account_sid,auth_token,msg_body,'+18434080524',number)
            return redirect('/demo/course/otp')
    else:
        messages.info(request,'Your Details Expired Please Try Again')
        return redirect('/forgot/password/otp')


def democourse_otp(request):
    number=request.session.get('Phonenumber')
    if request.method =='POST':
        otp=request.POST['opt']
        if Democlass_otp.objects.filter(phonenumber=number,otp=otp):
            Democlass_otp.objects.filter(phonenumber=number,otp=otp).update(validate='True')
            request.session['demo_phonenumber']=number
            return redirect('/course/calender')
        else:
            messages.info(request,'Incorrect Otp')
            return redirect('/demo/course/otp')
    else:
        return render(request, 'demo_course_message.html',{'number':number})



def calander(request):
    today=datetime.today()
    day1=today.day
    mo=today.strftime('%B')
    month=mo[0:3]
    year=today.year
    day2=day1+1
    day3=day1+2
    clander={
        'day1':day1,
        'day2':day2,
        'day3':day3,
        'month':month,
        'year':year,
    }
    return render(request,'calendar.html',clander)



def demo_sign(request):
    if request.method == "POST":
        number=request.session.get('demo_phonenumber')
        if Democlass_otp.objects.filter(phonenumber=number,validate='True').exists():
            account1=Democlass_otp.objects.filter(phonenumber=number,validate='True')
            day1=request.POST['date']
            time=request.POST['Grade']
            today=datetime.today()
            mo=today.strftime('%B')
            month=mo[0:3]
            year=today.year
            finaldate=str(month)+' '+str(day1)+','+str(year)
            courseid=request.session.get('Course_id')
            KidName=account1[0].kidName
            email=account1[0].email
            phone=account1[0].phonenumber
            Kid_Age=account1[0].kid_Age
            Lapptop_availability=account1[0].lapptop_availability
            info=Courses.objects.filter(id=courseid)
            msg_body='''
             is registerd demo class for '''
            web='''
            coderRange.com:'''
            msg_body=KidName+msg_body+info[0].courseName+web
            form=Democlass(email=email,kidName=KidName,kid_Age=Kid_Age,phonenumber=phone,date=finaldate,timezone=time,lapptop_availability=Lapptop_availability)
            instance=form
            instance.phonenumber=phone
            instance.coursesId_id=courseid
            instance.save()
            Democlass_otp.objects.filter(phonenumber=number,validate='True').delete()
            send_sms(account_sid,auth_token,msg_body,'+18434080524',phone)
            return redirect('/')



def Purchase_course(request):
    if request.method=="POST":
        courseid=request.POST['courseid']
        R=Courses.objects.filter(id=courseid)
        userid=request.user.id
        if Purchase.objects.filter(coursesId=courseid,userid=userid,status=True).exists():
            return redirect('/Profile/user=/'+str(userid))
        else:
            Purchase.objects.filter(coursesId=courseid,userid=userid,status=False).delete()
            date=datetime.today()
            amount=(R[0].price)*100
            amount=(amount*.18)+amount
            client = razorpay.Client(auth =("rzp_test_EL0CgmCc3DbVfk" , "Zdvcs8kQHHGWucUbrJ6n7EM1"))
            payment = client.order.create({'amount':amount, 'currency':'INR','payment_capture':'1'})
            order_status=payment['status']
            if order_status=='created':
                order=Purchase(paymentDate=date,ammount=amount,transactionid=payment['id'])
                instance=order
                instance.userid_id=userid
                instance.coursesId_id=courseid
                instance.save()
                customer=Account.objects.filter(id=userid)
                amo={
                    'payment':payment,
                    'course':R[0],
                    'course1':R[0].price,
                    'customer':customer[0]
                }
                return render(request,"checkout.html",amo)
            else:
                return render(request,"faild.html")
@csrf_exempt
def success(request):
    if request.method == "POST":
        client = razorpay.Client(auth =("rzp_test_EL0CgmCc3DbVfk" , "Zdvcs8kQHHGWucUbrJ6n7EM1"))
        response = request.POST
        params_dict={
            'razorpay_payment_id':response['razorpay_payment_id'],
            'razorpay_order_id':response['razorpay_order_id'],
            'razorpay_signature':response['razorpay_signature']
        }
        # print(params_dict)
        status = client.utility.verify_payment_signature(params_dict)
        if status == None:
            item=Purchase.objects.filter(transactionid=params_dict['razorpay_order_id'])
            ###Trainer assign
            a=Assigning_tainer(item)
            if a == True:
                Purchase.objects.filter(transactionid=params_dict['razorpay_order_id']).update(status=True)
                print("hey mahi")
                return render(request,'success.html',{'item':item[0]})
            else:
                print("hey mahi it's false here")
                Purchase.objects.filter(transactionid=params_dict['razorpay_order_id']).update(status=True)
                return render(request,'success.html',{'item':item[0]})
        else:
            return render(request,"faild.html")
    
def profile(request,myid):
    if request.method=='POST':
        kidname=request.POST['kidname']
        if kidname!='':
            if Parent.objects.filter(parentId=myid).exists():
                Parent.objects.filter(parentId=myid).update(kidname=kidname)
                Account.objects.filter(id=myid).update(username=kidname)
            elif Student.objects.filter(studentId=myid).exists():
                item=Student.objects.filter(studentId=myid).update(kidname=kidname)
                Account.objects.filter(id=myid).update(username=kidname)
        kid_age=request.POST['kid_age']
        address=request.POST['address']
        town=request.POST['town']
        state=request.POST['state']
        dist=request.POST['dist']
        pincode=request.POST['pincode']
        schoolName=request.POST['schoolName']
        country=request.POST['country']
        if Profile.objects.filter(userId=myid).exists():
            if address !='':
                Profile.objects.filter(userId=myid).update(address=address)
            if town !='':
                Profile.objects.filter(userId=myid).update(town=town)
            if state !='':
                Profile.objects.filter(userId=myid).update(state=state)
            if dist !='':
                Profile.objects.filter(userId=myid).update(dist=dist)
            if pincode !='':
                Profile.objects.filter(userId=myid).update(pincode=pincode)
            if schoolName !='':
                Profile.objects.filter(userId=myid).update(schoolName=schoolName)
            if country !='':
                Profile.objects.filter(userId=myid).update(country=country)
            if kid_age !='':
                Profile.objects.filter(userId=myid).update(kid_age=kid_age)
                if Parent.objects.filter(parentId=myid).exists():
                    Parent.objects.filter(parentId=myid).update(kid_age=kid_age)
                elif Student.objects.filter(studentId=myid).exists():
                    Student.objects.filter(studentId=myid).update(kid_age=kid_age)
            return redirect('/Profile/user=/'+str(myid))
        else:
            item=Profile(address=address,town=town,state=state,dist=dist,pincode=pincode,schoolName=schoolName,country=country)
            item.userId_id=myid
            item.save()
            return redirect('/Profile/user=/'+str(myid))
    else:
        user1=Account.objects.filter(id=myid)
        if Profile.objects.filter(userId=myid).exists():
            profile=Profile.objects.filter(userId=myid)
            purchase=Purchase.objects.filter(userid=myid,status=True)
            course=[]
            for purchase in purchase:
                it=purchase.coursesId.id
                i=Courses.objects.filter(id=it)
                course.append(i[0])
            count=0
            items=Courses.objects.filter(current_Demandofcourse='Future').order_by('-id')
            recom=items[0:3]
            return render(request,'profile1.html',{'user1':user1,'profile':profile[0],'course':course,'recom':recom})
        else:
            if Parent.objects.filter(parentId=myid).exists():
                item=Parent.objects.filter(parentId=myid)
                kid_ag=item[0].kid_age
            elif Student.objects.filter(studentId=myid).exists():
                item=Student.objects.filter(studentId=myid)
                kid_ag=item[0].kid_age
            item=Profile(kid_age=kid_ag)
            item.userId_id=myid
            item.save()
            profile=Profile.objects.filter(userId=myid)
            purchase=Purchase.objects.filter(userid=myid,status=True)
            course=[]
            for purchase in purchase:
                it=purchase.coursesId.id
                i=Courses.objects.filter(id=it)
                course.append(i[0])
            recom=[]
            count=0
            items=Courses.objects.filter(current_Demandofcourse='Future').order_by('-id')
            recom=items[0:3]
            return render(request,'profile1.html',{'user1':user1,'profile':profile[0],'course':course,'recom':recom})
def profile_img(request,myid):
    if request.method=='POST':
        if Profile.objects.filter(userId=myid).exists():
            instance=Profile.objects.get(userId=myid)
            form=img_Form(request.POST or None, request.FILES, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('/Profile/user=/'+str(myid))
        else:
            form=img_Form(request.POST or None, request.FILES)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.userId_id=myid
                instance.save()
                return redirect('/Profile/user=/'+str(myid))
def descussion(request,id):
    usermsg_id=Coursedetails.objects.filter(studentId=id)
    msg=[]
    if usermsg_id:
        for user in usermsg_id:
            user_msg=discussion.objects.filter(Course_RandomId=user.Trainercourse).order_by('-id')
            if user_msg:
                for i in user_msg:
                    msg.append(i)
    else:
        msg.append("You Don't have any messeges")
    return render(request,'msg.html',{'msg':msg})
def helpdesk(request,myid,payid):
    if request.method=='POST':
        ProductID=myid
        paymentid=payid
        form=helpdeskForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.Userid=request.user
            instance.ProductID=ProductID
            instance.Paymentid=paymentid
            instance.Status='Active'
            instance.save()
            return redirect('/')
def solutiondesk(request,Queryid):
    if request.method=='POST':
        form=solutiondeskForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.Userid=request.user
            instance.QueryId=Queryid
            instance.save()
            solutions=solutiondesk.objects.filter(QueryId=Queryid)
            if solutions[0].status in solved:                       ## Updating helpdesk status column #####
                helpdesk.objects.filter(id=Queryid).update(Status='Inactive(Query solved)')
            return redirect('/')