from django import forms
from .models import Providers, ConvenienceStore,directions 


class ProvidersForm(forms.ModelForm):
    name=forms.CharField(max_length=30,label="Nombre",widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    last_name=forms.CharField(max_length=100,label="Apellido",widget=forms.TextInput(attrs={'placeholder': 'Apellidos', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    telephone=forms.CharField(max_length=12,label="Teléfono",widget=forms.TextInput(attrs={'placeholder': 'Teléfono', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    #cambiar widget
    logo=forms.CharField(max_length=100,label="Logo",widget=forms.TextInput(attrs={'placeholder': 'Logo', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    enterprise_name=forms.CharField(max_length=100,label="Empresa",widget=forms.TextInput(attrs={'placeholder': 'Empresa', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    descripcion=forms.CharField(max_length=100,label="Descripción",widget=forms.TextInput(attrs={'placeholder': 'Descripción', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    class Meta:
        model = Providers
        fields = (
            "name",
            "last_name",
            "telephone",
            "logo",
            "enterprise_name",
            "descripcion",
            
            )
class ConvenienceStoreForm(forms.ModelForm):
    name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    last_name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Apellidos', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    telephone=forms.CharField(max_length=12,widget=forms.TextInput(attrs={'placeholder': 'Telefono', 'class':'form-control rounded-pill py-2 pr-5 mr-1   '}))
    descripcion=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Descripción', 'class':'form-control rounded-pill py-2 pr-5 mr-1  '}))
    class Meta:
        model = ConvenienceStore
        fields = (
            "name",
            "last_name",
            "telephone",
            "descripcion",
        )    
class directionsForm(forms.ModelForm):
    estate=forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Estado', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    city=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Ciudad', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    cologne=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Colonia', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    street=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Calle', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    outdoor_number=forms.IntegerField(min_value=0, widget=forms.TextInput(attrs={'placeholder': 'Número exterior', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    indoor_number=forms.IntegerField(min_value=0,required=False,  widget=forms.TextInput(attrs={'placeholder': 'Número interior', 'class':'form-control rounded-pill py-2 pr-5 mr-1 '}))
    class Meta:
        model = directions
        fields = (
            "estate",
            "city",
            "cologne",
            "street",
            "outdoor_number",
        )    