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
from clients.views import ProvidersFormView, ConvenienceStoreFormView,home
from Login.views import registro, identificate, SignOutView, contacto, registroComprador
from products.views import productDetail,cart, searchProducts
urlpatterns = [
    path("admin/", admin.site.urls),
    path('registro/', registro.as_view(), name='registro'),
    path('signout/', SignOutView.as_view(), name='signout'), 
    re_path("identificate/", identificate, name='identificate'),
    
    path("providers/", ProvidersFormView,name="Registro de vendedor"),
    path("carrito/<userId>", cart,name="Carrito"),
    path("detalle-producto/<id>", productDetail,name="Detalle producto"),
    path("nuevo-producto", productDetail,name="Detalle producto"),
    path("conveniencestore/", ConvenienceStoreFormView, name="Registro de comprador"),
    path("",home,name='home' ),
    path('registroComprador/', registroComprador, name='Registro Comprador'),
]
