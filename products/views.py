from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponseRedirect
from .forms import ProductsForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Products, Cart
from .forms import cartForm, ProductsForm
class cartProductTemplate:
    def __init__(self,id,name,photoPath,quantity,description):
        self.id=id
        self.name=name
        self.photoPath=photoPath
        self.quantinty=quantity
        self.description=description
    def increseQuantity(self, newQuantity):
        self.quantity+=newQuantity
    def decreseQuantity(self,newQuantity):
        self.quantinty-=newQuantity
def searchProducts(request,product):    
    categorias=["producto de limpieza", "producto a granel","cuidado personal"]
    if product=="0":
        #esto es para cuando proviene del buscador
        product=request.GET["searchProduct"] 
        products=Products.objects.filter(Name__contains=product)
        return render(request,"products.html",{'products': products, 'query':product,"len":len(products)})
    elif product in categorias:
        products=Products.objects.filter(Description__contains=product)
        return render(request,"products.html",{'products': products, 'query':product,"len":len(products)})
    else:
        #esto es cuando viene desde el carrito
        products=Products.objects.filter(id_products=product)
        return render(request, "product.html", {'product':products})



def cart(request, userId):
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
                product = get_object_or_404(Products, id=prod.id)
                newProduct = cartProductTemplate(id=prod.id, name=product.name, photoPath=product.photoPath, quantity=prod.quantity, description=product.description)
                products.append(newProduct)
                form = cartForm(initial={'quantity': prod.quantity})
                forms.append(form)
                total += product.price * prod.quantity
                
    return render(request, "carrito.html", {'products': products, 'total': total, 'forms': forms})


def productDetail(request, id):
    product = Products.objects.get(id=id)
    
def ProductsFormView(request):
    if request.method=="POST":
        form=ProductsForm(request.POST)
        if form.is_valid():
            product=form.save()
            messages.add_message(request, messages.SUCCESS, 'Registro exitoso')
            return HttpResponseRedirect(reverse_lazy('CatalogueFormView', args=[provider.id]))
    else:
        form=ProductsForm()
    return render(request, "ProductsForm.html", {'form':form})
