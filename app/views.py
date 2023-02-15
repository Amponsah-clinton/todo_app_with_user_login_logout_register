from django.shortcuts import render, redirect
from .models import myapp
from .forms import TodoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm
# Create your views here.

def index(request):
    form = TodoForm()
    obj = myapp.objects.all()
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TodoForm()

    return render(request,'index.html',{'form':form, 'obj':obj})

def Update(request, id):
    obj = myapp.objects.get(id=id)
    form = TodoForm()
    if request.method =='POST':
        form = TodoForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            form = TodoForm()
            return redirect('/index')

    return render(request,'update.html',{'form':form, 'obj':obj})

def Delete(request, id):
    obj = myapp.objects.get(id=id)
    obj.delete()
    return redirect('/index')


def logout_user(request):
    logout(request)
    return redirect('')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password, email=email)
            login(request,user)
            messages.success(request, ("Registration Successful!"))
            return redirect('/')
    else:
        form = RegisterUserForm()
        
    return render(request,'register.html',{'form':form})


def login_user(request):
    if request.method == "POST":
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)
             return redirect('index/')
         else:
             messages.success(request, ("There Was An Error Logging In, Try Again..."))	
             return redirect('/')	
    else:
		    return render(request, 'login.html', {})











