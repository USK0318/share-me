from django.shortcuts import render
from .forms import gameform
from django.contrib import messages
from .models import gamedata
import random

# Create your views here.
def display0(request):
    return render(request,'main.html')


def delet(a):
    xx=gamedata.objects.get(id=a)
    xx.delete()

def display2(request):
    if request.method=="POST":
        a=request.POST['ip']
        try:
            data=gamedata.objects.get(id=a)
            delet(a)
        except Exception:
            messages.error(request,'Invalied Code')
            return render(request,'second.html',{'nom':1})
        return render(request,'second.html',{'a':data,'nom':2})
    return render(request,'second.html',{'nom':1})
    
def display(request):
    if request.method=="POST":
        while True:
            a=random.randint(1000,1010)
            try:
                x=gamedata.objects.get(id=a)
            except Exception:
                b=a
                break
        a=request.FILES['imp']
        cod=b
        gamedata.objects.create(id=b,data=a)
        return render(request,'first.html',{'nom':1,'c':cod})
    return render(request,'first.html',{'nom':2})