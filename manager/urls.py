from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from manager import views
from manager.views import chartdata
urlpatterns = [
    path('manager',views.manager,name='manager'),
    path('manager/api',views.data,name='data'),
    path('manager/api1',chartdata.as_view())
]