from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
#, TemplateView
from .models import Perfil
from .forms import SignUpForm
from django.contrib.auth.views import LogoutView
from .forms import LoginForm
from django.urls import reverse_lazy


def signIn(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # Autenticación exitosa, redirigir a la página deseada
                return redirect('home')
    else:
        form = LoginForm(request)
    return render(request, 'iniciar_sesion.html', {'form': form})
class SignOutView(LogoutView):
    pass

class logIn(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario,password=password)
        login(self.request, usuario)
        return redirect('Dino registro de comprador')
    def userRol(request):
        if request.method=='POST':
            if 'vendedor' in request.POST:
                return render(request, "registrovendedor.html",{})
        
            elif 'comprador' in request.POST:
                return render(request, "registrocomprador.html",{})

def contacto (request):
    return render(request,"contacto.html",{})

def providerFormView(request):
    username = request.user.username
    return render(request, "registroVendedor.html", {'username': username})

def suscripcionView(request):
    username = request.user.username
    return render(request, "suscripcion.html", {'username': username})
