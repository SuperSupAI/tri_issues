from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = RegisterForm()
    
    context = {'form': form}
    return render(request, 'users/register.html', context)

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username__iexact=username).exists():
        return HttpResponse("<div style='color: red;'> This username already exists</div>" )
    else:
        return HttpResponse("<div style='color: green;'>This username is available</div>")