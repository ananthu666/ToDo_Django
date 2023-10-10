from django.shortcuts import render ,HttpResponse
from home.models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime


current_time = datetime.now()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S.%f%z')
current_time = formatted_time
@login_required(login_url='login')

# Create your views here.
def home(request):
    context={'success':False}
    
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ct = request.POST['ct']
        
        ins = Task(user=request.user,taskTitle=title, taskDesc=desc,time=ct)
        ins.save()
        context={'success':True}
    
    return render(request, 'index.html',context) 
    # return HttpResponse("This is my home page")
def tasks(request):
    allTasks = Task.objects.filter(user=request.user)
    # find expired tasks allTasks
    expired_tasks = allTasks.filter(time__lt=current_time)
    pending_tasks = allTasks.filter(time__gte=current_time , complete=False)
    completed_tasks = allTasks.filter(complete=True)
    
    context={"pending_tasks":pending_tasks ,"expired_tasks":expired_tasks,"completed_tasks":completed_tasks}
    return render(request, 'tasks.html' ,context) 


def register(request):
    if request.method == "POST":
        first_name= request.POST['reg_name']
        username = request.POST['reg_username']
        
        password = request.POST['reg_pwd']
        
        unique_name = User.objects.filter(username=username)
        if unique_name:
            
            context={'success1':True,'success2':False}
            return render(request, 'register.html',context) 
            
        myuser = User.objects.create_user(first_name=first_name,username=username,password=password)
        myuser.set_password(password)
        myuser.save()
        
        
    
    context={'success1':False,'success2':True}
    return render(request, 'register.html',context) 
    

  # return HttpResponse("This is my home page")
def login_page(request):
    if request.method == "POST":
        username = request.POST['reg_username']
        password = request.POST['reg_pwd']
        # if User.objects.filter(username=username).exists():
        #     return render(request, 'login.html')     
        
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/home') 
        else:
            return redirect('/') 
    return render(request, 'login.html' )


def task_del(request,id):
    
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/tasks')

def task_upd(request,id):
    
    task = Task.objects.get(id=id)
    context={'task':task}
    return render(request, 'update_task.html', context=context)



def updated(request,id):
    
    task = Task.objects.get(id=id)
    task.taskTitle = request.POST['title']
    task.taskDesc = request.POST['desc']
    task.time = request.POST['ct']
    task.save()
    
    return redirect('/tasks')
    # return HttpResponse("This is my home page",id)


def pending(request,id):
    
    task = Task.objects.get(id=id)
    task.complete = True
    task.save()
    return redirect('/tasks')


def completed(request,id):
    
    task = Task.objects.get(id=id)
    task.complete = False
    task.save()
    return redirect('/tasks')

def logout_page(request):
    
    logout(request)
    return redirect('/')
    
