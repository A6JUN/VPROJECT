from django.shortcuts import render,redirect
from frontend.models import prddb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

def main(req):
    return render(req,'mainpage.html')

def homepage(req):
    return render(req,'home.html')

def prdtdatasave(req):
    if req.method=="POST":
        pn=req.POST.get('pname')
        ds=req.POST.get('description')
        sz=req.POST.get('size')
        cl=req.POST.get('color')
        st=req.POST.get('status')
        obj=prddb(pname=pn,description=ds,size=sz,color=cl,status=st)
        obj.save()
        return redirect(homepage)

def prdtdisplay(req):
    data=prddb.objects.all()
    return render(req,'display.html',{'data':data})

def prdtdelete(req,dataid):
    data=prddb.objects.filter(id=dataid)
    data.delete()
    return redirect(prdtdisplay)

def prdtupdate(req,dataid):
  if req.method=="POST":
      pn = req.POST.get('pname')
      ds = req.POST.get('description')
      sz = req.POST.get('size')
      cl = req.POST.get('color')
      st = req.POST.get('status')
      prddb.objects.filter(id=dataid).update(pname=pn,description=ds,size=sz,color=cl,status=st)
  return redirect(prdtdisplay)

def prdtedit(req,dataid):
    data=prddb.objects.get(id=dataid)
    return render(req,"prdtedit.html",{'data':data})
