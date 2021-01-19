from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from .forms import AccountAuthenticationForm
from .models import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import settings
from .extrafun import send_sms, ran_otp
from django.contrib import messages
from decouple import config
from django.utils.timezone import datetime

# sms account details
account_sid = config('account_sid')
auth_token = config('auth_token')
# coding......


def phoneotp(request, name):
    today = datetime.today()
    day1 = today.day
    month1 = today.month
    h1 = today.strftime('%H')
    m1 = today.strftime('%M')
    items = PhoneOTP.objects.all().order_by('id')
    for items in items:
        date = items.date
        day = date.day
        month = today.month
        h = date.strftime('%H')
        m = date.strftime('%M')
        m1 = int(m1)-3
        if int(month1) < int(month):
            PhoneOTP.objects.filter(phone=items.phone).delete()
        elif int(month1) == int(month) and int(day) < int(day1):
            PhoneOTP.objects.filter(phone=items.phone).delete()
        elif int(month1) == int(month) and int(day1) == int(day) and int(h) < int(h1):
            PhoneOTP.objects.filter(phone=items.phone).delete()
        elif int(month1) == int(month) and int(day1) == int(day) and int(h1) == int(h) and int(m) < m1:
            PhoneOTP.objects.filter(phone=items.phone).delete()
    if name == 'Student':
        if request.method == 'POST':
            opt1 = ran_otp()
            msg_body = '''
            hello sir this is maheswarreddy peram otp task is done :)
            Your otp to verify for coderRange.com:'''
            msg_body = msg_body+opt1
            KidName = request.POST['kidName']
            email = request.POST['email']
            code = request.POST['code']
            number = request.POST['Mobile_number']
            Country = 'india'
            parentName = ''
            category = name
            phone = code+number
            request.session['Phone_number'] = phone
            Kid_Age = request.POST['KidAge']
            Lapptop_availability = request.POST['lapptop_availability']
            password = request.POST['password']
            if Lapptop_availability == 'No':
                messages.info(request, 'You Should Have Laptop')
                return redirect('/Signup/Student')
            else:
                if phone:
                    # Phone number exists
                    user = Account.objects.filter(phonenumber=phone)
                    if user.exists():
                        messages.info(request, 'mobile number taken')
                        return redirect('/Signup/Student')
                    else:                                                         # if Phone number not exists
                        Phonenumber = PhoneOTP.objects.filter(phone=phone)
                        # Resendotp
                        if Phonenumber.exists():
                            user = PhoneOTP.objects.filter(
                                phone=phone).update(otp=opt1)
                            send_sms(account_sid, auth_token,
                                     msg_body, '+14152003922', phone)
                            return redirect('/number/opt')
                        # New otp
                        else:
                            if Account.objects.filter(email=email).exists():
                                messages.info(request, 'Email already taken')
                                return redirect('/Signup/Student')
                            elif len(password) <= 6:
                                messages.info(
                                    request, 'Please enter password atleast 8 characters')
                                return redirect('/Signup/Student')
                            else:
                                user = PhoneOTP(kidname=KidName, password=password, phone=phone, email=email, parentName=parentName, otp=opt1,
                                                country=Country, kid_age=Kid_Age, category=category, lapptop_availability=Lapptop_availability, date=today)
                                user.save()
                                send_sms(account_sid, auth_token,
                                         msg_body, '+14152003922', phone)
                                return redirect('/number/opt')
                else:
                    messages.info(request, 'Phonenumber is not valid')
                    return render(request, 'signup.html')
        else:
            day1 = today.day
            month1 = today.month
            h1 = today.strftime('%H')
            m1 = today.strftime('%M')
            items = PhoneOTP.objects.all().order_by('id')
            for items in items:
                date = items.date
                day = date.day
                month = today.month
                h = date.strftime('%H')
                m = date.strftime('%M')
                m1 = int(m1)-3
                if int(month1) < int(month):
                    PhoneOTP.objects.filter(phone=items.phone).delete()
                elif int(month1) == int(month) and int(day) < int(day1):
                    PhoneOTP.objects.filter(phone=items.phone).delete()
                elif int(month1) == int(month) and int(day1) == int(day) and int(h) < int(h1):
                    PhoneOTP.objects.filter(phone=items.phone).delete()
                elif int(month1) == int(month) and int(day1) == int(day) and int(h1) == int(h) and int(m) < m1:
                    PhoneOTP.objects.filter(phone=items.phone).delete()
            return render(request, 'SSignup.html')
    else:
        if request.method == 'POST':
            opt1 = ran_otp()
            msg_body = '''
            hello sir this is maheswarreddy peram otp task is done :)
            Your otp to verify for coderRange.com:'''
            msg_body = msg_body+opt1
            KidName = request.POST['KidName']
            email = request.POST['email']
            code = request.POST['code']
            number = request.POST['Mobile_number']
            Country = 'india'
            parentName = request.POST['ParentName']
            category = name
            phone = code+number
            request.session['Phone_number'] = phone
            Kid_Age = request.POST['KidAge']
            Lapptop_availability = request.POST['lapptop_availability']
            password = request.POST['password']
            if phone:
                # Phone number exists
                user = Account.objects.filter(phonenumber=phone)
                if user.exists():
                    messages.info(request, 'mobile number taken')
                    return redirect('/Signup/Parent')
                else:                                                         # if Phone number not exists
                    Phonenumber = PhoneOTP.objects.filter(phone=phone)
                    # Resendotp
                    if Phonenumber.exists():
                        user = PhoneOTP.objects.filter(
                            phone=phone).update(otp=opt1)
                        send_sms(account_sid, auth_token,
                                 msg_body, '+14152003922', phone)
                        return redirect('/number/opt')
                    # New otp
                    else:
                        if Account.objects.filter(email=email).exists():
                            messages.info(request, 'Email already taken')
                            return redirect('/Signup/Parent')
                        elif len(password) <= 6:
                            messages.info(
                                request, 'Please enter password atleast 8 characters')
                            return redirect('/Signup/Student')
                        else:
                            user = PhoneOTP(kidname=KidName, password=password, phone=phone, email=email, parentName=parentName, otp=opt1,
                                            country=Country, kid_age=Kid_Age, category=category, lapptop_availability=Lapptop_availability, date=today)
                            user.save()
                            send_sms(account_sid, auth_token,
                                     msg_body, '+14152003922', phone)
                            return redirect('/number/opt')
            else:
                messages.info(request, 'Phonenumber is not valid')
                return render(request, 'signup.html')
        else:
            return render(request, 'PSignup.html')


def forgot_password_number(request):
    today = datetime.today()
    if request.method == 'POST':
        opt1 = ran_otp()
        msg_body = '''
        hello sir this is maheswarreddy peram otp task is done :)
        Your otp to verify for coderRange.com:'''
        msg_body = msg_body+opt1
        p_number = request.POST['number']
        code = request.POST['code']
        phone = code+p_number
        request.session['Phone_Forgot'] = phone
        if Forgot_otp.objects.filter(phonenumber=phone).exists():
            Forgot_otp.objects.filter(phonenumber=phone).update(otp=opt1)
            send_sms(account_sid, auth_token, msg_body, '+18434080524', phone)
            return redirect('/forgot/password/otp')
        else:
            item = Forgot_otp(phonenumber=phone, otp=opt1, date=today)
            item.save()
            p = send_sms(account_sid, auth_token,
                         msg_body, '+18434080524', phone)
            return redirect('/forgot/password/otp')
    else:
        day1 = today.day
        month1 = today.month
        h1 = today.strftime('%H')
        m1 = today.strftime('%M')
        items = Forgot_otp.objects.all().order_by('id')
        for items in items:
            date = items.date
            day = date.day
            month = today.month
            h = date.strftime('%H')
            m = date.strftime('%M')
            m1 = int(m1)-3
            if int(month1) < int(month):
                Forgot_otp.objects.filter(
                    phonenumber=items.phonenumber).delete()
            elif int(month1) == int(month) and int(day) < int(day1):
                Forgot_otp.objects.filter(
                    phonenumber=items.phonenumber).delete()
            elif int(month1) == int(month) and int(day1) == int(day) and int(h) < int(h1):
                Forgot_otp.objects.filter(
                    phonenumber=items.phonenumber).delete()
            elif int(month1) == int(month) and int(day1) == int(day) and int(h1) == int(h) and int(m) < m1:
                Forgot_otp.objects.filter(
                    phonenumber=items.phonenumber).delete()
        return render(request, 'forgotphone.html')


def forgot_resend(request):
    opt1 = ran_otp()
    msg_body = '''
    Your otp for Demo class:)
    Your otp to verify for coderRange.com:'''
    msg_body = msg_body+opt1
    number = request.session.get('Phone_Forgot')
    if Forgot_otp.objects.filter(phonenumber=number):
        Phonenumber = Forgot_otp.objects.filter(phonenumber=number)
        if Phonenumber.exists():
            Forgot_otp.objects.filter(phonenumber=number).update(otp=opt1)
            send_sms(account_sid, auth_token, msg_body, '+18434080524', number)
            return redirect('/forgot/password/otp')
    else:
        messages.info(request, 'Your Details Expired Please Try Again')
        return redirect('/forgot/password/otp')


def forgot_password_otp(request):
    number = request.session.get('Phone_Forgot')
    if request.method == 'POST':
        otp = request.POST['opt']
        if Forgot_otp.objects.filter(phonenumber=number, otp=otp).exists():
            Forgot_otp.objects.filter(phonenumber=number, otp=otp).delete()
            return redirect('/forgot/password')
        else:
            messages.info(request, 'Incorrect Otp')
            return redirect('/forgot/password/otp')
    else:
        return render(request, 'forgot_otp.html', {'number': number})


def forgot_password(request):
    if request.method == 'POST':
        password = request.POST['Password']
        Password1 = request.POST['Password1']
        if password == Password1:
            p_number = request.session.get('Phone_Forgot')
            if Account.objects.filter(phonenumber=p_number):
                u = Account.objects.get(phonenumber=p_number)
                u.set_password(password)
                u.save()
                return redirect('/')
            else:
                messages.info(request, 'Entered Mobile number is Wrong')
                return redirect('/forgot/password')
        else:
            messages.info(request, 'Password Not Matched')
            return redirect('/forgot/password')
    else:
        return render(request, 'newpassword.html')


def perant(request):
    return render(request, 'PSignup.html')


def sudent(request):
    return render(request, 'SSignup.html')


def resend_otp(request):
    opt1 = ran_otp()
    msg_body = '''
    Your otp for Demo class:)
    Your otp to verify for coderRange.com:'''
    msg_body = msg_body+opt1
    number = request.session.get('Phone_number')
    if PhoneOTP.objects.filter(phone=number):
        # print('mahi1')
        Phonenumber = PhoneOTP.objects.filter(phone=number)
        # Resendotp
        if Phonenumber.exists():
            # print('mahi')
            PhoneOTP.objects.filter(phone=number).update(otp=opt1)
            send_sms(account_sid, auth_token, msg_body, '+18434080524', number)
            return redirect('/number/opt')
    else:
        messages.info(request, 'Your Details Expired Please SignUP Again')
        return redirect('/number/opt')


def opt(request):
    number = request.session.get('Phone_number')
    if request.method == 'POST':
        otp = request.POST['opt']
        if PhoneOTP.objects.filter(phone=number, otp=otp).exists():
            account1 = PhoneOTP.objects.filter(phone=number, otp=otp)
            if account1[0].category == 'Student':
                KidName = account1[0].kidname
                email = account1[0].email
                phone = account1[0].phone
                password = account1[0].password
                country = account1[0].country
                kid_Age = account1[0].kid_age
                Lapptop_availability = account1[0].lapptop_availability
                user = Account.objects.create_user(
                    username=KidName, password=password, phonenumber=phone, email=email)
                user1 = Account.objects.filter(
                    username=KidName, phonenumber=phone)
                userid = user1[0].id
                student_obj = Student(kidname=KidName, email=email, country=country, kid_age=kid_Age,
                                      phonenumber=phone, lapptop_availability=Lapptop_availability)
                student_obj.studentId_id = userid
                student_obj.save()
                PhoneOTP.objects.filter(phone=number, otp=otp).delete()

                auth.login(request, user)
                return redirect('/')
            else:
                KidName = account1[0].kidname
                parentName = account1[0].parentName
                email = account1[0].email
                phone = account1[0].phone
                password = account1[0].password
                country = account1[0].country
                kid_Age = account1[0].kid_age
                Lapptop_availability = account1[0].lapptop_availability
                user = Account.objects.create_user(
                    username=parentName, password=password, phonenumber=phone, email=email)
                user1 = Account.objects.filter(
                    username=parentName, phonenumber=phone)
                userid = user1[0].id
                student_obj = Parent(kidname=KidName, parent_name=parentName, email=email, country=country,
                                     kid_age=kid_Age, phonenumber=phone, lapptop_availability=Lapptop_availability)
                student_obj.parentId_id = userid
                student_obj.save()
                PhoneOTP.objects.filter(phone=number, otp=otp).delete()
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request, 'Incorrect Otp')
            return redirect('/number/opt')
    else:
        return render(request, 'account_message.html', {'number': number})


def login(request):
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                auth_login(request, user)
                return redirect("/")
        else:
            messages.info(request, 'Email or Password Is Incorrect')
            return redirect('/account/login')
    else:
        return render(request, 'Login.html')


def logout_view(request):
    logout(request)
    return redirect('/')
