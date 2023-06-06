from django.db import models

from clients.models import Providers, ConvenienceStore

class Products(models.Model):
    name=models.CharField(max_length=20, default="Name", verbose_name="Nombre")
    price=models.FloatField(default=0, verbose_name="Precio por mayoreo")
    brand=models.CharField(max_length=20,default="Marca",verbose_name="Marca")
    description=models.CharField(max_length=50,default="descripción",verbose_name="Descripción")
    #esta es la cantidad disponible en tienda
    quantity=models.FloatField(default=0,verbose_name="Cantidad Disponible")
    photoPath = models.ImageField(upload_to='static/', null=True,blank=True)
    #clave foranea
    provider=models.ForeignKey(Providers,on_delete=models.CASCADE,verbose_name="Proveedor")
    
    class Meta:
        verbose_name_plural="Catálogo"
    def __str__(self) -> str:
        return "El proveedor es: %s, %s"%( self.provider,self.Name)
class Cart(models.Model): 
    bought=models.BooleanField(default=False,verbose_name="Comprado")
    quantity=models.IntegerField(default=1, verbose_name="Cantidad")
    id_convenience_store=models.ForeignKey(ConvenienceStore,on_delete=models.CASCADE,verbose_name="Id de comprador")
    id_producto=models.ForeignKey(Products,on_delete=models.CASCADE,verbose_name="Id de producto")


