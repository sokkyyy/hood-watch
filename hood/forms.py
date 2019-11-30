from django import forms
from .models import User,Business
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password

class RegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'username', 'password']
        widgets = {
            'password':forms.PasswordInput()
        }

class LoginForm(forms.Form):
    
    email = forms.EmailField()
    password = forms.CharField(max_length=240,widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')        
        password = cleaned_data.get('password')
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            user = None
            msg = forms.ValidationError('Invalid Email')
            self.add_error('email', msg)
        if user:
            if not check_password(password,user.password):
                psw_msg = forms.ValidationError('Invalid Password')
                self.add_error('password',psw_msg)

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','description',]



