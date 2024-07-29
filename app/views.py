from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate , login as loginUser , logout
from app.form import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login11')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')
        user_name = user.username if user else None  # Get the user's name
        return render(request, 'index.html', context={'form': form, 'todos': todos, 'user_name': user_name})
    
def login1(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'login.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )


 
def signup1(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login11')
        else:
            return render(request , 'signup.html' , context=context)
        
        
        
@login_required(login_url='login11')
def add(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else: 
            return render(request , 'index.html' , context={'form' : form})
        
        
def dele(request , id ):
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('home')

def cha_sta(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')


def signout(request):
    logout(request)
    return redirect('login11')