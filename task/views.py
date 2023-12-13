from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm,AccountAuthenticationForm,TaskForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from django.contrib import messages
import json 


# Create your views here.

@login_required(login_url='login')
def home(request):
    tasks = App.objects.all()
    return render(request,'task/home.html',{'tasks':tasks})     
    
@staff_member_required
def staff_home(request):
    tasks = App.objects.all()
    return render(request,'task/adminhome.html',{'tasks':tasks})



@staff_member_required
def add_App(request):
    form = AppForm()
    if request.method == 'POST':
        form = AppForm(request.POST, request._files)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request,"error occured while saving file")
            return redirect('create')
    else:
        return render(request,'task/snippets/create.html',{'form':form})
  
@login_required(login_url='login')
def single_view(request,**kwargs):
    user = request.user
    if request.method == 'POST':
        user = request.user
        print(request.POST)
        print(request.FILES)
        id = kwargs.get('id')
        app = App.objects.get(pk=id)
        new_task = Task.objects.create(app=app,img=request.FILES.get('img'),created=user,completed=False)
        new_task.save()
        try:
            print(new_task)
            return redirect('home')
        except:
            print('something went wrong')
    id = kwargs.get('id')
    print(id)
    app = App.objects.get(pk=id)
    return render(request,'task/snippets/single_task.html',{'task':app})
        

def register_view(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    
    return render(request, 'task/account/register.html', {'form': form})


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = Account.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')
    return render(request, 'task/account/login.html')

@login_required(login_url='login')
def view_points(request):
    user = request.user
    tasks= Task.objects.filter(created=user)
    points = get_total_point(request.user)
    return render(request,'task/snippets/tasks.html',{'tasks':tasks,'points':points})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def view_profile(request,**kwargs):

    id = kwargs.get('id')
    points = get_total_point(request.user)
    user = Account.objects.get(pk=id)

    return render(request,'task/snippets/profile.html',{'user':user,'points':points})

@staff_member_required
def view_app_task(request):
    tasks = Task.objects.all()
    return render(request,'task/snippets/alltasks.html',{'tasks':tasks})

@staff_member_required
def single_task_view(request,**kwargs):

    if request.method == 'POST':
        data = json.loads(request.body)
        taskId = data['taskId']
        action = data['action']
        id = taskId
        task = Task.objects.get(pk=id)
        if action == 'approve':
            task.completed = True
            task.save()
        elif action == 'disapprove':
            task.completed = False
            task.save()
        
    
    id = kwargs.get('id')
    print(id)
    task = Task.objects.get(pk=id)
    print('hello')
    return render(request,'task/snippets/single.tak.html',{'task':task})
    