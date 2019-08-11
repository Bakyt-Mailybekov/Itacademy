from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'kssdasite/it-academy.html')



def about(request):
    alumni = Alumni.objects.all()
    return render(request, 'kssdasite/about.html', {'alumnis': alumni})

    
