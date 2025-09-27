from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # (Optional) เข้าสู่ระบบผู้ใช้ทันทีหลังลงทะเบียน
            login(request, user)
            return redirect('home')  # เปลี่ยน 'home' เป็น URL ที่ต้องการ
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username__iexact=username).exists():
        return HttpResponse("<div style='color: red;'> This username already exists</div>" )
    else:
        return HttpResponse("<div style='color: green;'>This username is available</div>")