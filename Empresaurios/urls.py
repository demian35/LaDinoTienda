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
from clients.views import ProvidersFormView,home, ConvenienceStoreFormView
from Login.views import logIn, signIn, SignOutView, contacto, suscripcionView
from products.views import productDetail,cart, searchProducts, ProductsFormView,ticket,cosultOrders
urlpatterns = [
    path("admin/", admin.site.urls),
    path('cerrar-sesion', SignOutView.as_view(next_page='home'), name='cerrar sesion'), 
    re_path("iniciar-sesion", signIn, name='Dino iniciar sesion'),
    path('registro/', logIn.as_view(), name='Dino registro'),
    path("registro-vendedor", ProvidersFormView,name="Dino Registro vendedor"),
    path("busqueda-producto/<product>",searchProducts,name="Dino busqueda"),
    path("detalle-producto/<id>", productDetail,name="Dino producto especifico"),
    path("registro-producto", ProductsFormView,name="Dino registro de producto"),
    path("carrito/<userId>", cart,name="Dino carrito"),
    path("consultar-pedidos",cosultOrders, name="Dino consultar pedidos" ),
    path("ticket-de-compra/<userId>",ticket,name ="Dino ticket compra"),
    path("registro-comprador", ConvenienceStoreFormView, name="Dino registro de comprador"),
    path("suscripcion/", suscripcionView, name="Suscripcion"),
    path("",home,name='home' ),
]
