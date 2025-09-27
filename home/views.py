from django.shortcuts import render
from datetime import datetime

def home(request):

    today = datetime.now()
    context = {'today': today,}

    return render(request,'home/home.html',context)