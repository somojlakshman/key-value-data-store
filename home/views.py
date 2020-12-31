from django.shortcuts import render
from django.urls import path
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import Taskerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    task_list=Task.objects.all()
    serializer=Taskerializer(task_list,many=True)
    return Response(serializer.data)