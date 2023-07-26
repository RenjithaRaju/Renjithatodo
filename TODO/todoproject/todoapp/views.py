from django.shortcuts import render,redirect
from . models import *
import easygui

# Create your views here.
def login(request):
    if request.method=='POST':
        if Todosign.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            user_log=Todosign.objects.filter(username=request.POST['username'],password=request.POST['password'])
            easygui.msgbox("welcome")
            return redirect(dashboard)
        else:
            context={'msg':"wrong credential"}
            return render(request,'login.html',context)
    return render(request,'login.html')

def sign(request):
    if request.method=="POST":
       
       if Todosign.objects.filter(email=request.POST['email']):
           easygui.msgbox("email already taken")
       else:
           usersign=Todosign()
           usersign.username=request.POST['username'] 
           usersign.password=request.POST['password']
           usersign.email=request.POST['email']
        
           usersign.save()
           easygui.msgbox("successS")
           return redirect(login)    
    return render(request,'sign.html')


def dashboard(request):
    mytask=usertask.objects.all()
    if request.method=="POST":
       mytask=usertask()
       if len(request.FILES) !=0:
        mytask.userimage=request.FILES['userimage']
       mytask.tasks=request.POST['tasks']
       mytask.percentages=request.POST['percentages']
       mytask.dates=request.POST['dates']
       mytask.save()
       easygui.msgbox("Task added")
       return redirect(dashboard)    
    return render(request,'dashboard.html',{'mytask':mytask})

def update(request,id):
    edit=usertask.objects.get(id=id)
    return render(request,'update.html',{'edit':edit})

def updateedit(request,id):
    
       tasks=request.POST['tasks']
       percentages=request.POST['percentages']
       dates=request.POST['dates']
     
       edit=usertask.objects.all().filter(id=id).update(tasks=tasks,percentages=percentages,dates=dates)
       easygui.msgbox("Updated")
       return redirect(dashboard)
def delete(request,id):
    deletes=usertask.objects.all().get(id=id)
    deletes.delete()
    return redirect(dashboard)
    
    
  