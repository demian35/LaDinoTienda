from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
#, TemplateView
from .models import Perfil
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView

class identificate(LoginView):
    template_name = 'iniciar_sesion.html'

class SignOutView(LogoutView):
    pass
class registro(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En esta parte, si el form es valido lo guardamos y usamos authenticate e iniciamos sesión
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario,password=password)
        login(self.request, usuario)
        return redirect('/')
        
def home(request):
    return render(request,"home.html", {})
def contacto (request):
    return render(request,"contacto.html",{})
