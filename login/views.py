from django.http.response import HttpResponse
from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,'login.html')
def adduser(request):
    if request.method=='POST':
        username=request.post['uname']
        email=request.post['mail']
        password1=request.post['passw']
        password2=request.post['rpassw']
        number=request.post['num']
        user=User.objects.create_user(uname=username,mail=email,passw=password1,num=number)
        user.save()
        print("craeted")
        
    else:
        return render(request,'register.html')





    

