from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    a=About.objects.all()
    e=Experience.objects.all()
    ed=Education.objects.all()
    i=Interest.objects.all()
    s=Skill.objects.all()
    p=Project.objects.all()
    if request.method =="POST":
        n=request.POST["name"]
        e=request.POST["email"]
        s=request.POST["subject"]
        m=request.POST["message"]
        
        data=Contact(name=n,email=e,subject=s,message=m)
        data.save()
        
    return render(request,'index.html',{'about':a,'exp':e,'edu':ed,'interest':i,'skill':s,'project':p })