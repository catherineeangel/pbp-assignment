import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import CreateTaskForm

# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    currentUser = request.user
    data_todolist = Task.objects.filter(user=currentUser)

    context = {
        "todolist": data_todolist,
        "username": currentUser.username,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, 'todolist.html', context)

def register(request):
    form = UserCreationForm(request.POST) # ini apa bro
    if request.method == "POST":

        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')

    context = {'form': form}
    return render(request, 'register.html', context)
   

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = CreateTaskForm()

    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            # form.user=
            new_task.user = request.user
            new_task.save() 
            messages.success(request, 'Task telah berhasil dibuat!')
            return redirect('todolist:show_todolist')
    
    context = {'form':form}
    return render(request, 'create-task.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response