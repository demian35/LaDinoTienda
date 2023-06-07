from django import forms
from .models import Products, Cart
from django.forms import ImageField

class ProductsForm(forms.ModelForm):
    photoPath = forms.ImageField()
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Nombre del producto', 'class': 'rounded-pill py-2 pr-5 mr-1'}), label='Nombre')
    price = forms.FloatField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 0, 'class': 'rounded-pill py-2 pr-5 mr-1'}), label='Precio')
    brand = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Marca', 'class': 'rounded-pill py-2 pr-5 mr-1'}), label='Marca')
    quantity = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 0, 'class': 'rounded-pill py-2 pr-5 mr-1'}), label='Cantidad Disponible')
    description = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Descripción', 'class': 'rounded-pill py-2 pr-5 mr-1'}), label='Descripción')
    
    class Meta:
        model = Products
        fields = (
            'photoPath',
            'name',
            'price',
            'brand',
            'quantity',
            'description',
        )
class cartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity == 0:
            raise forms.ValidationError("La cantidad no puede ser cero.")
        return quantity
