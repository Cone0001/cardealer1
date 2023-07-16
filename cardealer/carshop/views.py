from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def initialroom(request):
    return render(request,'carshop/initial_room.html')

def selectedroom(request):
    return render(request,'carshop/selected_room.html')