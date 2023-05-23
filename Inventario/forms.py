from django import forms

from Inventario.models import Inventario


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ["Nombre", "Marca", "Descripcion", "Valor", "Unidades"]
        widgets = {
            "Nombre" : forms.TextInput(attrs={"class": "form-control", "placeholder": "Escribe el nombre del producto"}),
            "Marca" : forms.TextInput(attrs={"class": "form-control" , "placeholder": "Escribe la marca"}),
            "Descripcion" : forms.Textarea(attrs={"class": "form-control", "placeholder": "Escribe la descripcion del producto"}),
            "Valor" : forms.NumberInput(attrs={"class": "form-control", "placeholder": "Escribe el precio del producto"}),
            "Unidades" : forms.NumberInput(attrs={"class": "form-control", "placeholder": "Escribe la cantidad del producto"}),
        }
        