from django.shortcuts import render
from candidates import models

# Cr eate your views here.
def cse(request): 
    csepresidentdata=models.Csepresident.objects.all()
    csevicepresidentdata=models.Csevicepresident.objects.all()
    csesecretorydata=models.Csesecretory.objects.all()
    
    data={
        'Csepresidentdata' : csepresidentdata,
        'Csevicepresidentdata' : csevicepresidentdata,
        'Csesecretorydata' : csesecretorydata
    }
    return render(request,"cs.html",data)

def ise(request):
    

    return render(request,"is.html")

def ece(request):

    return render(request,"ec.html")

def civil(request):

    return render(request,"civil.html")
