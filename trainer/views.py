from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from home.models import *
from account.models import Trainer
from account.extrafun import makelist
from trainer.models import *
from rest_framework.generics import GenericAPIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
# @csrf_exempt
class LoginView(GenericAPIView):
    serializer_class = loginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer1 = login_details_Serializer(user, many=False)
        return Response(serializer1.data)

def assigning(trainer, course, userid):
    timing = makelist(trainer.timing_availability)
    time = list(map(int, timing))
    time1 = timing[0:1]
    s = ''.join(map(str, time1))
    for time in time:
        item = Trainercourse(time=time, countOfStudent=0)
        instance = item
        instance.trainerId_id = trainer.TrainerId.id
        instance.coaching_courseid_id = course[0].id
        instance.save()
    item = Trainercourse.objects.filter(
        trainerId=trainer.TrainerId.id, coaching_courseid=course[0].id, time=int(s))
    uniqueid = item[0].course_randId
    course = Coursedetails()
    course.studentId_id = userid
    course.Trainercourse_id = uniqueid
    course.save()
    return True

def Assigning_tainer(item):
    userid = item[0].userid.id
    trainer = Trainer.objects.all()
    course = Courses.objects.filter(id=item[0].coursesId.id)
    trainerList = []
    for trainer in trainer:
        if trainer.teachingCourse.lower() in course[0].courseName.lower() and trainer.status == 'Free':
            if Trainercourse.objects.filter(trainerId=trainer.TrainerId.id).exists():
                check_trainer = Trainercourse.objects.filter(
                    trainerId=trainer.TrainerId.id)
                for check_trainer in check_trainer:
                    timing = makelist(trainer.timing_availability)
                    timing = list(map(int, timing))
                    if check_trainer.time in timing and check_trainer.countOfStudent < 5:
                        Trainercourse.objects.filter(course_randId=check_trainer.course_randId).update(
                            countOfStudent=check_trainer.countOfStudent+1)
                        return True
            else:
                result = assigning(trainer, course, userid)
                return result
        else:
            print("boom")

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/Course/<str:pk>/',
        'Courses View': '/Courses/<int:id>/',
        'AllCourses': '/Courses/All/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def getCourse(request, id):
    trainer = Trainercourse.objects.filter(trainerId=id, countOfStudent__gt=0)
    print(trainer)
    trainer_serializer = TrainercourseSerializer(trainer, many=True)
    course1 = []
    if trainer:
        for trainer in trainer:
            # if trainer.coaching_courseid.id not in course1.id:
            course = Courses.objects.filter(id=trainer.coaching_courseid.id)
            course1.append(course[0])
        serializer = TaskSerializer(course1, many=True)
    else:
        serializer = [{"Message": "your are new"}]
        return Response(serializer)
    list = [{'trainer': trainer_serializer.data, 'serializer': serializer.data}]
    return Response(list)

@api_view(['GET'])
def CoursePage(request, id, sectionname):
    sectionname = sectionname.strip()
    course1 = Course_page.objects.filter(courseId=id, sectionName=sectionname)
    print("mahireddy", course1, sectionname)
    cont = []
    serilizer = CoursecontentSerializer(course1[0], many=False)
    cont.append(serilizer.data)
    return Response(cont)
@api_view(['GET'])
def Student(request):
    serializer = [{"Message": "your are new"}]
    return Response(serializer)

@api_view(['GET'])
def getCourse_info(request, id):
    course1 = Course_info.objects.filter(coursesId=id)
    lists = makelist(course1[0].courseContent)
    section1 = []
    section2 = []
    section3 = []
    section4 = []
    section5 = []
    section6 = []
    section7 = []
    n = len(lists)
    count = 1
    for lists in lists:
        dic = {}
        if count < n/7:
            dic['sub'] = lists
            section1.append(dic)
            count += 1
        elif count < (n/7)*2:
            dic['sub'] = lists
            section2.append(dic)
            count += 1
        elif count < (n/7)*3:
            dic['sub'] = lists
            section3.append(dic)
            count += 1
        elif count < (n/7)*4:
            dic['sub'] = lists
            section4.append(dic)
            count += 1
        elif count < (n/7)*5:
            dic['sub'] = lists
            section5.append(dic)
            count += 1
        elif count < (n/7)*6:
            dic['sub'] = lists
            section6.append(dic)
            count += 1
        else:
            dic['sub'] = lists
            section7.append(dic)
    # print(section1)
    context = {
        'section1': section1, 'section2': section2, 'section3': section3, 'section4': section4, 'section5': section5, 'section6': section6, 'section7': section7
    }
    return Response(context)

@api_view(['POST'])
def Message(request, id):
    print("mahi")
    serializer = discussionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
