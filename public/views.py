from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models

# Create your views here.
def signup (request):

    if request.method=="POST":
        Name=request.POST.get('name')
        Usn=request.POST.get('usn')
        Password=request.POST.get('password')
        data = models.Signup(name=Name,usn=Usn,password=Password)
        data.save()
        # print(Name,Usn,Password)
        return redirect('login')
     
    return render(request,"signup.html")
def login (request):
    if request.method=="POST":
        
        Usn=request.POST.get('usn')
        Password=request.POST.get('password')
        data = models.Login(usn=Usn,password=Password)
        data.save()
        return redirect('Index')
    return render(request,"login.html")