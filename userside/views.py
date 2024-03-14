from django.shortcuts import render
from frontend.models import prddb


def Buypage(req):
    data1=prddb.objects.all()
    return render(req,'buypage.html',{'data1':data1})

def Oder(req, proid):
    data2=prddb.objects.get(id=proid)
    return render(req,'orderpage.html',{'data2':data2})

# Create your views here.
