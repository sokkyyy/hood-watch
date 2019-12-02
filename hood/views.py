from django.shortcuts import render,redirect
from .forms import RegForm,LoginForm,BusinessForm,PostForm,ChangePic
from .models import User,Neighborhood,Hood,Business,Post,PublicService
from django.contrib.auth import authenticate,login,logout
from django import forms
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@login_required(login_url='/login')
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
            send_welcome_email(full_name,email)

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

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return redirect(user_login)

@login_required(login_url='/login')
def user_profile(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except ObjectDoesNotExist:
        raise Http404()

    if not user == request.user:
        raise Http404('YOU CAN ONLY VIEW YOUR PROFILE!!!')


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

@login_required(login_url='/login')
def hood_services(request,hood):
    user = request.user
    user_hood = user.hood.name

    if not user_hood == hood:
        raise Http404('YOU DO NOT BELONG TO THIS HOOD')
        
    try:
        hood = Hood.objects.get(user=user)
    except ObjectDoesNotExist:
        raise Http404()

    posts = Post.objects.filter(hood=hood)
    occupants = Hood.objects.filter(name=hood)
    public_services_police = PublicService.objects.filter(hood=hood,category='police')
    public_services_health = PublicService.objects.filter(hood=hood,category='health')
    #Businesses
    carpentry = Business.objects.filter(hood=hood,category='carpentry')
    print(carpentry)
    electronics = Business.objects.filter(hood=hood,category='electronics')
    hardware = Business.objects.filter(hood=hood,category='hardware')
    liqour = Business.objects.filter(hood=hood,category='liqour')
    restaurant = Business.objects.filter(hood=hood,category='restaurant')
    salon = Business.objects.filter(hood=hood,category='salon')

    return render(request, 'services.html',{'hood':hood,
    'carpentry':carpentry,'posts':posts,'public_services_police':public_services_police,
    'public_services_health':public_services_health,'electronics':electronics,'hardware':hardware,
    'liqour':liqour,'restaurant':restaurant,'salon':salon,'occupants':occupants})


# Handles submissions for businesses
@login_required(login_url='/login')
def submit_business(request):
    user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            new_business = form.save(commit=False)
            new_business.category = request.POST['category']
            new_business.user = user
            new_business.hood = user.hood.name
            new_business.save()
    return redirect(user_profile,user.id)
# Handles submissions for posts
@login_required(login_url='/login')
def hood_posts(request,hood):
    hood = Hood.objects.get(name=hood)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = request.POST['category']
            post.user = request.user
            post.hood = hood.name
            post.save()
    return redirect(user_profile, request.user.id)
# Handle profile pic changes
@login_required(login_url='/login')
def change_profile_pic(request):
    user = request.user
    if request.method == 'POST':
        pic_form = ChangePic(request.POST,request.FILES)
        if pic_form.is_valid():
            new_pic = pic_form.cleaned_data['profile_pic']
            user.profile_pic = f'profile_pics/{new_pic}'
            user.save()
            try:
                pic_form.save()
            except IntegrityError:
                print(None)

    return redirect(user_profile,user.id)