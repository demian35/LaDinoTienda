from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .forms import CatalogueForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Products, Cart

def busquedaArticulos(request,product):
    categorias=["productos-de-limpieza", "productos-a-granel","cuidado-personal"]
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
def Cart(request,userId):
    cart=Cart.objets.filter(id_convenience_store=userId,bought=False)
    products=[]
    total=0
    subtotal=total
    for prod in cart:
        product=Products.objects.filter(prod.id_producto)
        products.append(product)
        total+=product.price*prod.quantity
    return render (request,"carrito.html",{'products':products, 'total':total,'subtotal':subtotal})

# def CatalogueFormView(request):
#     if request.method=="POST":
#         form=ProductsForm(request.POST)
#         if form.is_valid():
#             product=form.save()
#             messages.add_message(request, messages.SUCCESS, 'Registro exitoso')
#             return HttpResponseRedirect(reverse_lazy('CatalogueFormView', args=[provider.id]))
#     else:
#         form=ProductsForm()
#     return render(request, "CatalogueRegister.html", {'form':form})
