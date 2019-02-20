from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm


class Register(View):
    def get(self,request):
        return render(request,'register.html',{})

class LoginView(View):
    def get(self,request):
        return render(request, 'login.html', {})

    def post(self,request):
        un = request.POST.get('username', '')
        pw = request.POST.get('password', '')
        loginem = LoginForm()
        if loginem.is_valid():
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login.html', {})
        else:
            return render(request, 'login.html', {})

class CustomBackend(ModelBackend):
    def authenticate(self,username=None,password=None):
        if username==None or password==None:
            return None

        user = UserProfile.objects.get(Q(username=username)|Q(email=username))
        if user is not None and user.check_password(password):
            return user
        else:
            return None



def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('username','')
        pw = request.POST.get('password', '')
        user=authenticate(username=un,password=pw)
        if user is not None:
            login(request,user)
            return render(request,'index.html',{})
        else:
            return render(request, 'login.html', {})
    elif request.method == 'GET':
        return render(request,'login.html',{})
