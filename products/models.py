from django.db import models

from clients.models import Providers, ConvenienceStore

class Products(models.Model):
    Name=models.CharField(max_length=20, default="Name", verbose_name="Nombre")
    Price=models.FloatField(default=0, verbose_name="Precio por mayoreo")
    Marca=models.CharField(max_length=20,default="Marca",verbose_name="Marca")
    Description=models.CharField(max_length=50,default="clasificación",verbose_name="Clasificación")
    #esta es la cantidad disponible en tienda
    quantity=models.FloatField(default=0,verbose_name="Cantidad Disponible")
    photoPath=models.CharField(max_length=50, default="", verbose_name="Ruta de foto")
    #clave foranea
    provider=models.ForeignKey(Providers,on_delete=models.CASCADE,verbose_name="Proveedor")
    
    class Meta:
        verbose_name_plural="Catálogo"
    def __str__(self) -> str:
        return "El proveedor es: %s, %s"%( self.provider,self.Name)
class Cart(models.Model): 
    id_convenience_store=models.ForeignKey(ConvenienceStore,on_delete=models.CASCADE,verbose_name="Id de comprador")
    bought=models.BooleanField(default=False,verbose_name="Comprado")
    quantity=models.IntegerField(default=1, verbose_name="Cantidad")
    id_provider=models.ForeignKey(Providers, on_delete=models.CASCADE, verbose_name="id de Vendedor")
    id_producto=models.ForeignKey(Products,on_delete=models.CASCADE,verbose_name="Id de producto")

    

