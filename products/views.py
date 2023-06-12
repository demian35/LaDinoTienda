from django.shortcuts import render, get_object_or_404, redirect
from django.http import  HttpResponseRedirect
from .forms import ProductsForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Products, Cart
from .forms import cartForm, ProductsForm
class cartProductTemplate:
    def __init__(self,id,name,photoPath,quantity,description,form):
        self.id=id
        self.name=name
        self.photoPath=photoPath
        self.quantinty=quantity
        self.description=description
        self.form=form
    def increseQuantity(self, newQuantity):
        self.quantity+=newQuantity
    def decreseQuantity(self,newQuantity):
        self.quantinty-=newQuantity
def searchProducts(request,product):   
    if request.user.is_authenticated:
        user=request.user.username
        categorias=["producto de limpieza", "producto a granel","cuidado personal"]
        if product=="0":
            #esto es para cuando proviene del buscador
            product=request.GET["searchProduct"] 

            if product in categorias:
                products=Products.objects.filter(description__contains=product)
                return render(request,"busqueda.html",{'products': products, 'query':product,"len":len(products),"username":user})
            else:
                products=Products.objects.filter(name__contains=product)
                return render(request,"busqueda.html",{'products': products, 'query':product,"len":len(products),"username":user})
        
        elif product in categorias:
            
            products=Products.objects.filter(description__contains=product)
            return render(request,"busqueda.html",{'products': products, 'query':product,"len":len(products),"username":user})
        else:
            #esto es cuando viene desde el carrito
            product=Products.objects.get(id=product)
            products=[product,]
            return render(request, "busqueda.html", {'products':products,"username":user,"len":1,"query":products[0].name})
    else:
        return redirect('Dino registro')



def cart(request, userId):
    if request.user.is_authenticated:
        user=request.user.username
        if request.method == 'POST':
            # Lógica para manejar el formulario POST si es necesario
            pass
        else:
            cart = Cart.objects.filter(id_convenience_store=userId, bought=False)
            products = []
            forms = []
            total = 0
            
            for prod in cart:
                if prod.quantity == 0:
                    # Eliminar el objeto del carrito si la cantidad es cero
                    prod.delete()
                else:
                    product = get_object_or_404(Products, id=prod.id_producto_id)
                    newform = cartForm(initial={'quantity': prod.quantity})
                    newProduct = cartProductTemplate(id=product.id, name=product.name, photoPath=product.photoPath, quantity=prod.quantity, description=product.description, form=newform)
                    products.append(newProduct)
                    total += product.price * prod.quantity
                    
        return render(request, "carrito.html", {'products': products, 'total': total, 'forms': forms,"username":user})
    else:
        return redirect('Dino registro')


def productDetail(request, id):
    if request.user.is_authenticated:   
        user=request.user.username 
        user_id=request.user.id
        product = Products.objects.get(id=id)
        if request.method=="POST":
            form=cartForm(request.POST)
            
            if form.is_valid():
                product=form.save(False)
                product.bought=False
                product.id_convenience_store_id=user_id
                product.id_producto_id=id
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Registro exitoso')
                return HttpResponseRedirect(reverse_lazy('Dino carrito', args=[user_id]))
        else:   
            form=cartForm()
        return render(request, "detalleProducto.html",{"product":product, "form":form,"username":user})    
    else:
        return redirect('Dino registro')
def ProductsFormView(request):
    if request.user.is_authenticated:  
        user=request.user.username  
        if request.method=="POST":
            form=ProductsForm(request.POST)
            if form.is_valid():
                product=form.save()

                messages.add_message(request, messages.SUCCESS, 'Registro exitoso')
                return HttpResponseRedirect(reverse_lazy('home', args=[]))
        else:
            form=ProductsForm()
        return render(request, "ProductsForm.html", {'form':form, "username":user})
    else:
        return redirect('Dino registro')
def cosultOrders(request):
    if request.user.is_authenticated:
        user=request.user.username
        return render(request, "consultarPedidos.html",{"username":user})
    else:
        return redirect('Dino registro')
def ticket (request):
    if request.user.is_authenticated:
        user=request.user.username
        return render(request, "ticketCompra.html",{"username":user})
    else:
        return redirect('Dino registro')
    
