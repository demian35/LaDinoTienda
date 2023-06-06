from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .forms import ProductsForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Products, Cart
from .forms import cartForm, Products
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

def cart(request,userId):
    
    if request.method =='POST':
        pass
    else:
        cart = Cart.objects.filter(id_convenience_store=userId, bought=False)
        products=[]
        forms=[]
        total=0
        
        for prod in cart:
            if prod.quantity==0:
                #solo para evitar bugs
                obj = Cart.objects.get(id=prod.id)      
                obj.delete()
            
            product=Products.objects.get(id=prod.id)
            newProduct=cartProductTemplate(id=prod.id,name=product.name,photoPath=product.photoPath,quantity=prod.quantity)
            products.append(newProduct)
            form=cartForm(initial={'quantity': newProduct.quantinty})
            forms.append(form)
            total+=product.price*prod.quantity
    return render (request,"carrito.html",{'cart':cart,'products':products, 'total':total})

def productDetail(request, id):
    product=Products.filter(id=id)
    return render(request, "detalleProducto.html",{"product":product})
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
