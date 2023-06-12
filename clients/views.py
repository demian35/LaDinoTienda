from django.shortcuts import render,redirect
from django.http import  HttpResponseRedirect
from .forms import ConvenienceStoreForm , ProvidersForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Providers, ConvenienceStore

def home(request):
    if request.user.is_authenticated:
        user_id=request.user.id
        user=request.user.username
        provider=Providers.objects.filter(user_id=user_id)
        buyer=ConvenienceStore.objects.filter(user_id=user_id)
        if provider:
            return render(request,"homeVendedor.html", {"username":user})
        elif buyer:
            return render(request,"homeComprador.html",{"username":user})
        else:
            return render(request,"homeComprador.html",{"username":user})
    else:
        return redirect('Dino registro')
def ProvidersFormView(request):
    if request.user.is_authenticated:
        user=request.user.username
        if request.method=="POST":
            form=ProvidersForm(request.POST)
            if form.is_valid():
                provider=form.save()
                messages.add_message(request, messages.SUCCESS, 'Registro exitoso')
                return HttpResponseRedirect(reverse_lazy('home', args=[]))
        else:
            form=ProvidersForm()
        return render(request, "registroVendedor.html", {'form':form,"username":user})
    else:
        return redirect('Dino registro')
def ConvenienceStoreFormView(request):
    if request.user.is_authenticated:
        user=request.user.username
        if request.method=="POST":
            form=ConvenienceStoreForm(request.POST)
            if form.is_valid():
                form.save()        
                messages.add_message(request, messages.SUCCESS, 'Registro exitoso')
                return HttpResponseRedirect(reverse_lazy('ConvenienceStoreHome', args=[]))
        else:
            form=ConvenienceStoreForm()
        return render(request, "ConvenienceStoreRegister.html",{'form': form,"title":"Registro de tienda de conveniencia","username":user })
    else:
        return redirect('Dino registro')
    
