from django.shortcuts import render,redirect
from .forms import RegForm
from .models import User
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

            new_user = User.objects.create_user(username,email,password)
            new_user.full_name = full_name
            new_user.save()

            return redirect(home)
    else:
        form = RegForm()
    return render(request,'auth/registration.html',
    {'form':form})