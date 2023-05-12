from django import forms
from .models import Products


class ProductsForm(forms.ModelForm):
    Name=forms.CharField(max_length=20, default="Name", label="Nombre")
    PricePerMayority=forms.FloatField(min=0,default=0, label="Precio por mayoreo")
    Marca=forms.CharField(max_length=20,default="Marca",label="Marca")
    clasification=forms.CharField(max_length=50,default="clasificación",label="Clasificación")
    quantity=forms.FloatField(min=0,default=0,label="Cantidad Disponible")
    class Meta:
        model = Products
        fields = (
            "Name",
            "PricePerMayority",
            "Marca",
            "clasification",
            "quantity",
        )