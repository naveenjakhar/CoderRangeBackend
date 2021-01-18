from django.urls import path
from trainer import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('jvt',views.apiOverview,name='apiOverview'),
    path('login',csrf_exempt(views.LoginView.as_view()),name='LoginView'),
    path('Courses/<int:id>',views.getCourse,name='getCourse'),
    path('student',views.Student,name='student'),
    path('Courses_info/<int:id>',views.getCourse_info,name='getallCourse'),
    path('Course/<int:id>/<str:sectionname>',views.CoursePage,name='CoursePage'),
    path('message/<int:id>',views.Message,name='Message'),
]