from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Courses, Service
from datetime import *

# Create your views here.

def about (request):
    return render (request, 'courses/about.html')

def contact (request):
    return render (request, 'courses/contact.html')

def index (request):
    port_content= Courses.objects.all()
    service_content= Service.objects.all()
    return render (request, 'courses/index.html', {'datae':port_content, 'service': service_content})
    


    

    
    


    
