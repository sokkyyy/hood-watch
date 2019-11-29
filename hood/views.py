from django.shortcuts import render,redirect
from .forms import RegForm,LoginForm
from .models import User,Neighborhood,Hood
from django.contrib.auth import authenticate,login,logout
from django import forms
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            password = form.cleaned_data['password']
            location = request.POST['location']


            

            new_user = User.objects.create_user(username,email,password)
            new_user.full_name = full_name
            new_user.save()

            #Neighbourhood Instatiations
            neighborhood = Neighborhood()
            neighborhood.save()
            #Hood Instatiations
            new_hood = Hood(neighborhood=neighborhood,name=location,user=new_user)
            new_hood.save()



            return redirect(user_login)
    else:
        form = RegForm()

    return render(request,'auth/registration.html',
    {'form':form})


def user_login(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            user = User.objects.get(email=email)

            login(request,user)
            return redirect(home)                
    else:
        form = LoginForm()

    return render(request, 'auth/login.html',
    {"form":form})

def user_profile(request, user_id):
    return render(request,'profile.html')