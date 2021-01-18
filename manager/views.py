from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import *
# Create your views here.
def manager(request):
    return render(request,'chart.html')

def data(request):
    data={
        "sales" :100,
        "customer" :10,
    }
    return JsonResponse(data)

class chartdata(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        users = Account.objects.all().count()
        labels= ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        DataChart=[users,3,24,4,5,7,4]
        data={
        "labels":labels,
        "DataChart":DataChart
        }
        return Response(data)