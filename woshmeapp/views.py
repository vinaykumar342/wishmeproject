from django.shortcuts import render
import datetime
# Create your views here.

def wish(request):
    time=datetime.datetime.now()
    return render(request,'wish.html',{'time':time})
