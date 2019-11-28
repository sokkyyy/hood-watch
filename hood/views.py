from django.shortcuts import render
from .forms import RegForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    form = RegForm()

    return render(request,'auth/registration.html',
    {'form':form})