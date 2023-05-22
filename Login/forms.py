from django import forms
from django.contrib.auth.forms import UserCreationForm
#, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  
#from django.forms.fields import EmailField  
#from django.forms.forms import Form  

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class':'py-2 pr-5 mr-1 '})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class':'py-2 pr-5 mr-1 '})
    )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class':'rounded-pill py-2 pr-5 mr-1'}))

    username = forms.CharField(   
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class':'rounded-pill py-2 pr-5 mr-1 '})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class':'rounded-pill py-2 pr-5 mr-1 '})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'class':'rounded-pill py-2 pr-5 mr-1 '})
    )
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
    
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("El usuario ya existe")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("El e-mail introdiucido ya existe")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Las contraseñas no coinciden")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user  