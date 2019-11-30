from django.shortcuts import render,redirect
from .forms import RegForm,LoginForm,BusinessForm,PostForm
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
    user = User.objects.get(pk=user_id)
    hood = Hood.get_user_hood(user)

    business_form = BusinessForm()
    post_form = PostForm()

    if 'location' in request.POST and request.method =='POST':
        location = request.POST['location']
        hood.name = location
        hood.save()
        return redirect(user_profile, user.id)
     
    return render(request,'profile.html',{'user':user,
    'hood':hood,"business_form":business_form,'post_form':post_form})

# Handles submissions for businesses
def hood_services(request,hood):
    hood = Hood.objects.get(name=hood)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.category = request.POST['category']
            business.hood = hood
            business.user = request.user
            business.save()
 
    return redirect(user_profile, request.user.id)
# Handles submissions for posts
def hood_posts(request,hood):
    hood = Hood.objects.get(name=hood)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = request.POST['category']
            post.user = request.user
            post.hood = hood
            post.save()
    return redirect(user_profile, request.user.id)
