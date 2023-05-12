from django.db import models
from datetime import date
from django.core.validators import MinValueValidator

from Login.models import Perfil
class Providers(models.Model):
    # proveedores, vendedores, tiendas de mayoreo 
    name=models.CharField(default="",max_length=30,verbose_name="Nombre")
    last_name=models.CharField(max_length=50,verbose_name="Apellidos")
    telephone=models.CharField(default="",max_length=12,verbose_name="Teléfono")
    logo=models.CharField(default="",max_length=100, verbose_name="Logo")
    enterprise_name=models.CharField(default="",max_length=100, verbose_name="Nombre de la empresa")
    descripcion=models.CharField(max_length=200,verbose_name="Descripción")
    is_suscribed=models.BooleanField(default=False,verbose_name="Está sustrito")
    user_id=models.ForeignKey(Perfil, on_delete=models.CASCADE,verbose_name="Id de usuario")
    #provider=models.ForeignKey(ConvenienceStore, on_delete=models.CASCADE, verbose_name="ID proveedor", null=True, blank=True)
    class Meta:
        verbose_name_plural="Catálogo"
    def __str__(self) -> str:
        return "%s - %s" % (self.name, self.telephone)
class ConvenienceStore(models.Model):
    name=models.CharField(max_length=30,verbose_name="Nombre")
    last_name=models.CharField(max_length=50,verbose_name="Apellidos")
    telephone=models.CharField(max_length=12,verbose_name="Teléfono")
    descripcion=models.CharField(max_length=200,verbose_name="Descripción")
    user_id=models.ForeignKey(Perfil, on_delete=models.CASCADE,verbose_name="Id de usuario")
    class Meta:
        verbose_name_plural = "ConvenienceStores"

class notifications(models.Model):
    title=models.CharField(max_length=15, default="",verbose_name="Titulo")
    description=models.CharField(max_length=40,default="",verbose_name="Descripción" )
    date=models.DateField(default=date.today(),verbose_name="Fecha")
    seen=models.BooleanField(default=False,verbose_name="Visto")
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='notifications', verbose_name="Usuario")

    def __str__(self): 
        return self.title
class directions(models.Model):
    user_id=models.ForeignKey(Perfil, on_delete=models.CASCADE,verbose_name="id de usuario")
    estate=models.CharField(max_length=20,default="",verbose_name="Estado")
    city=models.CharField(max_length=30,default="",verbose_name="Ciudad")
    cologne=models.CharField(max_length=30,default="",verbose_name="Colonia")
    street=models.CharField(max_length=30,default="",verbose_name="Calle")
    outdoor_number=models.IntegerField(validators=[MinValueValidator(0)],default=0,verbose_name="Número exterior")
    indoor_number=models.IntegerField(validators=[MinValueValidator(0)],default=0,blank=True,null=True,verbose_name="Número interior")



