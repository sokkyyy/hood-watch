from django.shortcuts import render,redirect
from .forms import RegForm,LoginForm,BusinessForm,PostForm,ChangePic
from .models import User,Neighborhood,Hood,Business,Post
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
    pic_form =ChangePic()

    user_business = Business.objects.filter(user=user)
    user_posts = Post.objects.filter(user=user)

    if 'location' in request.POST and request.method =='POST':
        location = request.POST['location']
        hood.name = location
        hood.save()
        return redirect(user_profile, user.id)
    
    if 'full_name' in request.POST and request.method == 'POST':
        new_name = request.POST['full_name']
        user.full_name = new_name
        user.save()
        return redirect(user_profile,user.id)
         
    return render(request,'profile.html',{'user':user,
    'hood':hood,"business_form":business_form,'post_form':post_form,
    'user_business':user_business,'user_posts':user_posts,
    'pic_form':pic_form})

def hood_services(request,hood):
    hood = Hood.objects.get(name=hood)
    businesses = Business.objects.filter(hood=hood)
    posts = Post.objects.filter(hood=hood)
    return render(request, 'services.html',{'hood':hood,
    'businesses':businesses,'posts':posts})


# Handles submissions for businesses
def submit_business(request):
    user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            new_business = form.save(commit=False)
            new_business.category = request.POST['category']
            new_business.user = user
            new_business.hood = user.hood
            new_business.save()
    return redirect(user_profile,user.id)
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
# Handle profile pic changes
def change_profile_pic(request):
    user = request.user
    if request.method == 'POST':
        pic_form = ChangePic(request.POST,request.FILES)
        if pic_form.is_valid():
            new_pic = pic_form.cleaned_data['profile_pic']
            user.profile_pic = f'profile_pics/{new_pic}'
            user.save()
            pic_form.save()

    return redirect(user_profile,user.id)