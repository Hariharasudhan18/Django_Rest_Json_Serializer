from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView

from rest_framework import viewsets
from .serializer import EmployeeSerializer
from .models import EmployeeModel

#Create your views here.
def homePageView(request):
    return HttpResponse("Welcome to Home page")
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all().order_by('name')
    serializer_class = EmployeeSerializer

# def employee(request):
#     return JsonResponse({'Name': 'Name', 'Job': 'Job'});

# class homePageView(ListView):
#     model = EmployeeModel
#     # template_name = 'home.html'