from django.shortcuts import render,redirect
from django.http import  HttpResponseRedirect
from .forms import ConvenienceStoreForm , ProvidersForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Providers, ConvenienceStore
from products.models import Cart, Products
from Login.models import Perfil

def home(request):
    if request.user.is_authenticated:
        user_id=request.user.id
        user=request.user.username
        provider=Providers.objects.filter(user_id=user_id)
        buyer=ConvenienceStore.objects.filter(user_id=user_id)
        if provider:
            # try:
                orders = Cart.objects.filter(bought=True)
                clients = []
                bills = []
                for order in orders:
                    client = ConvenienceStore.objects.get(id=order.id_convenience_store_id)
                    product = Products.objects.get(id=order.id_producto_id)
                    
                    if client in clients:
                        i = clients.index(client)
                        bills[i] += (order.quantity * product.price)
                    else:
                        clients.append(client)
                        bills.append(order.quantity * product.price)
                if len(clients)==0:
                    return render(request,"homeVendedor.html", {"username":user,"profile":True, "suscribe": provider[0].is_suscribed})
                if len(clients)==1:
                    print(clients)
                    return render(request,"homeVendedor.html", {"username":user,"profile":True, "suscribe": provider[0].is_suscribed,"bills": bills, "clients": clients})
                else:
                    return render(request, "homeVendedor.html", {"username": user, "profile": True, "suscribe": provider[0].is_suscribed,"bills": bills, "clients": clients})

        elif buyer:
    
            return render(request,"homeComprador.html",{"username":user })
        else:
            return render(request,"homeComprador.html",{"username":user})
    else:
        return redirect('Dino iniciar sesion')
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
        return redirect('Dino iniciar sesion')
def ConvenienceStoreFormView(request):
    if request.user.is_authenticated:
        user=request.user.username
        userId=request.user.id
        if request.method=="POST":
            form=ConvenienceStoreForm(request.POST)
            if form.is_valid():
                convenience_store = form.save(commit=False)  # Guarda el formulario sin guardar en la base de datos
                convenience_store.user_id_id = userId  # Asigna el ID del usuario a user_id_id
                convenience_store.save()       
                messages.add_message(request, messages.SUCCESS, 'Registro exitoso')
                return HttpResponseRedirect(reverse_lazy('home', args=[]))
        else:
            form=ConvenienceStoreForm()
        return render(request, "ConvenienceStoreRegister.html",{'form': form,"title":"Registro de tienda de conveniencia","username":user })
    else:
        return redirect('Dino iniciar sesion')
    
