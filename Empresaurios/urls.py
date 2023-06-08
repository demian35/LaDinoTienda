"""Empresaurios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from clients.views import providerFormView, ConvenienceStoreFormView,home,cosultOrders
from Login.views import logIn, signIn, SignOutView, contacto, buyerFormView, registroVendedor
from products.views import productDetail,cart, searchProducts, ProductsFormView,ticket
urlpatterns = [
    path("admin/", admin.site.urls),
    path('cerrar-sesion/', SignOutView.as_view(), name='cerrar sesion'), 
    re_path("registro/", signIn, name='Dino registro'),
    path('iniciar-sesion/', logIn.as_view(), name='Dino iniciar sesion'),
    path('registro-comprador/', buyerFormView, name='DinoDino Registro Comprador'),
    path("registro-vendedor/", providerFormView,name="Dino Registro vendedor"),
    path("busqueda-producto/",searchProducts,name="Dino busqueda"),
    path("detalle-producto/<id>", productDetail,name="Dino producto especifico"),
    path("registro-producto/", ProductsFormView,name="Dino registro de producto"),
    path("carrito/<userId>", cart,name="Dino carrito"),
    path("consultar-pedidos",cosultOrders, Name="Dino consultar pedidos" ),
    path("ticket-de-compra",ticket,name ="Dino ticket compra"),
    # path("conveniencestore/", ConvenienceStoreFormView, name="Registro de comprador"),
    path("",home,name='home' ),
]
